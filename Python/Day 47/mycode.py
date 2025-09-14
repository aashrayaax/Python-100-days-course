import random
import string

message = input("Enter your message : ")
b = message.split()
print(b)
print(b[1])
a = input("Coding or Decoding?? : ")
if(a=="coding"):
    for word in b:
        if(len(word)<=2):
            rev_word = "".join(reversed(word))
            print(rev_word)
        else:
            first_alpha = word[0]        
            sliced = word[1:]
            last_added = sliced + first_alpha
            length = 3
            characters = string.ascii_letters
            random_string1 = ''.join(random.choices(characters, k=length))
            random_string2 = ''.join(random.choices(characters, k=length))        
            print(f"{random_string1}{last_added}{random_string2}")
            
