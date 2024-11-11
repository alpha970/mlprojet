# ML Projet

Ce projet est un exemple d'application de Machine Learning.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Git** : pour cloner le dépôt.
- **Python** (version recommandée : 3.x) : pour exécuter le projet.
- **pip** : pour gérer les dépendances Python.

## Cloner le projet

1. Ouvrez un terminal ou une invite de commande.
2. Clonez le projet avec la commande suivante :
   ```bash
   git clone https://github.com/alpha970/mlprojet.git
3. Accédez au répertoire du projet :
   ```bash
   cd mlprojet



Installer les dépendances

1. Avec environnement virtuel (Recommandé)

   a. Créer un environnement virtuel  
   Dans le répertoire du projet, créez un environnement virtuel :
   - Sur Linux/Mac :
     ```bash
     python3 -m venv venv
   - Sur Windows :
     ```bash
     python -m venv venv

   b. Activer l'environnement virtuel  
   - Sur Linux/Mac :
     ```bash
     source venv/bin/activate
   - Sur Windows :
     ```bash
     .\venv\Scripts\activate

   c. Installer les dépendances  
   Une fois l'environnement virtuel activé, installez les dépendances à partir du fichier `requirements.txt` :
     ```bash
     pip install -r requirements.txt

3. Sans environnement virtuel

   Si vous ne souhaitez pas utiliser un environnement virtuel, vous pouvez installer directement les dépendances globalement. Pour cela, il suffit de faire :
     ```bash
     pip install -r requirements.txt

Lancer le projet

Une fois les dépendances installées, vous pouvez lancer le projet en local :
   ```bash
   flask run
