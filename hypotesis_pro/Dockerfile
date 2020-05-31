# etapa de compilación
FROM node:12-alpine3.10 as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm cache clean --force
COPY . .
RUN npm run build

# etapa de producción
FROM nginx:1.13.12-alpine as production-stage
# Copiar los archivos finales de la aplicación en la carpeta del servidor
COPY --from=build-stage /app/dist /var/www/html
# Hacer que todos los archivos pertenezcan al usuario nginx
RUN chown -R nginx:nginx /var/www/html

ENV HYP_MANAGER_URL $HYP_MANAGER_URL

# Abrir el puerto 80 del contenedor
EXPOSE 80
# Iniciar el servidor Nginx
CMD ["nginx", "-g", "daemon off;"]
