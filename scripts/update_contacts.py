import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace WhatsApp number
text = text.replace('5563999999999', '5563981249724')

# Replace Hero card name
text = text.replace('<span>DLuz & Frya</span>', '<span>Duilio Luz & Frya</span>')
text = text.replace('Estrategista Executivo + IA 24/7', 'Duilio Luz (Fundador) + IA Frya 24/7')

# Replace Founder name
text = text.replace('<span>DLuz</span>\n                  <i class="fa-solid fa-circle-check text-brand-cyan"></i>', '<span>Duilio Luz</span>\n                  <i class="fa-solid fa-circle-check text-brand-cyan"></i>')

# Add Instagram link in header if not present
if 'https://www.instagram.com/dluz.digital.pso' not in text:
    old_header_cta = '<div class="flex items-center gap-4">'
    new_header_cta = '<div class="flex items-center gap-4">\n        <a href="https://www.instagram.com/dluz.digital.pso" target="_blank" rel="noopener noreferrer" class="text-slate-300 hover:text-pink-400 text-lg transition hidden sm:inline-flex items-center gap-1.5" title="Instagram Oficial @dluz.digital.pso"><i class="fa-brands fa-instagram text-xl text-pink-500"></i></a>'
    text = text.replace(old_header_cta, new_header_cta, 1)

# Update footer links
old_footer = '<a href="https://wa.me/5563981249724" target="_blank" class="text-brand-cyan hover:underline">Contato WhatsApp</a>'
new_footer = '<a href="https://www.instagram.com/dluz.digital.pso" target="_blank" class="hover:text-pink-400 transition flex items-center gap-1.5"><i class="fa-brands fa-instagram text-pink-500"></i> @dluz.digital.pso</a>\n        <a href="https://wa.me/5563981249724" target="_blank" class="text-brand-cyan hover:underline flex items-center gap-1.5"><i class="fa-brands fa-whatsapp text-green-400"></i> (63) 98124-9724</a>'
text = text.replace(old_footer, new_footer)

text = text.replace('Tocantins • Palmas • Brasil', 'Paraíso do Tocantins • Palmas • Brasil')

# Bio update with Duilio Luz
old_bio = 'Como desenvolvedor, produtor audiovisual e especialista em inteligência artificial, cansei de ver pequenos e médios empresários do Tocantins'
new_bio = 'Como desenvolvedor, produtor audiovisual e especialista em inteligência artificial, me chamo <strong>Duilio Luz</strong> (conhecido como <strong>DLuz</strong>) e criei a DLuz Digital ao ver empresários de Paraíso do Tocantins, Palmas e região'
text = text.replace(old_bio, new_bio)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('index.html updated!')

# 2. Update proposta-comercial-modelo.html
with open('proposta-comercial-modelo.html', 'r', encoding='utf-8') as f:
    p_text = f.read()

p_text = p_text.replace('5563999999999', '5563981249724')
p_text = p_text.replace('(63) 99999-9999', '(63) 98124-9724')
p_text = p_text.replace('<span>DLuz — Fundador & Estrategista</span>', '<span>Duilio Luz — Fundador & Diretor Executivo</span>')
p_text = p_text.replace('DLuz Digital LTDA (Tocantins — Brasil)', 'DLuz Digital (Paraíso do Tocantins & Palmas — Brasil)')
p_text = p_text.replace('WhatsApp Oficial: (63) 98124-9724', 'WhatsApp Oficial: (63) 98124-9724 • Instagram: @dluz.digital.pso')

with open('proposta-comercial-modelo.html', 'w', encoding='utf-8') as f:
    f.write(p_text)

print('proposta-comercial-modelo.html updated!')
