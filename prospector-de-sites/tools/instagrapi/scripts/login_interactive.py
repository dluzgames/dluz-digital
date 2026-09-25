#!/usr/bin/env python3
"""
Instagrapi Interactive Login
Permite ao usuário autenticar com segurança no Instagram e salvar a sessão no session.json.
Suporta autenticação de 2 fatores (2FA / SMS / TOTP) e desafios de segurança.
"""

import os
import sys
import getpass
from instagrapi import Client
from instagrapi.exceptions import (
    BadPassword,
    TwoFactorRequired,
    ChallengeRequired,
    PleaseWaitFewMinutes,
)

SESSION_PATH = os.path.join(os.path.dirname(__file__), "..", "session.json")

def challenge_code_handler(username, choice):
    print(f"\n[!] Desafio de segurança exigido pelo Instagram via {choice}.")
    code = input("Digite o código de verificação recebido (SMS/E-mail): ").strip()
    return code

def main():
    print("=" * 60)
    print("🔐 INSTAGRAPI — LOGIN OFICIAL (SESSÃO MOBILE SEGURA)")
    print("=" * 60)
    print("Este script gerará os tokens oficiais de dispositivo Android")
    print(f"e salvará em: {os.path.abspath(SESSION_PATH)}\n")

    default_user = "dluz.digital.pso"
    username = input(f"Usuário do Instagram [{default_user}]: ").strip() or default_user
    password = getpass.getpass("Senha do Instagram: ")

    if not password:
        print("❌ Senha não pode ser vazia.")
        sys.exit(1)

    cl = Client()
    cl.challenge_code_handler = challenge_code_handler

    try:
        print(f"\n[*] Conectando como @{username}...")
        cl.login(username, password)
        print("✅ Autenticado com sucesso!")

    except TwoFactorRequired:
        print("\n🔒 Autenticação de Dois Fatores (2FA) Ativa!")
        code = input("Digite o código do aplicativo autenticador ou SMS: ").strip()
        try:
            cl.login(username, password, verification_code=code)
            print("✅ 2FA validado com sucesso!")
        except Exception as e:
            print(f"❌ Falha ao validar 2FA: {e}")
            sys.exit(1)

    except BadPassword:
        print("❌ Senha incorreta! Verifique suas credenciais.")
        sys.exit(1)

    except PleaseWaitFewMinutes:
        print("⚠️ Instagram solicitou aguardar alguns minutos antes de tentar novamente.")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Erro durante o login: {e}")
        sys.exit(1)

    # Salva sessão
    os.makedirs(os.path.dirname(SESSION_PATH), exist_ok=True)
    cl.dump_settings(SESSION_PATH)
    acc = cl.account_info()
    print("\n" + "=" * 60)
    print(f"🎉 SESSÃO GRAVADA COM SUCESSO!")
    print(f"• Conta: @{acc.username}")
    print(f"• Nome: {acc.full_name}")
    print(f"• ID: {cl.user_id}")
    print(f"• Arquivo: {SESSION_PATH}")
    print("=" * 60)
    print("\nAgora você pode enviar mensagens usando a skill instagrapi normalmente!")

if __name__ == "__main__":
    main()
