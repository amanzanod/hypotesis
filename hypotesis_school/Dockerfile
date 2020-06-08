# Etapa de compilación
FROM node:12-alpine3.10 as build-stage-school
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm cache clean --force

ENV HYP_MANAGER_URL $HYP_MANAGER_URL
ENV HYP_CONTEXT_URL $HYP_CONTEXT_URL
ENV HYP_ITEM_URL $HYP_ITEM_URL
ENV HYP_ENROL_URL $HYP_ENROL_URL

COPY . .
RUN npm run build

# Etapa de producción
FROM nginx:1.13.12-alpine as production-stage-school
COPY --from=build-stage-school /app/dist /var/www/html
RUN chown -R nginx:nginx /var/www/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
