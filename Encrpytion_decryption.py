import gnupg

def import_key(gpg, keyfile_path):
    with open(keyfile_path, 'r') as keyfile:
        import_result = gpg.import_keys(keyfile.read())
        print(f"Import result: {import_result}")

def remove_key(gpg, key_id):
    # Delete the key
    result = gpg.delete_keys(key_id)
    if result:
        print(f"Key {key_id} successfully deleted.")
    else:
        print(f"Failed to delete key {key_id}.")

def list_keys(gpg):
    public_keys = gpg.list_keys()
    secret_keys = gpg.list_keys(True)

    print("Public Keys:")
    for key in public_keys:
        print(f"Key ID: {key['keyid']}, Type: {key['type']}, Email: {key['uids'][0]}")

    print("\nSecret Keys:")
    for key in secret_keys:
        print(f"Key ID: {key['keyid']}, Type: {key['type']}, Email: {key['uids'][0]}")

def decrypt_file(gpg, file_path, output_path):
    with open(file_path, 'rb') as encrypted_file:
        decrypted_data = gpg.decrypt_file(encrypted_file, output=output_path)
        return decrypted_data.ok
    
def encrypt_file(gpg, file_path, recipient, output_path):
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = gpg.encrypt_file(file, recipients=[recipient], output=output_path)
            if encrypted_data.ok:
                print(f"File encrypted successfully. Encrypted file saved to: {output_path}")
            else:
                print(f"Encryption failed: {encrypted_data.status}")
    except Exception as e:
        print(f"An error occurred: {e}")


def generate_key(gpg, name, email, key_type='RSA', key_length=2048):
    input_data = gpg.gen_key_input(
        name_real=name,
        name_email=email,
        key_type=key_type,
        key_length=key_length
    )
    key = gpg.gen_key(input_data)
    print(f"Key generated. Key ID: {key}")



def main():
    # Path to the GnuPG executable
    gpg_executable = r'C:\Program Files (x86)\GnuPG\bin\gpg.exe'

    # Initialize GnuPG
    gpg = gnupg.GPG(gpgbinary=gpg_executable)

    #Generate keys
    #generate_key(gpg,'kaushil','kaushil@hotmail.com','RSA',2048)
    # Import the key
    list_keys(gpg)
    #encrypt file
    encrypt_file(gpg,'test1.txt','kaushil@hotmail.com','test1.gpg')


if __name__ == "__main__":
    main()