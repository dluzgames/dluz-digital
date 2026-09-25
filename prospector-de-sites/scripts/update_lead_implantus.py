import sqlite3

c = sqlite3.connect(r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\prospector.db')
cursor = c.cursor()
cursor.execute('SELECT slug, nome, status, urlNova FROM leads WHERE slug LIKE "%implantus%" OR nome LIKE "%Implantus%"')
rows = cursor.fetchall()
print('Implantus rows:', rows)

if rows:
    cursor.execute('''
        UPDATE leads 
        SET status = 'redesenhado', 
            urlNova = '/sites/implantus-centro-odontologico/implantus-centro-odontologico.html',
            whatsapp = '5563984812000'
        WHERE slug LIKE "%implantus%" OR nome LIKE "%Implantus%"
    ''')
    c.commit()
    print('Updated Implantus status to redesenhado with urlNova!')
