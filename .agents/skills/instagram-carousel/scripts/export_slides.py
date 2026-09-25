import asyncio
import sys
import argparse
from pathlib import Path
from playwright.async_api import async_playwright

VIEW_W = 420
VIEW_H = 525
SCALE = 1080 / 420  # = 2.571428... for 1080x1350 output

async def export_slides(html_path: Path, output_dir: Path, total_slides: int = None):
    output_dir.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": VIEW_W, "height": VIEW_H},
            device_scale_factor=SCALE,
        )

        html_content = html_path.read_text(encoding="utf-8")
        await page.set_content(html_content, wait_until="networkidle")
        await page.wait_for_timeout(3000)  # Wait for Google Fonts to load

        # Auto-detect slides if not provided
        if total_slides is None or total_slides <= 0:
            count = await page.evaluate("""() => {
                const slides = document.querySelectorAll('.carousel-track > div, .carousel-slide');
                return slides.length || 7;
            }""")
            total_slides = int(count)

        print(f"Detectados {total_slides} slides para exportação em 1080x1350...")

        # Hide IG frame chrome, show only the slide viewport
        await page.evaluate("""() => {
            document.querySelectorAll('.ig-header, .ig-dots, .ig-actions, .ig-caption')
                .forEach(el => el.style.display = 'none');

            const frame = document.querySelector('.ig-frame');
            if (frame) {
                frame.style.cssText = 'width:420px;height:525px;max-width:none;border-radius:0;box-shadow:none;overflow:hidden;margin:0;';
            }

            const viewport = document.querySelector('.carousel-viewport');
            if (viewport) {
                viewport.style.cssText = 'width:420px;height:525px;aspect-ratio:unset;overflow:hidden;cursor:default;';
            }

            document.body.style.cssText = 'padding:0;margin:0;display:block;overflow:hidden;';
        }""")
        await page.wait_for_timeout(500)

        for i in range(total_slides):
            await page.evaluate("""(idx) => {
                const track = document.querySelector('.carousel-track');
                if (track) {
                    track.style.transition = 'none';
                    track.style.transform = 'translateX(' + (-idx * 420) + 'px)';
                }
            }""", i)
            await page.wait_for_timeout(400)

            out_file = output_dir / f"slide_{i+1:02d}.png"
            await page.screenshot(
                path=str(out_file),
                clip={"x": 0, "y": 0, "width": VIEW_W, "height": VIEW_H}
            )
            print(f"[OK] Slide {i+1}/{total_slides} exportado -> {out_file.name}")

        await browser.close()
        print(f"Exportação concluída com sucesso em: {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Export swipeable HTML carousels to 1080x1350 PNG slides")
    parser.add_argument("html", help="Path to carousel.html")
    parser.add_argument("-o", "--output", default="slides", help="Output directory")
    parser.add_argument("-n", "--slides", type=int, default=None, help="Total number of slides")
    args = parser.parse_args()

    html_path = Path(args.html)
    if not html_path.exists():
        print(f"Erro: Arquivo '{html_path}' não encontrado.", file=sys.stderr)
        sys.exit(1)

    asyncio.run(export_slides(html_path, Path(args.output), args.slides))

if __name__ == "__main__":
    main()
