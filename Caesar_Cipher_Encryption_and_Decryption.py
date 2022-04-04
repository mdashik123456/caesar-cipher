from other import logo
from other import alphabet

def cipher_text(text, shift, choice):
    cipher = ""
    if choice == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            cipher += alphabet[position + shift]
        else:
            cipher += char
    print(f"The {choice}d text is : \"{cipher}\"")
    
    
print(logo)
while True:
    choice = input("Type 'encode' to encrypt\nType 'decode' to decrypt\n==> ")
    if choice == "encode" or choice == "decode":
        text = input("Type your messege : ")
        shift = int(input("Type the shift number : "))
        shift = shift % int((len(alphabet) / 2))
        cipher_text(text, shift, choice)
    else:
        print("\nWrong Selection\nYou need to type 'encode' to encrypt or 'decode' to decrypt\n")

    isContinue = input("Do you want to continue? (Y/N) : ")
    if isContinue == 'n' or isContinue == 'N': break
print("\nGoodbye\n")
