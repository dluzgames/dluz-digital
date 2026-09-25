import json
import urllib.request
import os

urls = [
    "https://instagram.fpmw6-1.fna.fbcdn.net/v/t51.82787-15/553357639_18136707598443802_103886013716683645_n.jpg?stp=dst-jpg_e35_p640x640_sh2.08_tt6&_nc_cat=103&_nc_map=urlgen_bucketless&ig_cache_key=MjIxODM5MTQxNTkxODMxMzI1MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IlNUT1JZLnhwaWRzLjcyMC5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=geRSC95gY4MQ7kNvwHEg5fP&_nc_oc=Adr--YrqONXGlqWJa5RhZ5RlOWF8WBJjBB9jMgBePq1dfs5Ncy2giRDmV6z7QIHqGj0&_nc_zt=23&_nc_ht=instagram.fpmw6-1.fna&_nc_gid=WYJK0D6f0mu2mvXZZ1X85g&_nc_ss=7a6a8&oh=00_AQInJHv82bkiOvhZNFsEWVN3Pogy2IE1r2Z83pk6DgCkGQ&oe=6ABC3FCA",
    "https://instagram.fpmw6-1.fna.fbcdn.net/v/t51.71878-15/533494218_745420818098956_8130002657182527925_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&_nc_map=urlgen_bucketless&ig_cache_key=MjA5MDc2MzgwNTQ2NjU4MTAxNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IlNUT1JZLnhwaWRzLjY0MC5zZHIudmlkZW9fZGVmYXVsdF9jb3Zlcl9mcmFtZS5DMyJ9&_nc_ohc=O5GzEWkbFNgQ7kNvwEPWTH4&_nc_oc=Adoi9oPSCVtNuhmRTz-XzTjMgmi1IOf9PKoaF5hUW-ZCAa54H7E3Nz3LW5jx18pgLoo&_nc_zt=23&_nc_ht=instagram.fpmw6-1.fna&_nc_gid=WYJK0D6f0mu2mvXZZ1X85g&_nc_ss=7a6a8&oh=00_AQLtkYCIuH55dUQ7LIOx7yTwtg6oVh6d4QGVoswiIss9-A&oe=6ABC7567",
    "https://instagram.fpmw6-1.fna.fbcdn.net/v/t51.82787-15/786993269_18218585263338009_811712886884714965_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=101&_nc_map=urlgen_bucketless&ig_cache_key=Mzk3MjI0NDkwMjEzNDkzODg2MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0ueHBpZHMuMTA4MC5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=2J-ZgKL453oQ7kNvwGjjEn0&_nc_oc=AdoSduUjRhQjTsD_j4C36VRnjKFAROXi1nj1QA78hClgv0pOloGd9VHX3AFu5fx3N7I&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=instagram.fpmw6-1.fna&_nc_gid=hWjpJxuilBlFuCt7dEKG6A&_nc_ss=7a22e&oh=00_AQLplmt7UboyevpdwsKjMnQEqU59ozAGl-e4IkFVom8HQg&oe=6ABC75B8",
    "https://instagram.fpmw6-1.fna.fbcdn.net/v/t51.82787-15/806082915_18220332940338009_892989190708038679_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=103&_nc_map=urlgen_bucketless&ig_cache_key=Mzk4MzkxNzI1OTQ1ODc4OTQzNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0ueHBpZHMuMTA4MC5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=drk9_OASGSAQ7kNvwHRE_wT&_nc_oc=AdryM1XjaGF9EV2GFT41NcQ0AJRlJX0AbKglzbOF4foP9u3KgV6ZJ9NdKiq78Qb9E_M&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=instagram.fpmw6-1.fna&_nc_gid=X2SWSKB7GzDqoVHGuE8o9w&_nc_ss=7a22e&oh=00_AQJbTyPegF1qTlpqxpfmZn1J5krwgIldHezYAOarNni98Q&oe=6ABC735E"
]

out_dir = r"c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\sites\implantus-centro-odontologico\fotos_instagram"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for idx, url in enumerate(urls):
    try:
        req = urllib.request.Request(url, headers=headers)
        target = os.path.join(out_dir, f"insta_foto_{idx+5}.jpg")
        with urllib.request.urlopen(req, timeout=15) as resp, open(target, 'wb') as f:
            f.write(resp.read())
        print(f"SUCCESS: {target}, size: {os.path.getsize(target)} bytes")
    except Exception as e:
        print(f"ERROR {idx+5}: {e}")
