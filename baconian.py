lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa','F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab','K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
          'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb','U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
  

def encrypt(message):
    cipher = ''
    for letter in message:
        if(letter != ' '):
            cipher += lookup[letter]
        else:
            cipher += ' '
  
    file1= open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt","a")
    file1.write("baconian"+ "\t"+ cipher+"\t")
    file1.close()


def decrypt(message):
    decipher = ''
    i = 0
  
    while True :
        if(i < len(message)-4):
            substr = message[i:i + 5]
            if(substr[0] != ' '):
                decipher += list(lookup.keys())[list(lookup.values()).index(substr)]
                i += 5
  
            else:
                decipher += ' '
                i += 1 
        else:
            break 

    print(decipher)