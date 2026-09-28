import os

base_dir = r"c:\Users\dluzgg\Documents\antigravity\serene-newton"
dirs = [base_dir, os.path.join(base_dir, "blazing-energy")]

files_to_update = ["metodologia.html", "resultados.html", "equipe.html", "contato.html"]

for d in dirs:
    for f_name in files_to_update:
        f_path = os.path.join(d, f_name)
        if not os.path.exists(f_path):
            continue
        with open(f_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 1. HTML brand replacement
        old_brand_html = """        <a href="index.html" class="brand-box">
          <img src="assets/dluz_infinity.png" alt="DLuz Digital" />
          <span class="brand-title">DLuz</span>
          <span class="brand-sub">Digital</span>
        </a>"""
        new_brand_html = """        <a href="index.html" class="brand-box">
          <img src="assets/dluz_infinity.png" alt="DLuz Digital" />
          <div class="brand-text">
            <div class="brand-row">
              <span class="brand-title">DLuz</span>
              <span class="brand-sub">Digital</span>
            </div>
            <span class="brand-tagline">MARKETING DIGITAL</span>
          </div>
        </a>"""
        if old_brand_html in content:
            content = content.replace(old_brand_html, new_brand_html)
            print(f"Replaced HTML brand in {f_path}")
        
        # 2. CSS brand replacement
        old_css = """.brand-box {
        display: flex;
        align-items: center;
        gap: 12px;
        text-decoration: none;
        color: #fff;
      }"""
        new_css = """.brand-box {
        display: flex;
        align-items: center;
        gap: 12px;
        text-decoration: none;
        color: #fff;
      }
      .brand-text {
        display: flex;
        flex-direction: column;
        gap: 2px;
      }
      .brand-row {
        display: flex;
        align-items: baseline;
        gap: 5px;
        line-height: 1.1;
      }
      .brand-tagline {
        font-size: 10.5px;
        font-weight: 800;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: #38bdf8;
        line-height: 1;
        display: block;
      }"""
        if old_css in content:
            content = content.replace(old_css, new_css)
            print(f"Replaced CSS brand in {f_path}")

        # Update img height in .brand-box img if it exists
        content = content.replace(".brand-box img {\n        height: 26px;", ".brand-box img {\n        height: 30px;")

        with open(f_path, "w", encoding="utf-8") as f:
            f.write(content)

# Update menu.html
for d in dirs:
    menu_path = os.path.join(d, "menu.html")
    if not os.path.exists(menu_path):
        continue
    with open(menu_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    old_menu_brand = """        <a href="index.html" class="brand-box">
          <img src="assets/dluz_infinity.png" alt="DLuz Digital" />
          <span class="brand-title">DLuz Digital</span>
        </a>"""
    new_menu_brand = """        <a href="index.html" class="brand-box">
          <img src="assets/dluz_infinity.png" alt="DLuz Digital" />
          <div class="brand-text">
            <div class="brand-row">
              <span class="brand-title">DLuz Digital</span>
            </div>
            <span class="brand-tagline">MARKETING DIGITAL</span>
          </div>
        </a>"""
    if old_menu_brand in content:
        content = content.replace(old_menu_brand, new_menu_brand)
        print(f"Replaced HTML brand in {menu_path}")
    
    if old_css in content:
        content = content.replace(old_css, new_css)
        print(f"Replaced CSS brand in {menu_path}")
    
    content = content.replace(".brand-box img {\n        height: 26px;", ".brand-box img {\n        height: 30px;")

    with open(menu_path, "w", encoding="utf-8") as f:
        f.write(content)

print("All HTML headers updated successfully!")
