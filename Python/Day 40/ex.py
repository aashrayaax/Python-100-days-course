import random
import string
word = input("Enter the word : ")
a = input("Hey there.WELCOME.So You want to code or decode? : ")
if(a == "code"):
    if(len(word) <= 2):        
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
elif(a == "decode"):
    if(len(word) <= 2):        
        rev_word = "".join(reversed(word))
        print(rev_word)
    else:
       sliced_word = word[3:-3]
       first_letter = sliced_word[-1]
       remaining_word = sliced_word[:-1]
       decoded_word = first_letter + remaining_word
       print(decoded_word)
       
    

        



