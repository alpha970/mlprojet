README.txt

Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Git** : pour cloner le dépôt.
- **Python** (version recommandée : 3.x) : pour exécuter le projet.
- **pip** : pour gérer les dépendances Python.

Cloner le projet

1. Ouvrez un terminal ou une invite de commande.
2. Clonez le projet avec la commande suivante :
   git clone https://github.com/alpha970/ml_projet.git
3. Accédez au répertoire du projet :
   cd ml_projet

Installer les dépendances

1. **Avec environnement virtuel (Recommandé)**

   a. Créer un environnement virtuel
   Dans le répertoire du projet, créez un environnement virtuel :
   - Sur Linux/Mac :
      python3 -m venv venv
   - Sur Windows :
      python -m venv venv

   b. Activer l'environnement virtuel
   - Sur Linux/Mac :
      source venv/bin/activate
   - Sur Windows :
      .\venv\Scripts\activate

   c. Installer les dépendances
   Une fois l'environnement virtuel activé, installez les dépendances à partir du fichier `requirements.txt` :
      pip install -r requirements.txt

2. **Sans environnement virtuel**

   Si vous ne souhaitez pas utiliser un environnement virtuel, vous pouvez installer directement les dépendances globalement. Pour cela, il suffit de faire :
      pip install -r requirements.txt

Lancer le projet

Une fois les dépendances installées, vous pouvez lancer le projet en local. 
   
     python app.py