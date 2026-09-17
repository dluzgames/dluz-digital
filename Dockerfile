FROM nginx:alpine

# Custom Nginx configuration with gzip and caching
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Static website assets
COPY index.html /usr/share/nginx/html/index.html
COPY proposta-comercial-modelo.html /usr/share/nginx/html/proposta-comercial-modelo.html
COPY assets/ /usr/share/nginx/html/assets/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
