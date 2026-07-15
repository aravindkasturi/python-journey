#Caeser Cipher
import logo
logo.logo
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

todo=input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))
if todo=="encode":
    def encrypt():
        encoded=""
        for i in text:
            if i in alphabet:
                x=alphabet.index(i)
                i=alphabet[(x+shift)%26]
                encoded+=i
            else:
                encoded+=i
        print(f"Here's the encoded result: {encoded}")
    encrypt()
elif todo=="decode":
    def decrypt():
        decoded=""
        for i in text:
            if i in alphabet:
                x=alphabet.index(i)
                i=alphabet[(x-shift)%26]
                decoded+=i
            else:
                decoded+=i
        print(f"Here's the decoded result: {decoded}")
    decrypt()
else:
    print("Invalid Input")