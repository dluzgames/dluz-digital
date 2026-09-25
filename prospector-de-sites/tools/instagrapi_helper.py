"""
Instagrapi Helper para Prospector de Sites
Extrai dados completos de perfis, fotos de alta resolução, carrosséis, reels e identidade visual de empresas no Instagram.
"""

import os, json, argparse
from instagrapi import Client

def get_client(session_file=None):
    cl = Client()
    # Se houver arquivo de sessão salvo, carregar
    if session_file and os.path.exists(session_file):
        try:
            cl.load_settings(session_file)
            print(f"[*] Sessão carregada de {session_file}")
        except Exception as e:
            print(f"[!] Erro ao carregar sessão: {e}")
    return cl

def fetch_profile(username, session_file=None):
    cl = get_client(session_file)
    username = username.strip().replace("https://www.instagram.com/", "").replace("https://instagram.com/", "").strip("/@")
    print(f"[*] Buscando perfil @{username} via instagrapi...")
    try:
        user_info = cl.user_info_by_username(username)
        data = {
            "pk": user_info.pk,
            "username": user_info.username,
            "full_name": user_info.full_name,
            "biography": user_info.biography,
            "follower_count": user_info.follower_count,
            "following_count": user_info.following_count,
            "media_count": user_info.media_count,
            "profile_pic_url": str(user_info.profile_pic_url),
            "profile_pic_url_hd": str(user_info.profile_pic_url_hd) if user_info.profile_pic_url_hd else None,
            "external_url": str(user_info.external_url) if user_info.external_url else None,
            "is_business": user_info.is_business,
            "category": user_info.category,
            "public_phone_number": user_info.public_phone_number,
            "public_email": user_info.public_email,
            "city_name": user_info.city_name,
            "address_street": user_info.address_street,
        }
        return data
    except Exception as e:
        print(f"[!] Erro ao buscar @{username}: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Instagrapi Helper para Prospecção")
    parser.add_argument("--profile", "-p", required=True, help="Username do Instagram (ex: implantus.co)")
    parser.add_argument("--session", "-s", help="Caminho do arquivo de sessão JSON")
    args = parser.parse_args()

    info = fetch_profile(args.profile, args.session)
    if info:
        print(json.dumps(info, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
