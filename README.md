# Projet : Nebula

## Description
Nebula est un projet qui permet de créer un système de stockage de fichiers décentralisé et sécurisé. Les fichiers sont chiffrés, divisés en morceaux, et distribués sur différents nœuds. Ainsi, seul l'utilisateur ayant la clé privée peut accéder, télécharger ou supprimer ses fichiers.

### Fonctionnalités principales :
- **Chiffrement RSA (asymétrique)** : Les fichiers sont protégés par une clé publique/privée.
- **Découpage de fichiers** : Les fichiers sont divisés en morceaux pour être distribués.
- **Stockage sécurisé** : Les morceaux sont stockés dans un dossier (en local pour le moment).
- **Authentification des clés** : Seule la clé valide permet d'effectuer des manipulations sur les fichiers.

## Structure du projet

```
.
├── main.py            # Fichier principal du projet
├── client.py          # Interface utilisateur et gestion des clés RSA
├── file_manager.py    # Gestion du découpage et recomposition des fichiers
├── network.py         # Simule la communication avec les nœuds (à venir)
├── storage/           # Répertoire local pour stocker les morceaux
├── metadata.json      # Métadonnées des fichiers (BDD)
├── private_key.pem    # Clé privée RSA (générée automatiquement)
└── public_key.pem     # Clé publique RSA (générée automatiquement)
```

## Installation

Installe le framework cryptography:
```bash
pip install cryptography
```

### Lancer le projet
1. Clone ce dépôt :
```bash
git clone https://github.com/shash/Nebula.git
```
2. Accède au répertoire :
```bash
cd DecentralizedFileStorage
```
3. Lance l'application :
```bash
python main.py
```

## Utilisation
Une fois lancé, le programme offre plusieurs options dans le terminal :
1. **Envoyer un fichier (upload)** : Sélectionne un fichier à chiffrer, découper, et stocker.
2. **Télécharger un fichier (download)** : Fournis l'ID du fichier et la clé pour le récupérer.
3. **Supprimer un fichier (delete)** : Fournis l'ID et la clé pour demander la suppression.
4. **Quitter** : Ferme l'application.

## Exemple:
### Upload d'un fichier :
```
=== Bienvenue dans le lanceur Nebula ===
1. Envoyer un fichier (upload)
2. Télécharger un fichier (download)
3. Supprimer un fichier (delete)
4. Quitter
Choisissez une option : 1 ou upload
Entrez le chemin du fichier à envoyer : mots.txt
Divisez le fichier en Mo/Ko ? 
Fichier mots.txt envoyé avec succès. ID : 1234
Clé associée : la clée pour dechiffrer 
```

### Télécharger un fichier :
```
=== Bienvenue dans le stockage décentralisé ===
1. Envoyer un fichier (upload)
2. Télécharger un fichier (download)
3. Supprimer un fichier (delete)
4. Quitter
Choisissez une option : 2
Entrez l'ID du fichier à télécharger : 1234
Entrez la clé associée : b'your_generated_key'
Téléchargement et décryptage terminés.
```

## Fonctionnalités futures
- Distribution réelle des morceaux de fichiers sur des nœuds distants.
- Implémentation d'un protocole réseau décentralisée.
- Intégration d'un système de consensus pour la vérification entre les noeuds.
- Intégration d'un système de requêtes (quand l'utilisateur demande un download, tous les noeuds ayant des morceaux l'envoie à l'utilisateur pour le reconstruire).
- Mise en place de récompenses (crypto) pour les noeuds qui hébergent des fichiers externes

