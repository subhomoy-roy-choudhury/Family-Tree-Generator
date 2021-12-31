from cryptography.fernet import Fernet

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("tree.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("tree.key", "rb").read()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


if __name__ == "__main__":

    PATH_TREE = os.getcwd()

    if not os.path.isdir(PATH_TREE) :
        os.mkdir(PATH_TREE)

    files=[os.path.basename(x) for x in glob.glob(PATH_TREE + 'tree.key')]
    if len(files) > 0 :
        load_key()
    else :
        write_key()
        load_key()


    # args = parser.parse_args()
    # file = args.file
    # generate_key = args.generate_key
    #
    # if generate_key:
    #     write_key()
    # # load the key
    # key = load_key()
    #
    # encrypt_ = args.encrypt
    # decrypt_ = args.decrypt
    #
    # if encrypt_ and decrypt_:
    #     raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
    # elif encrypt_:
    #     encrypt(file, key)
    # elif decrypt_:
    #     decrypt(file, key)
    # else:
    #     raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
