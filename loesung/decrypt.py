#!/bin/python3
import itertools

ZIP_HEADER = b'\x50\x4b\x03\x04' # known header for zip files that aren't empty

def decrypt(header, key):
    decrypted_data = []

    for index in range(len(header)):
        decrypted_byte = header[index] ^ key[index % len(key)]
        decrypted_data.append(decrypted_byte)

    return bytearray(decrypted_data)

def bruteforce(file_path):
    with open(file_path, 'rb') as file:
        encrypted_header = file.read(4)

    for count, key in enumerate(itertools.product(range(256), repeat=4), 1):
        decrypted_header = decrypt(encrypted_header, key)

        if decrypted_header == ZIP_HEADER:
            return key

    return None

def decrypt_file(input_path, output_path, key):
    with open(input_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = bytearray(len(encrypted_data))
    for i in range(len(encrypted_data)):
        decrypted_data[i] = encrypted_data[i] ^ key[i % len(key)]

    with open(output_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

if __name__ == "__main__":
    input_file = 'geheim.zip.crypt'
    output_file = 'geheim.zip'

    key = bruteforce('geheim.zip.crypt')
    if key is not None:
        print(f"Key gefunden {key}")
        decrypt_file(input_file, output_file, key)
    else:
        print("Key nicht gefunden")
