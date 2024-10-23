import os
import random
import string
from multiprocessing import Process

def generate_random_filename(prefix, length=8):
    """Generate a random filename with a given prefix."""
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return f"{prefix}_{random_suffix}.hex"

def write_large_file(filename, size_in_bytes):
    """Write a large file with random data."""
    chunk_size = 1024 * 1024 * 100  # 100 MB chunks
    with open(filename, 'wb') as f:
        for _ in range(size_in_bytes // chunk_size):
            f.write(os.urandom(chunk_size))
        # Write any remaining bytes
        remaining_bytes = size_in_bytes % chunk_size
        if remaining_bytes > 0:
            f.write(os.urandom(remaining_bytes))

def generate_large_hex_files(prefix, size_in_gb):
    size_in_bytes = size_in_gb * 1024 * 1024 * 1024
    while True:
        filename = generate_random_filename(prefix)
        process = Process(target=write_large_file, args=(filename, size_in_bytes))
        process.start()
        print(f"Started generating {filename} with size {size_in_gb}GB")

# Example usage: Start generating files
generate_large_hex_files(.hex, 1)
