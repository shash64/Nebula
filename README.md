# Nebula

## Description
Nebula is a project that enables the creation of a decentralized and secure file storage system. Files are encrypted, split into chunks, and distributed across different nodes. Only the user with the private key can access, download, or delete their files.

### Key Features:
- **RSA Encryption**: Files are protected by a public/private key pair.
- **File Splitting**: Files are divided into chunks for distribution.
- **Secure Storage**: Chunks are stored in a directory (locally for now).
- **Key Authentication**: Only the valid key allows file manipulation.

## Project Structure

```
.
├── main.py # Main project file
├── client.py # User interface and RSA key management
├── file_manager.py # File splitting and reassembly management
├── network.py # Simulates communication with nodes (to be implemented)
├── storage/ # Local directory for storing chunks
├── metadata.json # File metadata (database)
├── private_key.pem # RSA private key (automatically generated)
└── public_key.pem # RSA public key (automatically generated)
```

## Installation

Install the cryptography framework:
```bash
pip install cryptography
```

### Running the Project
1. Clone this repository:
```bash
git clone https://github.com/shash64/Nebula.git
```
2. Navigate to the directory:
```bash
cd Nebula
```
3. Launch the application:
```bash
python main.py
```

## Usage
Une fois lancé, le programme permet:
1. **Upload a file (upload)** : Select a file to encrypt, split, and store.
2. **Download a file (download)** : Provide the file ID and key to retrieve and reassemble it.
3. **Delete a file (delete)** : Provide the ID and key to request deletion.
4. **Quit (quit)** : Close the app.

## Example:
### Uploading a file:
```
=== Welcome to Nebula Launcher ===
1. Upload a file
2. Download a file
3. Delete a file
4. Quit
Choose an option: 1 or upload
Enter the file path to upload: words.txt
Split the file in MB/KB? : Depending on file size
File words.txt uploaded successfully. ID: 1234
Associated key: the key to save for decryption
```

### Downloading a file:
```
=== Welcome to Nebula Launcher ===
1. Upload a file
2. Download a file
3. Delete a file
4. Quit
Choose an option: 2 or download
Enter the file ID to download: 1234
Enter the associated key: the key generated during upload
Download and decryption completed.
```

## Future Features:
- Real distribution of file chunks across remote nodes.
- Implementation of a decentralized network protocol.
- Integration of a consensus system for node verification.
- Integration of a query system (when a user requests a download, all nodes with chunks send them to the user for reassembly).
- Implementation of rewards (crypto) for nodes hosting external files.

