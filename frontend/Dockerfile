FROM nginx:alpine

WORKDIR /usr/share/nginx/html

# Install envsubst
RUN apk add --no-cache gettext

# Copy all frontend assets
COPY . .

# Configure Nginx
COPY nginx.conf /etc/nginx/templates/default.conf.template

# Create a script to substitute environment variables and start Nginx
RUN echo '#!/bin/sh\n\
envsubst < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf\n\
nginx -g "daemon off;"\n\
' > /docker-entrypoint.sh && chmod +x /docker-entrypoint.sh

EXPOSE 80

CMD ["/docker-entrypoint.sh"] 