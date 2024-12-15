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
├── main.py            # Point d'entrée principal du projet
├── client.py          # Interface utilisateur et gestion des clés RSA
├── file_manager.py    # Gestion du découpage et recomposition des fichiers
├── network.py         # Simule la communication avec les nœuds
├── storage/           # Répertoire local pour stocker les morceaux
├── metadata.json      # Métadonnées des fichiers (généré automatiquement)
├── private_key.pem    # Clé privée RSA (générée automatiquement)
├── public_key.pem     # Clé publique RSA (générée automatiquement)
└── README.md          # Documentation du projet
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

## Exemple d'exécution
### Upload d'un fichier :
```
=== Bienvenue dans le stockage décentralisé ===
1. Envoyer un fichier (upload)
2. Télécharger un fichier (download)
3. Supprimer un fichier (delete)
4. Quitter
Choisissez une option : 1
Entrez le chemin du fichier à envoyer : example.txt
Fichier example.txt envoyé avec succès. ID : 1234
Clé associée : b'your_generated_key'
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
- Distribution réelle des morceaux sur des nœuds distants.
- Implémentation d'un protocole réseau (ex : Flask, gRPC).
- Amélioration de la gestion des clés avec un modèle inspiré de PGP.
- Intégration d'un système de consensus pour la vérification distribuée.

## Contribution
Les contributions sont les bienvenues !
1. Fork le dépôt.
2. Crée une branche :
```bash
git checkout -b feature-nouvelle-fonctionnalite
```
3. Effectue tes changements et commit :
```bash
git commit -m "Ajoute une nouvelle fonctionnalité"
```
4. Pousse la branche et ouvre une Pull Request.

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
