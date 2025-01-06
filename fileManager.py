def split_file(data, num_chunks, chunk_size, remaining):
    chunks = []
    start = 0
    for i in range(num_chunks):
        end = start + chunk_size + (1 if i<remaining else 0)
        chunks.append(data[start:end])
        start = end
    return chunks

def combine_chunks(chunks):
    total_size = sum(len(chunk) for chunk in chunks)
    print(f"Taille totale des morceaux: {total_size} octets")
    return b"".join(chunks)
