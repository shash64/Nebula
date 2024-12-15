import os
import json
import network
import fileManager

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class Client:
    def __init__(self):
        self.metadata = {}
        self.private_key = None
        self.public_key = None
        self.load_keys()


    def generate_key(self):
        return Fernet.generate_key()


    def generate_rsa_keys(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048)
        self.public_key = self.private_key.public_key()
        self.save_keys()


    def save_keys(self):
        with open("private_key.pem", "wb") as privateKeyFile:
            privateKeyFile.write(self.private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()))
        
        with open("public_key.pem", "wb") as publicKeyFile:
            publicKeyFile.write(self.public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))


    def load_keys(self):
        if os.path.exists("private_key.pem") and os.path.exists("public_key.pem"):
            with open("private_key.pem", "rb") as privateKeyFile:
                self.private_key = serialization.load_pem_private_key(privateKeyFile.read(), password=None)

            with open("public_key.pem", "rb") as publicKeyFile:
                self.public_key = serialization.load_pem_public_key(publicKeyFile.read())

        else:
            self.generate_rsa_keys()


    def encrypt_jsonkey_with_public_key(self, key):
        return self.public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))


    def decrypt_jsonkey_with_private_key(self, encrypted_key):
        return self.private_key.decrypt(encrypted_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),label=None))


    def save_metadata(self):
        with open("metadata.json", "w") as metadataFile:
            json.dump(self.metadata, metadataFile)


    def load_metadata(self):
        if os.path.exists("metadata.json"):
            with open("metadata.json", "r") as metadataFile:
                self.metadata = json.load(metadataFile)


    def encrypt_file(self, filepath, key):
        fernet = Fernet(key)
        with open(filepath, "rb") as file:
            encrypted_data = fernet.encrypt(file.read())
        return encrypted_data


    def decrypt_file(self, encrypted_data, key, file_id):
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)
        output_path = f"decrypted_{self.metadata[file_id]['file_path'].split('/')[-1]}"
        with open(output_path, "wb") as file:
            file.write(decrypted_data)
        print(f"Fichier décrypté et sauvegardé sous {output_path}")


    def authenticate_key(self, file_id, provided_key):
        encrypted_stored_key = bytes.fromhex(self.metadata[file_id]["encrypted_key"])
        try:
            stored_key = self.decrypt_jsonkey_with_private_key(encrypted_stored_key)
            return stored_key == provided_key.encode()
        except Exception:
            return False
        

    def upload_file(self):
        filepath = input("Entrez le chemin du fichier à envoyer : ")
        if os.path.exists(filepath):
            key = self.generate_key()
            encrypted_key = self.encrypt_jsonkey_with_public_key(key)
            encrypted_data = self.encrypt_file(filepath, key)

            chunk_size = input("Divisez le fichier en Mo/Ko ? ")
            if chunk_size == "Mo":

                chunks = fileManager.split_file(encrypted_data, 1048576)
                file_id = network.upload_chunks(chunks)

                self.metadata[file_id] = {"file_path": filepath, "encrypted_key": encrypted_key.hex()}
                self.save_metadata()

                print(f"Fichier {filepath} envoyé avec succès. ID : {file_id}")
                print(f"Veuillez sauvegarder la clé associée : {key.decode()}")

            elif chunk_size == "Ko":
                chunks = fileManager.split_file(encrypted_data, 1024)
                file_id = network.upload_chunks(chunks)

                self.metadata[file_id] = {"file_path": filepath, "encrypted_key": encrypted_key.hex()}
                self.save_metadata()

                print(f"Fichier {filepath} envoyé avec succès. ID : {file_id}")
                print(f"Veuillez sauvegarder la clé associée : {key.decode()}")

        else:
            print("Fichier introuvable")


    def download_file(self):
        file_id = input("Entrez l'ID du fichier à télécharger : ")
        if file_id in self.metadata:
            provided_key = input("Entrez la clé associée : ")
            if self.authenticate_key(file_id, provided_key):
                chunks = network.download_chunks(file_id)
                if chunks:
                    encrypted_data = fileManager.combine_chunks(chunks)
                    self.decrypt_file(encrypted_data, provided_key, file_id)

                    print("Téléchargement et décryptage terminés")
                else:
                    print("Erreur lors du téléchargement des morceaux")
            else:
                print("Clé incorrecte. Accès refusé")
        else:
            print("Fichier non trouvé dans les métadonnées")


    def delete_file(self):
        file_id = input("Entrez l'ID du fichier à supprimer : ")
        if file_id in self.metadata:
            provided_key = input("Entrez la clé associée : ")
            if self.authenticate_key(file_id, provided_key):
                network.delete_chunks(file_id)
                self.metadata.pop(file_id, None)
                self.save_metadata()
                print(f"Fichier ID {file_id} supprimé avec succès")
            else:
                print("Clé incorrecte. Suppression refusée")
        else:
            print("Fichier non trouvé dans les métadonnées")


    def run(self):
        self.load_metadata()
        while True:
            print("\n=== Bienvenue dans le lanceur Nebula ===")
            print("1. Envoyer un fichier (upload)")
            print("2. Télécharger un fichier (download)")
            print("3. Supprimer un fichier (delete)")
            print("4. Quitter (quit)")
            choice = input("Choisissez une option : ")

            if choice == "1" or choice == "upload":
                self.upload_file()
            elif choice == "2" or choice == "download":
                self.load_metadata()
                self.download_file()
            elif choice == "3" or choice == "delete":
                self.load_metadata()
                self.delete_file()
            elif choice == "4" or choice == "quit":
                break

            else:
                print("Option invalide. Veuillez réessayer.")
