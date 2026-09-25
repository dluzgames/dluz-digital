import re

site_path = r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\sites\implantus-centro-odontologico\implantus-centro-odontologico.html'
with open(site_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Instagram Section to insert before Section 8
instagram_section = '''<!-- 7.5. SEÇÃO DE AUTORIDADE E INSTAGRAM OFICIAL -->
<section class="py-20 bg-gradient-to-b from-surface to-surface-container-low relative border-t border-outline-variant/30" id="instagram">
  <div class="max-w-7xl mx-auto px-6 md:px-12">
    <!-- Header da Seção -->
    <div class="text-center max-w-[720px] mx-auto mb-14">
      <div class="inline-flex items-center gap-2 bg-gradient-to-r from-[#833ab4]/10 via-[#fd1d1d]/10 to-[#fcb045]/10 border border-[#fd1d1d]/20 px-4 py-1.5 rounded-full mb-4">
        <svg class="w-4 h-4 fill-[#dc2743]" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        <span class="text-xs font-bold uppercase tracking-wider text-gray-800">Presença Digital & Comunidade</span>
      </div>
      <h2 class="font-headline-lg-mobile md:font-headline-lg text-headline-lg-mobile md:text-headline-lg text-[#8B1E2F] font-bold">
        Acompanhe nosso trabalho no Instagram
      </h2>
      <p class="font-body-md text-body-md text-on-surface-variant mt-3">
        Mais de <strong>12 mil pessoas</strong> acompanham as transformações de sorrisos, bastidores clínicos e orientações de saúde na <strong>@implantus.co</strong>.
      </p>
    </div>

    <!-- Instagram Profile Featured Card -->
    <div class="bg-surface-container-lowest rounded-3xl p-8 md:p-10 border border-outline-variant/40 shadow-xl max-w-4xl mx-auto mb-12">
      <div class="flex flex-col sm:flex-row items-center sm:items-start gap-6 md:gap-8">
        <!-- Avatar Oficial HD Extraído -->
        <div class="relative group shrink-0">
          <div class="w-24 h-24 sm:w-28 sm:h-28 rounded-full p-1 bg-gradient-to-tr from-[#f09433] via-[#dc2743] to-[#bc1888] shadow-lg">
            <img src="logo.png" alt="Perfil Oficial da Implantus Centro Odontológico" class="w-full h-full object-cover rounded-full bg-white p-1">
          </div>
          <span class="absolute bottom-1 right-1 bg-blue-500 text-white p-1 rounded-full text-xs shadow-md" title="Perfil Verificado">
            <span class="material-symbols-outlined text-[14px] block">check</span>
          </span>
        </div>

        <!-- Info do Perfil -->
        <div class="flex-grow text-center sm:text-left space-y-3">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div>
              <h3 class="font-headline-sm text-headline-sm font-bold text-gray-900 flex items-center justify-center sm:justify-start gap-2">
                implantus.co
              </h3>
              <p class="text-sm font-medium text-[#8B1E2F]">Implantus Centro Odontológico</p>
            </div>
            <a href="https://instagram.com/implantus.co" target="_blank" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-[#833ab4] via-[#fd1d1d] to-[#fcb045] hover:opacity-95 text-white px-6 py-2.5 rounded-full font-label-md text-label-md font-bold shadow-md transition-all active:scale-95">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              <span>Seguir no Instagram</span>
            </a>
          </div>

          <!-- Métricas -->
          <div class="flex justify-center sm:justify-start gap-8 text-sm pt-1 border-y border-gray-100 py-2.5">
            <div><strong class="font-bold text-gray-900">+12 mil</strong> <span class="text-gray-500">seguidores</span></div>
            <div><strong class="font-bold text-gray-900">4.9 ★</strong> <span class="text-gray-500">Google Reviews</span></div>
            <div><strong class="font-bold text-gray-900">Paraíso - TO</strong> <span class="text-gray-500">Unidade Centro</span></div>
          </div>

          <!-- Bio -->
          <p class="text-xs sm:text-sm text-gray-700 leading-relaxed">
            ✨ <strong>Infinity Clinic Implantes</strong> · Protocolo Sobre Implantes · Lentes de Contato Dental · Ortodontia · Clínica Geral & Reabilitação Oral. ☎️ (63) 3602-3847 · WhatsApp (63) 98481-2000.
          </p>
        </div>
      </div>
    </div>

    <!-- Mini Galeria de Imagens da Clínica -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-5xl mx-auto">
      <div class="rounded-2xl overflow-hidden shadow-md border border-outline-variant/30 group relative bg-surface-container">
        <img src="clinica_recepcao.png" alt="Recepção moderna da Implantus em Paraíso do Tocantins" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
        <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent flex items-end p-5">
          <p class="text-white text-xs font-semibold">Recepção em Mármore & Ambiente Acolhedor</p>
        </div>
      </div>

      <div class="rounded-2xl overflow-hidden shadow-md border border-outline-variant/30 group relative bg-surface-container">
        <img src="clinica_fachada.png" alt="Fachada da Implantus na Avenida Bernardo Sayão" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
        <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent flex items-end p-5">
          <p class="text-white text-xs font-semibold">Fachada na Av. Bernardo Sayão, 1414 - Centro</p>
        </div>
      </div>

      <div class="rounded-2xl overflow-hidden shadow-md border border-outline-variant/30 group relative bg-gradient-to-br from-[#8B1E2F] to-[#5A101C] p-6 flex flex-col justify-between text-white">
        <div>
          <span class="bg-white/20 text-white text-[11px] font-bold px-3 py-1 rounded-full uppercase tracking-wider inline-block mb-3">Tecnologia & Conforto</span>
          <h4 class="font-headline-sm text-headline-sm font-bold leading-tight mb-2">Cirurgia Guiada & Escaneamento 3D</h4>
          <p class="text-xs text-white/80 leading-relaxed">Procedimentos de implante com muito mais precisão, sem dor e com recuperação ultra rápida.</p>
        </div>
        <a href="https://wa.me/5563984812000?text=Olá!%20Gostaria%20de%20saber%20mais%20sobre%20os%20implantes%20guiados%20da%20Implantus." target="_blank" class="mt-4 inline-flex items-center gap-2 bg-[#25D366] text-white px-4 py-2.5 rounded-xl font-bold text-xs shadow-md hover:bg-[#20ba59] transition-colors w-fit">
          <span class="material-symbols-outlined text-[16px]">chat</span>
          Conversar com Especialista
        </a>
      </div>
    </div>
  </div>
</section>
'''

target_tag = '<!-- 8. LOCALIZAÇÃO E AGENDAMENTO HUMANIZADO -->'
if target_tag in html:
    html = html.replace(target_tag, instagram_section + '\n' + target_tag)

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

print('INSTAGRAM_SECTION_SUCCESS')
