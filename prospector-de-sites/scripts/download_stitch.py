import urllib.request, os

url = 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzNhMWU0MzExYzUyYjRkMGNiZjk3YmY4YTI3MTFmMGY2EgsSBxDK4vbB4hcYAZIBIwoKcHJvamVjdF9pZBIVQhM3MDQ0MzYwNDA0NDg0NzUxNjM4&filename=&opi=96797242'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')
print('Tamanho baixado do Stitch:', len(content))

target = r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\sites\implantus-centro-odontologico\implantus-centro-odontologico.html'
with open(target, 'w', encoding='utf-8') as f:
    f.write(content)

# Editor visual
editor_layer = open(r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\skills\redesign-premium\references\editor-visual.md', encoding='utf-8').read()
ini = editor_layer.find('<!-- PROSPECTOR-EDITOR-START -->')
fim = editor_layer.find('<!-- PROSPECTOR-EDITOR-END -->') + len('<!-- PROSPECTOR-EDITOR-END -->')
editor_block = editor_layer[ini:fim]

editor_html = content.replace('</body>', editor_block + '\n</body>') if '</body>' in content else content + editor_block
target_ed = r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\sites\implantus-centro-odontologico\implantus-centro-odontologico-editor.html'
with open(target_ed, 'w', encoding='utf-8') as f:
    f.write(editor_html)

print('ARQUIVOS ATUALIZADOS COM O CÓDIGO DO GOOGLE STITCH!')
