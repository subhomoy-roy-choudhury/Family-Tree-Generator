from family_tree import FamilyTree
import pickle
import os
import sys
import glob
import re
import hashlib
from cryptography.fernet import Fernet
from exception_decor import exception
from whaaaaat import prompt, print_json, Separator

def tree_command_parser(func):
    def wrapper(*args, **kwargs):
        x = re.findall(r"member<*[a-zA-Z]{1,},[0-9]>",args[0])
        result = []
        if len(x) == 0 :
            return "wrong command"
        for item in x:
            item = re.findall(r"[a-zA-Z]{1,},.[0-9]*",item)
            result.append(item[0].split(','))
        return func(result)
    return wrapper

#### Saving Objects as Pickle
class PickleTree :
    def save_pickle(self,file,object):
        # object = FamilyTree(5,'hfolsdhf')
        with open(f'pickles/{file}', 'wb') as f :
            pickle.dump(object, f)

    def unpickle(self,file) :
        with open(f'pickles/{file}', "rb") as f :
            loaded_object = pickle.load(f)
        return loaded_object

def custom_select(name,message,choices):
    questions = [
        {
            "type": "list",
            "name": name,
            "message": message,
            "choices": choices,
            "filter" : lambda val: val.lower(),
        },
    ]
    answers = prompt(questions)
    return answers

def intro_selection():
    name = "intro"
    message = "Please select one for creating your own"
    choices = [
        "insert member",
        "Show Tree structure",
        "Choose Pickle File",
        "Console",
        "Exit",
    ]
    answers = custom_select(name,message,choices)
    return answers['intro']

def get_command() :
    a = input("Family Tree >> ")
    return a

def console(tree):
    while True :
        query_cmd = get_command()
        if query_cmd == "exit" :
            break
        elif "show table" == query_cmd:
            tree.structure(tree)
        elif "show table" in query_cmd:
            parent,generation=decode_command_show_table(query_cmd)
            sub_tree = tree.find_member_by_name_generation_DFS(tree,parent,generation)
            if sub_tree :
                sub_tree.structure(sub_tree)
            else :
                print("Wrong Input")
        else :
            print("Wrong Command")

@tree_command_parser
def decode_command_show_table(query):
    name = query[0][0]
    generation = query[0][1]
    return name,int(generation)

def check_pickle(pkl,pkl_file):
    PATH_TREE = os.getcwd()
    FOLDERNAME = '/pickles/'
    PATH_PAPER = PATH_TREE + FOLDERNAME

    if not os.path.isdir(PATH_PAPER) :
        os.mkdir(PATH_PAPER)

    files=[os.path.basename(x) for x in glob.glob(PATH_PAPER + '*.pkl')]
    # if len(files) == 0 :
    #     print("You dont have existing Trees")
    #     return  None
    # else :
    name = "pickle_list"
    choices = files
    message = "Please select any existing tree"
    choices.append("Add a New Tree")
    answers = custom_select(name,message,choices)
    pkl_file = answers[name]
    print(pkl_file)
    return pkl_file

def create_root_member():
    mamber_input_int,member_input_name = input("Enter the root element ").split(",")
    return mamber_input_int,member_input_name

def insert_member_input():
    parent = input("Enter the name of Parent :- ")
    pos = input("Enter the generation :- ")
    mamber_input_int,member_input_name = input("Enter the member element ").split(",")
    return mamber_input_int,member_input_name,pos,parent

def choose_pickle_file(pkl,pkl_file):
    print(f'Selected Tree : - {pkl_file}')
    while True:
        desc = str(input("Do you want to change the Tree (yes/no) :- "))
        if desc == "yes" :
            check_pkl = check_pickle(pkl,pkl_file)
            return check_pkl
        elif desc == "no" :
            return pkl_file
        else :
            print("Wrong desicion")

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


def login():
    username = input("Enter Username :- ")
    password = input("Enter Password :- ")
    if os.path.exists("pass.txt"):
        key = load_key()
        decrypt("pass.txt",key)
        resp = check_login(username,password)
        encrypt("pass.txt",key)
    else :
        write_key()
        key = load_key()
        resp = start_signup(username,password)
        encrypt("pass.txt",key)
    return resp

def start_signup(username,password):
    cred = str([username,password])
    cred = bytes(cred, 'utf-8')
    hash_object = hashlib.sha256(cred)
    hex_dig = hash_object.hexdigest()
    with open("pass.txt",'w') as file :
        file.write(hex_dig)
    return True

def check_login(username,password):
    cred = str([username,password])
    cred = bytes(cred, 'utf-8')
    hash_object = hashlib.sha256(cred)
    hex_dig = hash_object.hexdigest()
    with open("pass.txt",'r') as file :
        saved_cred = file.read()
    if hex_dig == saved_cred :
        return True
    else :
        return False

@exception
def main() :
    pkl = PickleTree()
    print("This is our Family Tree")
    check_pkl = check_pickle(pkl,pkl_file=None)
    if not check_pkl or check_pkl == "add a new tree":
        print("Add the Tree")
        num,name = create_root_member()
        tree = FamilyTree(num,name)
        pkl_file = str(input("Enter the pickle file name :- "))
        pkl.save_pickle(f'{pkl_file}.pkl',tree)
        tree = pkl.unpickle(f'{pkl_file}.pkl')
    else :
        pkl_file = check_pkl
        tree = pkl.unpickle(pkl_file)
    while True :
        query = intro_selection()
        if query == "exit" :
            sys.exit()
        elif query == "console":
            console(tree)
        elif query == "show tree structure" :
            tree.structure(tree)
        elif query == "choose pickle file" :
            pkl_file = choose_pickle_file(pkl,pkl_file)
            tree = pkl.unpickle(pkl_file)
        elif query == "insert member" :
            try :
                num,name,generation,parent = insert_member_input()
                tree.find_member_by_name_generation_DFS(tree,parent,generation).insert_member(num,name)
                pkl.save_pickle(pkl_file,tree)
                tree = pkl.unpickle(pkl_file)
            except Exception as e:
                print("Parent Not Found!!!")

    # tree = FamilyTree(5,'ANIL')
    # tree.insert_member(2,"Sunil")
    # tree.insert_member(3,'AMAN')
    # tree.insert_member(4,'SHAH')
    # tree.nodes[1].insert_member(19,"MANKU")
    # tree.find_member_DFS(tree,3).insert_member(1,'ABC')
    # tree.find_member_DFS(tree,4).insert_member(0,'DEF')
    # tree.find_member_DFS(tree,0).insert_member(11,'GHI')
    # tree.find_member_DFS(tree,0).insert_member(13,'MNM')
    # tree.find_member_DFS(tree,13).insert_member(15,'LOL')
    # tree.find_member_DFS(tree,4).insert_member(25,'LaL')
    # tree.structure(tree)
    # pkl.save_pickle('sample.pkl',tree)

if __name__ == '__main__':
    if login():
        main()
    else :
        sys.exit()
