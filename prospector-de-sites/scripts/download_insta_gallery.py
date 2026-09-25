import json
import urllib.request
import os

urls = [
    # Foto 1 - Caso Clínico / Sorriso / Paciente
    "https://instagram.fpmw6-1.fna.fbcdn.net/v/t51.82787-15/810996440_18221634751338009_5371648625375072070_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=111&_nc_map=urlgen_bucketless&ig_cache_key=Mzk5MjUwNzU0NzA2MDU0NjY3OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0ueHBpZHMuMTA4MC5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=0TdLu3Da8g0Q7kNvwHz5PtB&_nc_oc=AdqwiAPZZTZBSWo-_-zXT8WapI0GhYBk5W7OEkgPVuC4tXkQbozQtIiSzREyWvzGDEc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=instagram.fpmw6-1.fna&_nc_gid=X2SWSKB7GzDqoVHGuE8o9w&_nc_ss=7a22e&oh=00_AQJivuxyLqYDuSR9g45mb5Tl2yZfm08qisSYu3M0tkDy6Q&oe=6ABC6EE7",
    # Foto 2 - Procedimento / Equipamento / Clínica
    "https://instagram.fpmw6-1.fna.fbcdn.net/v/t51.82787-15/796640974_18220868614338009_5501317447319429608_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=101&_nc_map=urlgen_bucketless&ig_cache_key=Mzk4NzQyMzIxNzg3NTcwMzE2Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQueHBpZHMuMTA4MC5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=miabBgdz7dIQ7kNvwFPiMf7&_nc_oc=AdpDcSV4MOloT0ozAlNp-s5fIJT31RRnro5ayCWvW60gBqO2ewnIxAPDMrK72JtbCFQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=instagram.fpmw6-1.fna&_nc_gid=X2SWSKB7GzDqoVHGuE8o9w&_nc_ss=7a22e&oh=00_AQIfdXLEhm_QR65njRxI4B2cMJ1ZLn7Xi6roaCkoxuLk7A&oe=6ABC74F3",
    # Foto 3 - Alta Resolução 1440px
    "https://instagram.fpmw6-1.fna.fbcdn.net/v/t51.82787-15/784428524_18218352028338009_3998312844981961539_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=107&_nc_map=urlgen_bucketless&ig_cache_key=Mzk3MDcxOTI2NjMyNDYxMTk5Ng%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQueHBpZHMuMTQ0MC5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=CDf7y9f5FwoQ7kNvwHsP_hj&_nc_oc=AdoJti1yTu1h8G80WnRRsuaVr5iQXt82d9vc5JGSjN7l4DEZo2XVUiabIFiRXEOPflM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=instagram.fpmw6-1.fna&_nc_gid=vKcUrOT54v1b_Pr9n1DDhQ&_nc_ss=7a22e&oh=00_AQJQePYvFCUIkyDzMD02NwRsQyenH2MDTxd_obg2u3AboQ&oe=6ABC70FF",
    # Foto 4 - Protocolo
    "https://instagram.fpmw6-1.fna.fbcdn.net/v/t51.82787-15/779865881_18218052295338009_3632110343799983665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=107&_nc_map=urlgen_bucketless&ig_cache_key=Mzk2ODY5Njc0MDI1NDU4NTA3NA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0ueHBpZHMuMTQ0MC5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=qNGvQNRwEbUQ7kNvwEm1rQj&_nc_oc=AdqJCh2C7EutbDx0dgiRAfVTUYLH1PS74Lu2P9wWIN0ijffEn5K_bPRIJWDGWndAo30&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=instagram.fpmw6-1.fna&_nc_gid=vKcUrOT54v1b_Pr9n1DDhQ&_nc_ss=7a22e&oh=00_AQKYaDoq6A7eh02Tmp1oFHJX5dVAuBFrh_7Ot3EnQuN1Uw&oe=6ABC658F"
]

out_dir = r"c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\sites\implantus-centro-odontologico\fotos_instagram"
os.makedirs(out_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for idx, url in enumerate(urls):
    try:
        req = urllib.request.Request(url, headers=headers)
        target = os.path.join(out_dir, f"insta_foto_{idx+1}.jpg")
        with urllib.request.urlopen(req, timeout=15) as resp, open(target, 'wb') as f:
            f.write(resp.read())
        print(f"SUCCESS: {target}, size: {os.path.getsize(target)} bytes")
    except Exception as e:
        print(f"ERROR {idx+1}: {e}")
