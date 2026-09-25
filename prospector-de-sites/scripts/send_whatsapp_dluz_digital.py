#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Oficial de Envio de WhatsApp da DLuz Digital (dluz.digital.pso)
Utiliza a sessão oficial da agência no CRM WAHA (DeskComm CRM) na VPS Hermes:
- Número: 556399432564
- Perfil: Frya - Dluz Digital
- Sessão: org_a0000000_0169a9454fd24b7aae6e565810f38365
"""

import sys
import json
import argparse
import paramiko

VPS_HOST = "207.180.228.14"
VPS_PORT = 22
VPS_USER = "root"
VPS_PASS = "455184Mdbluz"

WAHA_IP = "10.0.4.2"
WAHA_PORT = 3000
WAHA_API_KEY = "862563ecba8c8c28a4de42ba5a8dfeb9"
DLUZ_DIGITAL_SESSION = "org_a0000000_0169a9454fd24b7aae6e565810f38365"

def format_chat_id(number: str) -> str:
    cleaned = "".join(filter(str.isdigit, number))
    if not cleaned.endswith("@c.us"):
        return f"{cleaned}@c.us"
    return cleaned

def send_whatsapp_dluz_digital(number: str, text: str) -> dict:
    chat_id = format_chat_id(number)
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(VPS_HOST, port=VPS_PORT, username=VPS_USER, password=VPS_PASS, timeout=20)
    
    payload = {
        "session": DLUZ_DIGITAL_SESSION,
        "chatId": chat_id,
        "text": text
    }
    
    payload_json = json.dumps(payload, ensure_ascii=False)
    
    # Executa curl interno na VPS apontando para o container do WAHA
    cmd = (
        f'curl -s -X POST "http://{WAHA_IP}:{WAHA_PORT}/api/sendText" '
        f'-H "Content-Type: application/json" '
        f'-H "X-Api-Key: {WAHA_API_KEY}" '
        f'-d {json.dumps(payload_json)}'
    )
    
    try:
        stdin, stdout, stderr = client.exec_command(cmd)
        out = stdout.read().decode("utf-8", errors="replace").strip()
        err = stderr.read().decode("utf-8", errors="replace").strip()
        
        if not out:
            raise RuntimeError(f"Resposta vazia do WAHA. Stderr: {err}")
            
        data = json.loads(out)
        return data
    finally:
        client.close()

def main():
    parser = argparse.ArgumentParser(description="Envio de WhatsApp via DLuz Digital (WAHA CRM)")
    parser.add_argument("--number", "-n", required=True, help="Número com DDD (ex: 5563984812000)")
    parser.add_argument("--text", "-t", required=True, help="Mensagem a ser enviada")
    args = parser.parse_args()
    
    try:
        res = send_whatsapp_dluz_digital(args.number, args.text)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Erro ao enviar: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
