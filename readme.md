## Hypotesis Open

Trabajo Final del Grado Multimedia

### Variables de entorno
```
.env.example --> .env
```

Es necesario reemplazar los archivos .env.example en todas las carpetas de los servicios y modificar los valores si fuera necesario.

### Docker Compose

#### Arrancar el proyecto
```
docker-compose up
```


## Django

Comandos más utilizados en Django

### Crear una migración
```
python manage.py makemigrations
python manage.py makemigrations --empty manager
```

### Ejecutar una migración
```
python manage.py migrate
```

### Crear proyecto
```
django-admin startproject hypotesis_context
```

### Crear aplicación
```
python manage.py startapp context
```

### Ejecutar traducciones
```
django-admin makemessages -l es
```

