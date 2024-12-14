def split_file(data, chunk_size):
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    print(f"Fichier divisé en {len(chunks)} morceaux.")
    return chunks

def combine_chunks(chunks):
    return b"".join(chunks)

