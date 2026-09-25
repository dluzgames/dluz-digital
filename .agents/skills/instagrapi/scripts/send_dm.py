#!/usr/bin/env python3
"""
Instagrapi Direct Message Sender
Envia mensagens diretas (DMs) para perfis do Instagram via instagrapi.
"""

import os
import sys
import json
import argparse
from instagrapi import Client

DEFAULT_SESSION = os.path.join(os.path.dirname(__file__), "..", "session.json")

def send_direct_message(target, message, session_file=None):
    session_file = session_file or DEFAULT_SESSION
    if not os.path.exists(session_file):
        raise FileNotFoundError(f"Arquivo de sessão não encontrado: {session_file}")

    cl = Client()
    cl.load_settings(session_file)
    
    # Valida login
    try:
        my_account = cl.account_info()
        print(f"[*] Conectado como: @{my_account.username} ({my_account.full_name})")
    except Exception as e:
        raise RuntimeError(f"Falha na autenticação da sessão: {e}")

    # Limpa username
    clean_target = target.strip().replace("https://www.instagram.com/", "").replace("https://instagram.com/", "").strip("/@")
    
    # Se o target for numérico, assume user_id direto, senão busca id por username
    if clean_target.isdigit():
        user_id = int(clean_target)
    else:
        print(f"[*] Obtendo User ID para @{clean_target}...")
        try:
            user_id = cl.user_id_from_username(clean_target)
        except Exception as e:
            # Fallback buscando info de usuário
            user_info = cl.user_info_by_username(clean_target)
            user_id = user_info.pk

    print(f"[*] Destinatário User ID: {user_id}")
    print(f"[*] Enviando mensagem direta...")
    
    # Envia direct
    res = cl.direct_send(message, user_ids=[user_id])
    
    result_data = {
        "success": True,
        "target_username": clean_target,
        "target_id": str(user_id),
        "thread_id": getattr(res, "thread_id", None),
        "message_id": getattr(res, "id", None) or getattr(res, "item_id", None),
        "timestamp": str(getattr(res, "timestamp", None))
    }
    return result_data

def main():
    parser = argparse.ArgumentParser(description="Envio de Direct no Instagram via Instagrapi")
    parser.add_argument("--target", "-t", required=True, help="Username ou ID do destinatário (ex: srnailspso)")
    parser.add_argument("--message", "-m", required=True, help="Conteúdo do texto a ser enviado")
    parser.add_argument("--session", "-s", help="Caminho do arquivo de sessão JSON")
    args = parser.parse_args()

    try:
        res = send_direct_message(args.target, args.message, args.session)
        print("\n=== DIRECT ENVIADO COM SUCESSO ===")
        print(json.dumps(res, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"\n❌ Erro ao enviar direct: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
