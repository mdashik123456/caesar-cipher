from other import logo
from other import alphabet

print(logo)

def cipher_text(text, n, choice):
    cipher = ""
    if choice == "decode":
        n *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            cipher += alphabet[position + n]
        else:
            cipher += char
    if choice != "encode" and choice != "decode":
        print("\nWrong Selection\nYou need to type 'encode' to encrypt or 'decode' to decrypt\n")
        return
    print(f"The {choice}d text is : \"{cipher}\"")

conti = 'y'
while conti == 'y':
    
    choice = input("Type 'encode' to encrypt\nType 'decode' to decrypt\n")
    
    text = input("Type your messege : ")
    n = int(input("Type the shift number : "))
    n = n % int((len(alphabet) / 2))
    cipher_text(text, n, choice)
    
    conti = input("Do you want to continue? (Y/N) : ")
    conti = conti.lower()
print("\nGoodbye\n")