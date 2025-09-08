import shutil
columns = shutil.get_terminal_size().columns
message = "***Welcome to Kaun Banenga Karodpathi***"
message1 = "Five questions will be asked,4 options will be given,You have to choose the correct answer"
message2 = "For each correct answer we will add 1000 ruppes to your bag"
message3 = "Lets get started!!"
print(message.center(columns))
print(message1.center(columns))
print(message2.center(columns))
print(message3.center(columns))
data = [
    " What does not grow on a tree, according to a popular Hindi saying?  a)Money b)Flowers c)Trees d)Water ",
    " Which country is the largest producer of coffee in the world?  a)Money b)Flowers c)Brazil d)Water ",
    " Who was the first Indian woman to win a medal in the Olympics?  a)Money b)Flowers c)Trees d)Karam Malleswari ",
    " Which city is the capital of Canada?  a)Money b)Ottava c)Trees d)Water ",
    " The Parley between Prime Ministers Zulfikar Ali Bhutto and Indira Gandhi was held at?  a)Money b)Shimla c)Trees d)Water "]
answers = ["Money","Brazil","Karam Malleswari","Ottava","Shimla"]
win = 0
a = input(data[0])
if(a==answers[0]):
    win = win + 1
    print("You won")
else:
    print("You lost")  

a = input(data[1])
if(a==answers[1]):
    win = win + 1
    print("You won")
else:
    print("You lost")      
a = input(data[2])
if(a==answers[2]):
    win = win + 1
    print("You won")
else:
    print("You lost")
a = input(data[3])
if(a==answers[3]):
    win = win + 1
    print("You won")
else:
    print("You lost")
a = input(data[4])
if(a==answers[4]):
    win = win + 1
    print("You won")
else:
    print("You lost")
print("The total correct answers are " , win)
if(win == 0):
    print("Ohhh Bad luck,You couldnot add any money to your bag") 
if(win == 1):
    print("You won 1000")     
if(win == 2):
    print("You won 2000") 
if(win == 3):
    print("You won 3000")     
if(win == 4):
    print("You won 4000")  
if(win == 5):
    print("Congrats buddy,You won the game.Take your 5000 homeeeeeeeeeeeee")     
end = "You have reached the end of the game,Thank You for playing my gameeeeeeeeeeeeeeeeeeeeeeeeeeeeee" 
print(end.center(columns))    




