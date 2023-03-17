from zipfile import ZipFile
import time
import os


def crack(zip_file_name, passwords_list):
    for password in passwords_list:
        password = password.rstrip("\n")
        with ZipFile(zip_file_name) as zipfile:
            try:
                zipfile.extractall(pwd = password.encode("utf-8"))
                print(f"\n[+] Password Match @ {password}\n")
                break
                time.sleep(15)
            except:
                print("[-] Password does not Match @ " + password)

def read_file(password_list):
    os.chdir(os.path.dirname(__file__))
    with open(password_list,"r") as obj:
      content =  obj.readlines()
      return content 

def main():
    file_name = input("[+] Enter zip file name: ")
    p_list = ("list.txt")
    passwords = read_file(p_list)

    crack(file_name, passwords)

main()