def isVowel(c):
    return (c == 'A' or c == 'E' or c == 'I' or
            c == 'O' or c == 'U' or c == 'a' or
            c == 'e' or c == 'i' or c == 'o' or
            c == 'u')
  
  
def pigLatin(s):
  
    # the index of the first vowel is stored.
    length = len(s)
    index = -1
    for i in range(length):
        if (isVowel(s[i])):
            index = i
            break
  
    # Pig Latin is possible only if vowels
    # is present
    if (index == -1):
        file1= open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt","a")
        file1.write("piglatin:"+ "\t"+ s +"\n")
        file1.close()
    # Take all characters after index (including
    # index). Append all characters which are before
    # index. Finally append "ay"
    else:
        cipher=(s[index:] + s[0:index] + "AY").lower()
        file1= open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt","a")
        file1.write("piglatin:"+ "\t"+ cipher +"\t")
        file1.close()
  