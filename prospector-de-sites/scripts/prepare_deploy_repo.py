import os
import shutil
import subprocess

staging_dir = r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\staging\srnails-site'
source_dir = r'c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\sites\sr-nails-paraiso'

dist_dir = os.path.join(staging_dir, 'dist')
os.makedirs(dist_dir, exist_ok=True)

# Copy HTML files
shutil.copy2(os.path.join(source_dir, 'sr-nails-paraiso.html'), os.path.join(dist_dir, 'index.html'))
shutil.copy2(os.path.join(source_dir, 'sr-nails-paraiso.html'), os.path.join(dist_dir, 'sr-nails-paraiso.html'))
shutil.copy2(os.path.join(source_dir, 'proposta.html'), os.path.join(dist_dir, 'proposta.html'))
shutil.copy2(os.path.join(source_dir, 'sr-nails-paraiso-editor.html'), os.path.join(dist_dir, 'sr-nails-paraiso-editor.html'))

# Copy img folder
shutil.copytree(os.path.join(source_dir, 'img'), os.path.join(dist_dir, 'img'), dirs_exist_ok=True)

# Write Dockerfile
dockerfile_lines = [
    "FROM nginx:alpine",
    "",
    "# Remove pagina padrao do Nginx",
    "RUN rm -rf /usr/share/nginx/html/*",
    "",
    "# Copia os arquivos de producao para o diretorio web do Nginx",
    "COPY dist /usr/share/nginx/html",
    "",
    "# Configuracao de roteamento com fallback e tipos MIME corretos",
    "RUN echo 'server { \\",
    "    listen 80; \\",
    "    server_name localhost; \\",
    "    location / { \\",
    "        root /usr/share/nginx/html; \\",
    "        index index.html index.htm; \\",
    "        try_files $uri $uri/ /index.html; \\",
    "    } \\",
    "    error_page 500 502 503 504 /50x.html; \\",
    "    location = /50x.html { \\",
    "        root /usr/share/nginx/html; \\",
    "    } \\",
    "}' > /etc/nginx/conf.d/default.conf",
    "",
    "EXPOSE 80",
    "",
    'CMD ["nginx", "-g", "daemon off;"]',
    ""
]

with open(os.path.join(staging_dir, 'Dockerfile'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(dockerfile_lines))

with open(os.path.join(staging_dir, '.gitignore'), 'w', encoding='utf-8') as f:
    f.write('.DS_Store\nThumbs.db\n')

print('Staged files successfully!')
print('Dist contents:', os.listdir(dist_dir))
print('Images count:', len(os.listdir(os.path.join(dist_dir, 'img'))))
