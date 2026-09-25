---
name: deploy-hostgator
description: Esta skill deve ser usada ao publicar páginas na hospedagem HostGator — upload via script local automático, FTP ou cPanel, criação de pastas por cliente, verificação da URL pública e HTTPS. Acione quando o usuário disser "publicar", "subir o site", "colocar no ar", "deploy", "hostgator" ou pedir para publicar (skill deploy-hostgator).
---

# Deploy de Páginas e Sites de Clientes

> ⚠️ **REGRA OFICIAL DLuz Games / DLuz Digital:**
> 1. **DEPLOY AUTOMÁTICO AO ENVIAR PROPOSTA:** Sempre que o usuário pedir para enviar para o cliente (ou "enviar a proposta", "enviar para ela/ele"), realize **AUTOMATICAMENTE** o deploy completo da aplicação no Coolify, garantindo que o site já esteja online no domínio oficial quando o cliente abrir a mensagem.
> 2. **DESTINO COOLIFY:** Todo deploy de cliente deve ser realizado no **Coolify (`coolify.dluz.com.br`)**, obrigatoriamente dentro do projeto **"Clientes Sites"** (UUID: `a96qaj5yukctlrnk31ynhoso`) no ambiente **`production`** (UUID: `cr8m0qzzynl254n2z2evaxvn`).
> Utilitário CLI local: `node prospector-de-sites/scripts/deploy-coolify.js --action list|deploy|status`

---

## Deploy no Coolify (Padrão Oficial)

- **Painel:** `https://coolify.dluz.com.br`
- **Projeto:** `Clientes Sites` (`a96qaj5yukctlrnk31ynhoso`)
- **Ambiente:** `production` (`cr8m0qzzynl254n2z2evaxvn`)
- **Servidor:** `localhost` (`y39qmwncbniv5ux9fd7cs2wt`)
- **Rede / Proxy Traefik:** `coolify` (`vac5t6k8m8ibrurv9d94iyf9`)
- **Padrão de Build:** `Dockerfile` com Nginx ou Git Repo `dluzgames/<slug>-site`
- **Domínios:** `<cliente>.com.br,https://<cliente>.dluz.com.br`

---

## Deploy Alternativo na HostGator (Legado)

## Método 1 — Publicador automático local (RECOMENDADO: instala uma vez, nunca mais clica)

A rede do sandbox do Cowork NÃO alcança FTP nem cPanel — isso vale para todo usuário. A publicação roda na máquina do usuário via um publicador instalado no agendador do Windows: a cada minuto ele verifica a fila e sobe o que houver, escondido, lendo as credenciais do config. O usuário instala UMA vez e o a skill deploy-hostgator vira 100% automático.

1. **Garanta os arquivos do publicador na pasta conectada** (copie de `references/` desta skill, sobrescrevendo versões antigas), conforme o sistema do usuário — pergunte ou detecte:
   - **Windows**: `publicar-agora.ps1`, `publicar-agora.bat`, `publicador-oculto.vbs`, `instalar-publicador.bat`.
   - **Mac**: `publicar-agora.command` e `instalar-publicador.command` (o instalador registra o publicador no launchd, a cada 60s; desinstalar = `launchctl unload` do plist com.prospector.publicador).
   Em dúvida, copie todos — cada sistema ignora os do outro.
2. **Primeira vez**: peça UM duplo clique no `instalar-publicador.bat` (Windows — cria a tarefa "ProspectorPublicador"; erro de permissão = botão direito → Executar como administrador) ou no `instalar-publicador.command` (Mac — se o macOS bloquear por segurança: botão direito → Abrir na primeira vez). Só uma vez na vida.
3. **Monte a fila**: escreva `fila-publicacao.txt` na raiz da pasta conectada, uma linha por arquivo: `caminho/local/arquivo.html|public_html/[pastaBase]/[slug]/index.html`. Inclua página (`index.html`) e capa (`proposta.html`) de cada cliente. Em até 1 minuto o publicador sobe tudo sozinho e renomeia a fila para `fila-publicada-[data].txt` (o log fica em `publicador-log.txt`).
4. **Aguarde ~90s e verifique**: confira se a fila foi renomeada e teste as URLs (verificação abaixo). Sem tarefa instalada, o fallback manual é o duplo clique no `publicar-agora.bat` (Windows) ou `publicar-agora.command` (Mac).

## Método 2 — FTP direto do sandbox (tentar primeiro, silencioso)

Antes de acionar o usuário, tente publicar você mesmo: `curl -sS --connect-timeout 15 -T [arquivo] "ftp://[servidor]/public_html/[pastaBase]/[slug]/index.html" --user "[usuario]:[senha do config]" --ftp-create-dirs` (senha lida do arquivo via script — jamais mostrada). Se funcionar, ótimo: zero ação do usuário. Se a rede do sandbox bloquear (timeout/refused), caia SEM DRAMA para o Método 1 — não insista em tentativas repetidas.

## Método 3 — Navegador (último recurso)

Se os métodos 1 e 2 falharem (ex.: curl ausente na máquina do usuário): cPanel File Manager pelo o MCP de navegador (Playwright) — o USUÁRIO faz o login dele (nunca peça a senha no chat), você navega, cria as pastas e faz upload pela interface.

## Verificação (obrigatória, após qualquer método)

1. Abra `https://[dominio]/[pastaBase]/[slug]/` e a capa `.../proposta.html` — confirme que carregam com conteúdo certo.
2. **HTTPS obrigatório**: precisa carregar com cadeado válido. Se der erro de certificado: HostGator tem SSL grátis — guie: cPanel → **SSL/TLS Status** → marcar o domínio → **Run AutoSSL** (minutos). Enquanto o HTTPS não valida, a publicação NÃO está concluída — link `http://` NUNCA vai para cliente.
3. Atualize `leads.md` + dashboard com status `publicado` e a URL.

## Teste de conexão do a configuração inicial (skill prospector-setup)

Publique `teste.html` simples ("Funcionou!") em `public_html/[pastaBase]/teste/index.html` pelo Método 2; se bloqueado, já deixe os scripts do Método 1 copiados na pasta, monte a fila com o teste e peça os 2 cliques — assim o usuário aprende o fluxo logo no setup.
