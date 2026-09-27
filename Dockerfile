FROM nginx:alpine

# Custom Nginx configuration with gzip and caching
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Static website assets
COPY *.html /usr/share/nginx/html/
COPY favicon.svg /usr/share/nginx/html/favicon.svg
COPY assets/ /usr/share/nginx/html/assets/
COPY models/ /usr/share/nginx/html/models/
COPY modelos/ /usr/share/nginx/html/modelos/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
