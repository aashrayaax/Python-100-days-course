import random
import string

message = input("Enter your message : ")
words = message.split()
coded_words = []  # List to store the coded words
decoded_words = [] # List to store the decoded words

choice = input("Coding or Decoding? (c/d) : ").lower()

if choice == "c":
    for word in words:
        if len(word) <= 2:
            rev_word = "".join(reversed(word))
            coded_words.append(rev_word)
        else:
            first_alpha = word[0]
            sliced = word[1:]
            last_added = sliced + first_alpha
            
            length = 3
            characters = string.ascii_letters
            random_string1 = ''.join(random.choices(characters, k=length))
            random_string2 = ''.join(random.choices(characters, k=length))
            
            coded_word = f"{random_string1}{last_added}{random_string2}"
            coded_words.append(coded_word)
            
    print("Coded Message:", " ".join(coded_words))

elif choice == "d":
    for word in words:
        if len(word) <= 2:
            rev_word = "".join(reversed(word))
            decoded_words.append(rev_word)
        else:
            # The word has random strings, so we need to remove them first
            middle_part = word[3:-3]
            
            # The original word had its first letter moved to the end
            last_alpha = middle_part[-1]
            original_word = last_alpha + middle_part[:-1]
            
            decoded_words.append(original_word)

    print("Decoded Message:", " ".join(decoded_words))

else:
    print("Invalid choice. Please enter 'c' for coding or 'd' for decoding.")