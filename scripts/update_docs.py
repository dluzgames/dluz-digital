# Update docs
with open('docs/proposta_comercial_modelo.md', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('WhatsApp: (63) 99999-9999', 'WhatsApp: (63) 98124-9724 | Instagram: @dluz.digital.pso')
text = text.replace('DLuz — Fundador & Diretor de Tecnologia da DLuz Digital', 'Duilio Luz (DLuz) — Fundador & Diretor Executivo da DLuz Digital')
text = text.replace('Tocantins — Brasil', 'Paraíso do Tocantins & Palmas — Brasil')

with open('docs/proposta_comercial_modelo.md', 'w', encoding='utf-8') as f:
    f.write(text)

with open('docs/dluz_digital_masterplan.md', 'r', encoding='utf-8') as f:
    m_text = f.read()

m_text = m_text.replace('(63) 99999-9999', '(63) 98124-9724')
m_text = m_text.replace('DLuz Digital', 'DLuz Digital (Duilio Luz)')
m_text = m_text.replace('Palmas - TO', 'Paraíso do Tocantins & Palmas - TO')

with open('docs/dluz_digital_masterplan.md', 'w', encoding='utf-8') as f:
    f.write(m_text)

print('docs updated!')
