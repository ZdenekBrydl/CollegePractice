#Print the highest number in string input
def maximum(s):
    print(max(s))
    #a= s[0]
    #for i in range(len(s)):
    #    if(a<s[i]):
    #        a= s[i]
    #print(a)

#Print sum of all numbers in string input
def total(s):
    print(sum(s))
    #a= 0
    #for i in range(len(s)):
    #    a+= s[i]
    #print(a)

#Figure out whether number n from input is present in string input
def search(n,s):
    return(n in s)
    #for i in range(len(s)):
    #    if(s[i]==n):
    #        return True
    #return False

#Print input text interlaced by anothe input text
def interleaving(text, filler):
    output= text[0]
    for i in range(len(text)-1):
        output+= filler+text[(i+1)]
    print(output)

#Print encrypted input text using Caesar cipher with right shift of input key
def caesar(text, key):
    for i in range(len(text)):
        print(chr((ord(text[i])+key-ord('a'))%26+ord('a')))

#Print encrypted input text using Vigenère cipher with input text key - i added a choice to encrypt or decrypt
def vigenere(text, key, encrypt= True):
    cipher= ''
    ASCII= []
    for j in range(len(key)):
        ASCII.append((ord(key[j])-ord('a'))%26)
    for i in range(len(text)):
        if(encrypt):
            cipher+= chr((ord(text[i])+ASCII[i%len(key)]-ord('a'))%26+ord('a'))
        else:
            cipher+= chr((ord(text[i])-ASCII[i%len(key)]-ord('a'))%26+ord('a'))
    print(cipher)
        
    

