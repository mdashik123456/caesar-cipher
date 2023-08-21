from other import *
from os import system
import platform

def clear_display():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

def cipher_text(text, key, choice):
    cipher = ""
    if choice == "decode":
        key *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            
            cipher += alphabet[position + key]
        else:
            cipher += char
    print(f"The {choice}d text is : \"{cipher}\"")
    
clear_display()
    
while True:
    print(logo)
    choice = input("Type 'encode' to encrypt\nType 'decode' to decrypt\n==> ")
    if choice == "encode" or choice == "decode":
        text = input("Type your messege : ")
        key = int(input("Type the key number : "))
        key = key % int((len(alphabet) / 2))
        cipher_text(text, key, choice)
    else:
        print("\nWrong Selection\nYou need to type 'encode' to encrypt or 'decode' to decrypt\n")

    isContinue = input("Do you want to continue? (Y/N) : ")
    clear_display()
    if isContinue == 'n' or isContinue == 'N': break
    
print("\n\n---------------------------------------------------")
print("\nGoodbye\nThanks for using....")
print("---------------------------------------------------")