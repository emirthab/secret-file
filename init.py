import os
import encryption as enc


def clear():
    os.system('clear')

header = "\033[92m\
_______________________________________________________________________________\
\n\
\n\
\n\
███████╗███████╗ ██████╗██████╗ ███████╗████████╗    ███████╗██╗██╗     ███████╗\n\
██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝    ██╔════╝██║██║     ██╔════╝\n\
███████╗█████╗  ██║     ██████╔╝█████╗     ██║       █████╗  ██║██║     █████╗  \n\
╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║       ██╔══╝  ██║██║     ██╔══╝  \n\
███████║███████╗╚██████╗██║  ██║███████╗   ██║       ██║     ██║███████╗███████╗\n\
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚══════╝╚══════╝\n\
\n\
Made by \033[94m@emirthab\033[93m                               github.com/emirthab/hidden-file\
\033[92m\
\n\
_______________________________________________________________________________\
\n\033[93m\
\n\
"

menu = "\
|------- MENU -------|\n\n\033[94m\
1.) Encrypt File\n\n\
2.) Decrypt File\n\n\
3.) Help\n\n\
4.) Exit\
\n\n\033[95m\
"

encrypt = "\
|--- Encrypt File ---|\n\n\033[94m\
\033[95m\
"

decrypt = "\
|--- Decrypt File ---|\n\n\033[94m\
\033[95m\
"

fileNotFound = "\
---> File Not Found!\nPress enter to go to the menu... \n\n\033[94m\
\033[95m\
"

def encrypting(filedir):
    clear()
    print(header + encrypt)
    x = input("> Enter File Password : ")
    if x:
        enc.encodeFile(filedir,x)
    else:
        encrypting(filedir)

def decrypting(filedir,typ=0):
    clear()
    print(header + decrypt)
    if typ == 0:
        x = input("> Enter File Password : ")
    elif typ == 1:
        x = input("> Wrong Password Try Again : ")
    if x:
        operation = enc.decodeFile(filedir,x)
        if operation:
            clear()
            print(header + decrypt)
            x = input("> File Decrypted Succesfuly, Press Enter To Go To Menu : ")
        else:
            decrypting(filedir,1)
    else:
        decrypting(filedir,1)

def main():
    clear()
    print(header + menu)
    x = input("> Enter choice : ")
    if x == "1":
        clear()
        print(header + encrypt)
        x = input("> Enter File Path : ")
        if os.path.isfile(x):
            filedir = x
            encrypting(filedir)
        else:
            clear()
            print(header + fileNotFound)
            x = input(">")
            main()
    elif x == "2":
        clear()
        print(header + decrypt)
        x = input("> Enter File Path : ")
        if os.path.isfile(x):
            filedir = x
            decrypting(filedir,0)

main()