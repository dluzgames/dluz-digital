import sqlite3

c = sqlite3.connect(r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\prospector.db')
cursor = c.cursor()

lead_data = {
    'slug': 'implantus-centro-odontologico',
    'nome': 'Implantus Centro Odontológico',
    'nicho': 'odontologia',
    'cidade': 'Paraíso do Tocantins - TO',
    'nota': 4.9,
    'avaliacoes': 38,
    'email': 'contato@implantus.com.br',
    'telefone': '(63) 3602-3847',
    'whatsapp': '5563984812000',
    'siteAntigo': 'https://instagram.com/implantus.co',
    'motivo': 'Site antigo inexistente/apenas Instagram bio. Redesenhado em formato Editorial de Alto Luxo com comparador interativo e simulador 3D.',
    'status': 'redesenhado',
    'urlNova': '/sites/implantus-centro-odontologico/implantus-centro-odontologico.html',
    'obs': 'Avaliador RT Dr. Guilherme B. Pasquali. Localizado há 9 anos na Av. Bernardo Sayão, 1414.'
}

columns = ', '.join(lead_data.keys())
placeholders = ', '.join(['?'] * len(lead_data))
query = f"INSERT OR REPLACE INTO leads ({columns}) VALUES ({placeholders})"

cursor.execute(query, list(lead_data.values()))
c.commit()
print("Implantus inserido com sucesso no prospector.db como REDESENHADO!")
