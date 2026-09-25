---
name: instagrapi
description: Skill oficial para automação, envio de mensagens diretas (DMs), extração de perfis, prospecção e download de mídias no Instagram via instagrapi (https://github.com/subzeroid/instagrapi). Permite prospectar clientes, enviar propostas no Direct, buscar dados públicos e de contato de perfis e sincronizar sessões autenticadas.
triggers:
  - instagrapi
  - instagram direct
  - direct instagram
  - enviar direct instagram
  - dm instagram
  - mensagem instagram
  - direct cliente
  - subzeroid/instagrapi
  - instagram api privada
---

# Instagrapi — Instagram Private API & Direct Automation

Skill especializada para controle, extração de dados e automação de mensagens diretas (DMs) no Instagram utilizando a biblioteca oficial **`instagrapi`** ([subzeroid/instagrapi](https://github.com/subzeroid/instagrapi)).

---

## 🔑 Autenticação e Sessão Persistente

- **Arquivo de Sessão:** `C:\Users\dluzgg\.gemini\config\skills\instagrapi\session.json`
- **Conta Conectada:** `@dluz.digital.pso` (Dluz Digital Pso | Marketing Digital)
- A sessão utiliza o armazenamento nativo do `instagrapi` com tokens de dispositivo, evitando bloqueios ou reautenticações desnecessárias.

---

## 🛠️ Comandos Disponíveis via CLI

### 1. Enviar Mensagem Direta (Direct Message / DM):
Envia texto formatado ou link para qualquer perfil do Instagram via username ou ID:
```bash
python "C:\Users\dluzgg\.gemini\config\skills\instagrapi\scripts\send_dm.py" --target "usuario" --message "Olá! Preparei uma proposta para o seu negócio..."
```

### 2. Extrair Dados Completos de um Perfil:
Recupera biografia, telefone público, WhatsApp, e-mail, quantidade de seguidores/seguindo, foto em alta resolução e últimas postagens:
```bash
python "C:\Users\dluzgg\.gemini\config\skills\instagrapi\scripts\extract_profile.py" --profile "usuario" --amount 12
```

### 3. Verificar ou Atualizar Sessão:
Verifica se a conta continua ativa ou atualiza com um novo `sessionid`:
```bash
# Checar status da sessão
python "C:\Users\dluzgg\.gemini\config\skills\instagrapi\scripts\sync_session.py" --check

# Atualizar sessionid
python "C:\Users\dluzgg\.gemini\config\skills\instagrapi\scripts\sync_session.py" --sessionid "<SESSION_ID>"
```

---

## 🛡️ Boas Práticas Anti-Bloqueio
1. **Padrão Humano:** Evitar envios em massa simultâneos. Respeitar intervalos naturais entre mensagens.
2. **Personalização Real:** Sempre citar o nome da empresa e elogios específicos aos trabalhos reais encontrados no perfil.
3. **Link Único:** Incluir apenas o link oficial de demonstração (`https://<cliente>.dluz.com.br`).
