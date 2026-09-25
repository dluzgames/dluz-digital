import re

site_path = r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\sites\implantus-centro-odontologico\implantus-centro-odontologico.html'
with open(site_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Substituir imagem de estoque por foto real do Dr. Guilherme Pasquali (Avaliador Especialista)
# Na seção de diferenciais/estrutura
dr_guilherme_card = '''<div class="rounded-2xl overflow-hidden shadow-lg border border-[#8B1E2F]/20 bg-surface-container-lowest group">
  <div class="relative h-64 overflow-hidden bg-gray-100">
    <img class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500" alt="Dr. Guilherme B. Pasquali - Dentista Avaliador Especialista da Implantus" src="dr_guilherme_instagram.jpg"/>
    <div class="absolute bottom-3 left-3 bg-[#8B1E2F]/90 backdrop-blur-md px-3 py-1 rounded-full text-white text-xs font-bold flex items-center gap-1">
      <span class="material-symbols-outlined text-[14px]">verified</span>
      Avaliador Especialista
    </div>
  </div>
  <div class="p-5">
    <div class="flex items-center justify-between mb-1">
      <h5 class="font-headline-sm text-headline-sm font-bold text-[#8B1E2F]">Dr. Guilherme B. Pasquali</h5>
      <a href="https://instagram.com/dr.guilhermebpasquali" target="_blank" class="text-xs text-pink-600 font-semibold hover:underline">@dr.guilhermebpasquali</a>
    </div>
    <p class="font-body-sm text-body-sm text-on-surface-variant text-xs leading-relaxed mt-2">
      Dedica-se a entender as necessidades de cada paciente desde a primeira consulta. <strong>Há 9 anos no mesmo endereço na Av. Bernardo Sayão, 1414</strong> (ao lado do Posto Andrade).
    </p>
  </div>
</div>'''

# Replace the scanner box or comfort box with Dr. Guilherme's profile
old_box_pattern = re.compile(r'<div class="rounded-2xl overflow-hidden shadow-md border border-outline-variant/30 bg-surface-container-lowest">\s*<img class="w-full h-56 object-cover[^>]+data-alt="Modern 3D digital dental scanner[^>]+>\s*<div class="p-4">\s*<h5 class="font-label-lg text-label-lg font-bold text-\[#8B1E2F\]">Scanner Intraoral 3D</h5>.*?</div>\s*</div>', re.DOTALL)
if old_box_pattern.search(html):
    html = old_box_pattern.sub(dr_guilherme_card, html, count=1)
else:
    # Fallback search
    target_str = '<div class="rounded-2xl overflow-hidden shadow-md border border-outline-variant/30 bg-surface-container-lowest">\n<img class="w-full h-56 object-cover hover:scale-105 transition-transform duration-500" data-alt="Modern 3D digital dental scanner'
    if target_str in html:
        # replace block
        end_idx = html.find('</div>\n</div>\n<div class="rounded-2xl p-6 bg-[#8B1E2F]-container', html.find(target_str)) + len('</div>\n</div>')
        html = html[:html.find(target_str)] + dr_guilherme_card + html[end_idx:]

# 2. Inserir o caso real do Instagram do Protocolo sobre Implantes na seção de Depoimentos
# O post real: https://www.instagram.com/p/DcgP_Asmy-M/ com a foto caso_clinico_instagram.jpg
caso_real_card = '''<!-- Depoimento Real Oficial do Instagram (Post https://www.instagram.com/p/DcgP_Asmy-M/) -->
<div class="bg-surface-container-lowest rounded-2xl overflow-hidden border-2 border-[#8B1E2F]/30 shadow-md flex flex-col justify-between relative group hover:border-[#8B1E2F] transition-all">
  <div class="relative h-44 overflow-hidden bg-gray-900">
    <img src="caso_clinico_instagram.jpg" alt="Caso Clínico Real de Protocolo sobre Implantes na Implantus" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
    <div class="absolute top-2 right-2 bg-gradient-to-r from-[#833ab4] via-[#fd1d1d] to-[#fcb045] text-white px-2.5 py-0.5 rounded-full text-[10px] font-bold flex items-center gap-1 shadow">
      <svg class="w-3 h-3 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
      Instagram Real
    </div>
  </div>
  <div class="p-6">
    <div class="flex text-amber-500 text-sm mb-3">★★★★★</div>
    <p class="font-body-md text-body-md text-on-surface font-semibold italic leading-relaxed mb-4 text-sm">
      “Eu deixei de comprar um automóvel para investir no meu tratamento dentário. Conquistei liberdade, conforto e qualidade de vida!”
    </p>
    <div class="pt-3 border-t border-outline-variant/20 flex items-center justify-between">
      <div>
        <p class="font-label-sm text-label-sm font-bold text-[#8B1E2F]">Paciente de Protocolo</p>
        <p class="text-[11px] text-gray-500">Reabilitação Oral sobre Implantes</p>
      </div>
      <a href="https://www.instagram.com/p/DcgP_Asmy-M/?img_index=1" target="_blank" class="text-xs text-[#8B1E2F] hover:text-secondary font-bold inline-flex items-center gap-1">
        Ver post ↗
      </a>
    </div>
  </div>
</div>'''

depo_1_old = '''<!-- Depoimento 1 -->
<div class="bg-surface-container-lowest rounded-2xl p-7 border border-outline-variant/30 shadow-sm flex flex-col justify-between relative group hover:border-secondary transition-colors">
<div>
<div class="flex text-amber-500 text-sm mb-4">★★★★★</div>
<p class="font-body-md text-body-md text-on-surface italic leading-relaxed mb-6">
              "Voltei a comer castanhas e churrasco sem nenhum medo de a prótese sair. O procedimento de protocolo foi tranquilo e sem dor. Sou outra pessoa!"
            </p>
</div>
<div class="flex items-center gap-3 pt-4 border-t border-outline-variant/20">
<div class="w-10 h-10 rounded-full bg-primary-container text-secondary-fixed flex items-center justify-center font-bold text-sm">
              MH
            </div>
<div>
<p class="font-label-lg text-label-lg font-bold text-[#8B1E2F]">Maria Helena S.</p>
<p class="font-body-sm text-body-sm text-outline text-xs">Paraíso do Tocantins</p>
</div>
</div>
</div>'''

if depo_1_old in html:
    html = html.replace(depo_1_old, caso_real_card)

with open(site_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Atualizar versão do editor visual
editor_layer = open(r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\skills\redesign-premium\references\editor-visual.md', encoding='utf-8').read()
ini = editor_layer.find('<!-- PROSPECTOR-EDITOR-START -->')
fim = editor_layer.find('<!-- PROSPECTOR-EDITOR-END -->') + len('<!-- PROSPECTOR-EDITOR-END -->')
editor_block = editor_layer[ini:fim]

editor_html = html.replace('</body>', editor_block + '\n</body>') if '</body>' in html else html + editor_block
with open(site_path.replace('.html', '-editor.html'), 'w', encoding='utf-8') as f:
    f.write(editor_html)

print('POST_IMAGES_INTEGRATED_SUCCESS')
