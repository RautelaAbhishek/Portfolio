#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        


names = []
letter = []
        
        
with open('Mail_merge\Input\\Names\invited_names.txt') as file:
    for line in file:
        for word in line.split():
            names.append(word)


for name in range(len(names)):                
    with open(f'mail_merge\Input\Letters\starting_letter.txt','r') as file:
        letter = file.readlines()
        letter[0] = f'Dear {names[name]}\n'
    
        with open(f'mail_merge\Input\Letters\{names[name]}.txt','w') as file2:
            for item in letter: 
                file2.write(item)