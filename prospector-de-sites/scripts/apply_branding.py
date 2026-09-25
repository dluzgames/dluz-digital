import re, os

site_path = r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\sites\implantus-centro-odontologico\implantus-centro-odontologico.html'
with open(site_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Atualizar paleta de cores para o Vinho Bordô oficial da fachada e do logo (#8B1E2F)
html = html.replace('"primary": "#002532"', '"primary": "#8B1E2F"')
html = html.replace('"primary-container": "#0d3b4c"', '"primary-container": "#6E1321"')
html = html.replace('"primary-fixed": "#bfe9fe"', '"primary-fixed": "#FCE7EB"')
html = html.replace('"primary-fixed-dim": "#a4cce1"', '"primary-fixed-dim": "#F7CAD2"')
html = html.replace('bg-primary', 'bg-[#8B1E2F]')
html = html.replace('border-primary-container', 'border-[#6E1321]')
html = html.replace('text-primary', 'text-[#8B1E2F]')

# 2. Corrigir telefones e WhatsApp
html = html.replace('(63) 3602-0000', '(63) 3602-3847')
html = html.replace('(63) 99999-9999', '(63) 98481-2000')
html = html.replace('5563999999999', '5563984812000')

# 3. Adicionar Instagram no Top Notice Bar
top_bar_old = '''<div class="flex items-center gap-4 text-xs">
<span class="bg-primary-container text-secondary-fixed px-2.5 py-0.5 rounded-full font-label-md text-label-md uppercase tracking-wider flex items-center gap-1">
<span class="material-symbols-outlined text-secondary-fixed text-[14px]" style="font-variation-settings: 'FILL' 1;">verified</span>
          Atendimento Humanizado
        </span>
<a class="hover:text-secondary-fixed transition-colors font-label-md text-label-md flex items-center gap-1 text-surface-bright" href="tel:6336020000">'''

top_bar_new = '''<div class="flex items-center gap-4 text-xs">
<a href="https://instagram.com/implantus.co" target="_blank" class="bg-gradient-to-r from-[#833ab4] via-[#fd1d1d] to-[#fcb045] text-white px-3 py-1 rounded-full font-label-md text-label-md flex items-center gap-1.5 shadow-sm hover:opacity-90 transition-opacity">
  <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
  <span>Instagram @implantus.co</span>
  <span class="bg-white/20 px-1.5 py-0.2 rounded-full text-[10px] font-bold">+12 mil seguidores</span>
</a>
<span class="bg-[#6E1321] text-secondary-fixed px-2.5 py-0.5 rounded-full font-label-md text-label-md uppercase tracking-wider flex items-center gap-1">
<span class="material-symbols-outlined text-secondary-fixed text-[14px]" style="font-variation-settings: 'FILL' 1;">verified</span>
          Atendimento Humanizado
        </span>
<a class="hover:text-secondary-fixed transition-colors font-label-md text-label-md flex items-center gap-1 text-surface-bright" href="tel:6336023847">'''

if top_bar_old in html:
    html = html.replace(top_bar_old, top_bar_new)

# 4. Substituir logo no Navbar pelo logo real da Implantus
logo_nav_old = '''<!-- Logo Marca -->
<a class="flex items-center gap-3 group" href="#">
<div class="w-10 h-10 rounded-xl bg-primary-container flex items-center justify-center text-secondary-fixed shadow-inner transition-transform group-hover:scale-105">
<span class="material-symbols-outlined text-[24px]">dentistry</span>
</div>
<div>
<span class="font-headline-md text-headline-md font-semibold text-primary tracking-tight block leading-none">Implantus</span>
<span class="font-label-sm text-label-sm uppercase tracking-widest text-secondary block mt-0.5">Centro Odontológico</span>
</div>
</a>'''

logo_nav_new = '''<!-- Logo Marca Oficial da Implantus -->
<a class="flex items-center gap-3 group" href="#">
  <img src="logo.png" alt="Logo Implantus Centro Odontológico" class="h-12 w-auto object-contain rounded-lg border border-[#8B1E2F]/20 p-1 bg-white shadow-sm transition-transform group-hover:scale-105">
  <div>
    <span class="font-headline-md text-headline-md font-bold text-[#8B1E2F] tracking-tight block leading-none">Implantus</span>
    <span class="font-label-sm text-label-sm uppercase tracking-widest text-secondary block mt-0.5">Centro Odontológico</span>
  </div>
</a>'''

if logo_nav_old in html:
    html = html.replace(logo_nav_old, logo_nav_new)

# 5. Adicionar botão do Instagram ao lado do WhatsApp no Navbar
nav_actions_old = '''<div class="flex items-center gap-3">
<a class="hidden sm:inline-flex items-center gap-2 bg-[#25D366] hover:bg-[#20ba59] text-white px-5 py-2.5 rounded-full font-label-lg text-label-lg transition-all duration-200 ease-in-out active:scale-95 whatsapp-glow font-semibold" href="https://wa.me/5563999999999?text=Olá!%20Gostaria%20de%20agendar%20uma%20consulta%20na%20Implantus" rel="noopener noreferrer" target="_blank">'''

nav_actions_new = '''<div class="flex items-center gap-3">
<a class="hidden lg:inline-flex items-center gap-2 bg-gradient-to-r from-[#833ab4] via-[#fd1d1d] to-[#fcb045] hover:opacity-90 text-white px-4 py-2.5 rounded-full font-label-lg text-label-lg transition-all duration-200 ease-in-out active:scale-95 font-semibold shadow-sm" href="https://instagram.com/implantus.co" rel="noopener noreferrer" target="_blank" title="Instagram Oficial com mais de 12 mil seguidores">
<svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
<span>@implantus.co</span>
<span class="bg-white/20 px-1.5 py-0.5 rounded-full text-[11px]">+12k</span>
</a>
<a class="hidden sm:inline-flex items-center gap-2 bg-[#25D366] hover:bg-[#20ba59] text-white px-5 py-2.5 rounded-full font-label-lg text-label-lg transition-all duration-200 ease-in-out active:scale-95 whatsapp-glow font-semibold" href="https://wa.me/5563984812000?text=Olá!%20Gostaria%20de%20agendar%20uma%20consulta%20na%20Implantus" rel="noopener noreferrer" target="_blank">'''

if nav_actions_old in html:
    html = html.replace(nav_actions_old, nav_actions_new)

# 6. Atualizar a foto do Hero para a foto real da recepção em mármore da clínica
hero_img_pattern = re.compile(r'<img class="w-full h-\[460px\][^>]+src="[^"]+"/>')
new_hero_img = '<img class="w-full h-[460px] object-cover object-center transform hover:scale-105 transition-transform duration-700" alt="Recepção real da Implantus Centro Odontológico em Paraíso do Tocantins" src="clinica_recepcao.png"/>'
html = hero_img_pattern.sub(new_hero_img, html, count=1)

# 7. Adicionar Card de Destaque do Instagram no Hero
hero_social_card = '''<!-- Floating Instagram & Social Proof Card -->
<div class="absolute -top-4 -right-4 bg-white/95 backdrop-blur-md p-3.5 rounded-2xl shadow-xl border border-[#8B1E2F]/20 flex items-center gap-3 max-w-xs z-20">
  <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-[#f09433] via-[#dc2743] to-[#bc1888] text-white flex items-center justify-center shrink-0 shadow-md">
    <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
  </div>
  <div>
    <a href="https://instagram.com/implantus.co" target="_blank" class="font-label-md text-label-md font-bold text-gray-900 hover:text-[#8B1E2F] flex items-center gap-1">@implantus.co <span class="text-xs text-blue-500">✔</span></a>
    <p class="font-body-sm text-body-sm text-gray-600 text-xs">+12 mil seguidores no Instagram</p>
  </div>
</div>'''

html = html.replace('<div class="rounded-3xl overflow-hidden shadow-2xl', hero_social_card + '\n<div class="rounded-3xl overflow-hidden shadow-2xl')

# 8. Na seção de localização, mostrar a fachada real da clínica
map_img_pattern = re.compile(r'<img class="w-full h-full object-cover"[^>]+src="https://lh3.googleusercontent.com/aida-public/AB6AXuAn3[^"]+"/>')
new_facade_img = '<img class="w-full h-full object-cover" alt="Fachada real da Implantus na Av. Bernardo Sayão em Paraíso do Tocantins" src="clinica_fachada.png"/>'
html = map_img_pattern.sub(new_facade_img, html, count=1)

# 9. No Footer, adicionar o Instagram oficial e o logo real
footer_logo_old = '''<div class="w-8 h-8 rounded-lg bg-surface-container-lowest/15 text-secondary-fixed flex items-center justify-center">
<span class="material-symbols-outlined text-[20px]">dentistry</span>
</div>
<span class="font-headline-md text-headline-md text-surface-bright font-semibold">Implantus</span>'''

footer_logo_new = '''<div class="flex items-center gap-3">
  <img src="logo.png" alt="Logo Implantus" class="h-10 w-auto object-contain rounded bg-white p-1 shadow-sm">
  <span class="font-headline-md text-headline-md text-surface-bright font-bold">Implantus</span>
</div>'''

if footer_logo_old in html:
    html = html.replace(footer_logo_old, footer_logo_new)

# Adicionar links sociais no Footer
footer_links_old = '''<div class="flex items-center gap-4 shrink-0">
<span class="text-secondary-fixed font-medium">Implantus Odontologia Digital</span>
</div>'''

footer_links_new = '''<div class="flex items-center gap-4 shrink-0">
<a href="https://instagram.com/implantus.co" target="_blank" class="flex items-center gap-1.5 text-secondary-fixed hover:text-white transition-colors">
  <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
  <span>Instagram @implantus.co (+12k)</span>
</a>
<a href="https://wa.me/5563984812000" target="_blank" class="text-secondary-fixed hover:text-white transition-colors">WhatsApp (63) 98481-2000</a>
</div>'''

if footer_links_old in html:
    html = html.replace(footer_links_old, footer_links_new)

with open(site_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Atualizar também a versão do editor visual
editor_layer = open(r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\skills\redesign-premium\references\editor-visual.md', encoding='utf-8').read()
ini = editor_layer.find('<!-- PROSPECTOR-EDITOR-START -->')
fim = editor_layer.find('<!-- PROSPECTOR-EDITOR-END -->') + len('<!-- PROSPECTOR-EDITOR-END -->')
editor_block = editor_layer[ini:fim]

editor_html = html.replace('</body>', editor_block + '\n</body>') if '</body>' in html else html + editor_block
with open(site_path.replace('.html', '-editor.html'), 'w', encoding='utf-8') as f:
    f.write(editor_html)

print('APPLIED_BRANDING_SUCCESS')
