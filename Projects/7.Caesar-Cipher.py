logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

cont = True
a = "abcdefghijklmnopqrstuvwxyz"
alphabet = []
for i in a:
    alphabet.append(i)





def ceasar(action,text,shift):
    result = []
    for i in text:
        if i not in alphabet:
            result.append(i)
        else:
            pos1 = alphabet.index(i)
            if action == 'encode':
                pos2 = (pos1 + shift) % 26
            elif action == 'decode':
                pos2 = (pos1 - shift) % 26
            result.append(alphabet[pos2])
    print(f"Your {action}d result is: " +  "".join(result))


while cont == True:
    repeat = False
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt.\n").lower()
    if action != 'encode' and action != 'decode':
        print("You entered an invalid action. Try Again")
        continue
    text = input("Enter your message:\n").lower()
    shift = int(input("Enter the shift number:\n"))
    
    ceasar(action, text, shift)

    while True:

        repeat = input("Type 'Y' to continue or 'N' to close the program.\n").lower()

        if repeat == "y":
            break
        elif repeat == 'n':
            cont = False
            break
        else:
            print("You entered an invalid option.")
            continue