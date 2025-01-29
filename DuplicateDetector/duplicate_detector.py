import os
import hashlib

def get_file_hash(file_path):
    """Generates a hash SHA256."""
    with open(file_path, 'rb') as f:
        hash = hashlib.file_digest(f, 'sha256')
    return hash.hexdigest()


def find_duplicate_media(directory_path):
    """Find duplicate videos and images inside the given directory."""
    VALID_EXTENSIONS = {
        '.jpg',
        '.jpeg',
        '.png',
        '.gif',
        '.bmp',
        '.mp4',
        '.avi',
        '.mov',
        '.mkv',
        '.mpeg',
        '.mpg'
    }
    file_hashes = {}
    duplicates = []

    for root_path, _, filenames in os.walk(directory_path):
        for file in filenames:
            if os.path.splitext(file)[1].lower() in VALID_EXTENSIONS:
                file_path = os.path.join(root_path, file)
                file_hash = get_file_hash(file_path)

                if file_hash in file_hashes:
                    duplicates.append(file_path)
                else:
                    file_hashes[file_hash] = file_path

    return duplicates
