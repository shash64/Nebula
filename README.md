# Nebula

## Description
Nebula est un projet qui permet de créer un système de stockage de fichiers décentralisé et sécurisé. Les fichiers sont chiffrés, divisés en morceaux et distribués sur différents nœuds, ainsi, seul l'utilisateur ayant la clé privée peut accéder, télécharger ou supprimer ses fichiers.

### Fonctionnalités principales:
- **Chiffrement RSA** : Les fichiers sont protégés par une clé publique/privée.
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

Installation du framework cryptography:
```bash
pip install cryptography
```

### Lancer le projet
1. Cloner ce dépôt :
```bash
git clone https://github.com/shash64/Nebula.git
```
2. Accèder au répertoire :
```bash
cd Nebula
```
3. Lancer l'application :
```bash
python main.py
```

## Utilisation
Une fois lancé, le programme permet:
1. **Envoyer un fichier (upload)** : Sélectionne un fichier à chiffrer, découper et stocker.
2. **Télécharger un fichier (download)** : Fournis l'ID du fichier et la clé pour le récupérer et le recompiler.
3. **Supprimer un fichier (delete)** : Fournis l'ID et la clé pour demander la suppression.
4. **Quitter (quit)** : Ferme l'application.

## Exemple:
### Upload d'un fichier:
```
=== Bienvenue dans le lanceur Nebula ===
1. Envoyer un fichier (upload)
2. Télécharger un fichier (download)
3. Supprimer un fichier (delete)
4. Quitter (quit)
Choisissez une option : 1 ou upload
Entrez le chemin du fichier à envoyer : mots.txt
Divisez le fichier en Mo/Ko ? : Selon la taille du fichier 
Fichier mots.txt envoyé avec succès. ID : 1234
Clé associée : la clé à sauvegarder pour déchiffrer les fichiers
```

### Télécharger un fichier:
```
=== Bienvenue dans le lanceur Nebula ===
1. Envoyer un fichier (upload)
2. Télécharger un fichier (download)
3. Supprimer un fichier (delete)
4. Quitter (quit)
Choisissez une option : 2 ou download
Entrez l'ID du fichier à télécharger : 1234
Entrez la clé associée : la clé générée lors de l'upload
Téléchargement et décryptage terminés.
```

## Fonctionnalités futures:
- Distribution réelle des morceaux de fichiers sur des nœuds distants.
- Implémentation d'un protocole réseau décentralisée.
- Intégration d'un système de consensus pour la vérification entre les noeuds.
- Intégration d'un système de requêtes (quand l'utilisateur demande un download, tous les noeuds ayant des morceaux l'envoie à l'utilisateur pour le reconstruire).
- Mise en place de récompenses (crypto) pour les noeuds qui hébergent des fichiers externes

