import os
import random

def upload_chunks(chunks):
    file_id = str(random.randint(1000, 99999))
    storage_dir = f"storage/{file_id}"
    os.makedirs(storage_dir, exist_ok=True)
    print(f"Envoi des morceaux pour le fichier ID : {file_id}...")
    for i, chunk in enumerate(chunks):
        chunk_path = os.path.join(storage_dir, f"chunk_{i}.bin")
        with open(chunk_path, "wb") as chunk_file:
            chunk_file.write(chunk)
        print(f"Morceau {i + 1} sauvegardé à {chunk_path}. Taille : {len(chunk)} octets.")
    return file_id


def download_chunks(file_id):
    storage_dir = f"storage/{file_id}"
    if not os.path.exists(storage_dir):
        print(f"Aucun fichier trouvé pour l'ID : {file_id}")
        return []

    
    print(f"Téléchargement des morceaux pour le fichier ID : {file_id}...")
    chunks = []
    for chunk_file in sorted(os.listdir(storage_dir)):
        chunk_path = os.path.join(storage_dir, chunk_file)
        with open(chunk_path, "rb") as cf:
            chunks.append(cf.read())
        print(f"Morceau {chunk_file} chargé.")
    return chunks


def delete_chunks(file_id):
    storage_dir = f"storage/{file_id}"
    if os.path.exists(storage_dir):
        for chunk_file in os.listdir(storage_dir):
            os.remove(os.path.join(storage_dir, chunk_file))
        os.rmdir(storage_dir)
        print(f"Tous les morceaux pour le fichier ID {file_id} ont été supprimés.")
    else:
        print(f"Aucun fichier trouvé pour l'ID : {file_id}.")
