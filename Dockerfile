# Image officielle Python comme base
FROM python:3.9

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers de l'application
COPY app.py /app/
COPY requirements.txt /app/

# Installation des dépendances
RUN pip install -r requirements.txt

# Port exposé par le conteneur
EXPOSE 5000

# Commande de lancement
CMD ["python", "app.py"]

