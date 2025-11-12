#liste = [0,2,4]
#print (liste[-1])



#test = []
#for index in range(0,10,2):
    #test.append(f"coucou au n{index}")
 #   print(index)
    
#print(test)


#palindrome = 'kayake'

#if palindrome == palindrome[::-1]:
    
 #   print('Le mot est un palindrome')

#else:

  #  print("Le mot n'est pas un palindrome")

#def is_palindrome(word):
  #  word=word.lower()
 #   return word ==word[::-1]

#print(is_palindrome('Kayak'))



import string

def chiffre_cesar(message,gap):
    alphabet =string.ascii_lowercase
    result = ""



    for char in message:
            if char in alphabet:
                
                
                result += alphabet[(alphabet.index(char) + gap) % len(alphabet)]
            
            else:
               
                raise(TypeError)

    return result




def dechiffre_cesar(message,gap):
    return chiffre_cesar(message,-gap)



def brute_force_cesar(message):
    for decalage in range(1, 26): 
        texte = dechiffre_cesar(message, decalage)
        print(f"Décalage {decalage:2d} : {texte}")



message_code = chiffre_cesar("bonjour", 20)
print(message_code)


message_dechiffre = dechiffre_cesar(message_code, 20)
#print(message_dechiffre)

print("Message chiffré :", message_code)
print("\n--- Brute Force ---")
brute_force_cesar(message_code)



   # for char in message:
        
    #    message_code = (alphabet.index(char) + decalage) % len(string.ascii_lowercase) if char in alphabet else  print("un probleme est survenue"
     #   if char in alphabet:
            
      #      nouvelle_position = (alphabet.index(char) + decalage) % 26
     #   resultat += alphabet[message_code]
        #else:
            
         #   resultat += char

    #return resultat


