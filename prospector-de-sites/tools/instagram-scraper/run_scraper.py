import os, sys, json, argparse

def main():
    parser = argparse.ArgumentParser(description="Instagram Scraper Runner (ScraperHub / Crawlbase)")
    parser.add_argument("--profile", "-p", help="Instagram username or URL to scrape")
    parser.add_argument("--post", help="Instagram post URL to scrape")
    parser.add_argument("--hashtag", help="Instagram hashtag to scrape")
    parser.add_argument("--token", help="Crawlbase API Token (optional, can also be read from env CRAWLBASE_TOKEN or prospector-config.json)")
    args = parser.parse_args()

    token = args.token or os.environ.get("CRAWLBASE_TOKEN")
    if not token:
        # Tentar ler do prospector-config.json
        cfg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "dashboard", "prospector-config.json"))
        if os.path.exists(cfg_path):
            try:
                with open(cfg_path, "r", encoding="utf-8") as f:
                    cfg = json.load(f)
                    token = cfg.get("crawlbase_token") or cfg.get("prospeccao", {}).get("crawlbase_token")
            except Exception:
                pass

    if args.profile:
        username = args.profile.strip().replace("https://www.instagram.com/", "").replace("https://instagram.com/", "").strip("/@")
        url = f"https://www.instagram.com/{username}/"
        print(f"[*] Alvo: {url}")
        if token:
            from crawlbase import CrawlingAPI
            api = CrawlingAPI({"token": token})
            res = api.get(url, options={"scraper": "instagram-profile"})
            if res.get("statusCode") == 200:
                data = json.loads(res.get("body", "{}")) if isinstance(res.get("body"), str) else res.get("body")
                print(json.dumps(data, indent=2, ensure_ascii=False))
                return
            else:
                print(f"[!] Erro Crawlbase: {res.get('statusCode')}")
        else:
            print("[i] Token do Crawlbase não configurado. Para usar a API direta do ScraperHub/Crawlbase, adicione crawlbase_token no prospector-config.json.")
            print("[i] Usando fallback local para inspeção pública...")

if __name__ == "__main__":
    main()
