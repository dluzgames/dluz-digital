#!/usr/bin/env python3
"""
Instagrapi Profile & Media Extractor
Extrai dados completos de perfil, bio, telefones, links e mídias de alta resolução.
"""

import os
import sys
import json
import argparse
from instagrapi import Client

DEFAULT_SESSION = os.path.join(os.path.dirname(__file__), "..", "session.json")

def extract_profile(username, session_file=None, media_count=12):
    session_file = session_file or DEFAULT_SESSION
    cl = Client()
    if os.path.exists(session_file):
        cl.load_settings(session_file)

    clean_user = username.strip().replace("https://www.instagram.com/", "").replace("https://instagram.com/", "").strip("/@")
    print(f"[*] Extraindo perfil @{clean_user}...")

    user_info = cl.user_info_by_username(clean_user)
    
    data = {
        "pk": str(user_info.pk),
        "username": user_info.username,
        "full_name": user_info.full_name,
        "biography": user_info.biography,
        "follower_count": user_info.follower_count,
        "following_count": user_info.following_count,
        "media_count": user_info.media_count,
        "is_private": user_info.is_private,
        "is_verified": user_info.is_verified,
        "profile_pic_url_hd": str(user_info.profile_pic_url_hd or user_info.profile_pic_url),
        "external_url": str(user_info.external_url) if user_info.external_url else None,
        "public_phone_number": getattr(user_info, "public_phone_number", None),
        "public_email": getattr(user_info, "public_email", None),
        "category": getattr(user_info, "category", None),
        "city_name": getattr(user_info, "city_name", None),
        "address_street": getattr(user_info, "address_street", None),
        "recent_medias": []
    }

    if media_count > 0:
        print(f"[*] Baixando últimas {media_count} mídias...")
        try:
            medias = cl.user_medias(user_info.pk, amount=media_count)
            for m in medias:
                m_info = {
                    "id": str(m.id),
                    "code": m.code,
                    "caption": m.caption_text[:100] if m.caption_text else "",
                    "media_type": m.media_type,
                    "like_count": m.like_count,
                    "comment_count": m.comment_count,
                    "thumbnail_url": str(m.thumbnail_url) if m.thumbnail_url else None,
                    "resources": [str(r.thumbnail_url or r.video_url) for r in (m.resources or [])]
                }
                data["recent_medias"].append(m_info)
        except Exception as e:
            print(f"[!] Erro ao obter mídias: {e}")

    return data

def main():
    parser = argparse.ArgumentParser(description="Extração de Perfil no Instagram via Instagrapi")
    parser.add_argument("--profile", "-p", required=True, help="Username do Instagram (ex: srnailspso)")
    parser.add_argument("--amount", "-a", type=int, default=12, help="Quantidade de mídias para extrair")
    parser.add_argument("--session", "-s", help="Caminho do arquivo de sessão JSON")
    args = parser.parse_args()

    try:
        data = extract_profile(args.profile, args.session, args.amount)
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"❌ Erro ao extrair perfil: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
