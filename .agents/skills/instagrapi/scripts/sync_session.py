#!/usr/bin/env python3
"""
Instagrapi Session Manager
Valida a sessão atual ou atualiza o session.json via sessionid ou credenciais.
"""

import os
import sys
import json
import argparse
from instagrapi import Client

SESSION_PATH = os.path.join(os.path.dirname(__file__), "..", "session.json")

def check_session():
    if not os.path.exists(SESSION_PATH):
        print(f"❌ Sessão não encontrada em: {SESSION_PATH}")
        return False
    cl = Client()
    try:
        cl.load_settings(SESSION_PATH)
        acc = cl.account_info()
        print(f"✅ Sessão Ativa! Logado como: @{acc.username} (ID: {cl.user_id})")
        return True
    except Exception as e:
        print(f"⚠️ Sessão inválida ou expirada: {e}")
        return False

def login_with_sessionid(session_id):
    cl = Client()
    print(f"[*] Autenticando com sessionid...")
    cl.login_by_sessionid(session_id)
    cl.dump_settings(SESSION_PATH)
    acc = cl.account_info()
    print(f"✅ Login realizado com sucesso! Salvo em {SESSION_PATH}")
    print(f"Usuário: @{acc.username} (ID: {cl.user_id})")
    return True

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de Sessão do Instagrapi")
    parser.add_argument("--check", action="store_true", help="Verificar status da sessão atual")
    parser.add_argument("--sessionid", help="Atualizar sessão com novo sessionid do Instagram")
    args = parser.parse_args()

    if args.sessionid:
        login_with_sessionid(args.sessionid)
    else:
        check_session()

if __name__ == "__main__":
    main()
