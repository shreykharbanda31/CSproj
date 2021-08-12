
import encrypter
import registerlogin
import mysql.connector
from importlib import reload
reload(registerlogin)
from registerlogin import login_window

lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V','F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q','K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
                'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G','U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B','Z' : 'A'}
  
def atbash(message):
    cipher = ''
    for letter in message:
        if(letter != ' '):
            cipher += lookup_table[letter]
        else:
            cipher += ' '
    file1= open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt","a")
    file1.write("atbash"+ "\t"+ cipher.lower()+"\t")
    file1.close()