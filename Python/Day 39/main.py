questions = [
    ["Who is the president of india?" , "Harry" , "modi" ,"farah" , "Gamesh" , "None" , 2],
    ["Which animal is known as the 'King of the Jungle'?", "Tiger", "Lion", "Elephant", "Leopard", "None", 2],
    ["What programming language was created by Guido van Rossum?", "Java", "Python", "C++", "JavaScript", "None", 2],
    ["How many continents are there on Earth?", "5", "6", "7", "8", "None", 3],
    ["Which of these is not a primary color?", "Red", "Blue", "Green", "Yellow", "None", 4],
    ["What is the chemical symbol for Gold?", "Ag", "Au", "Fe", "Cu", "None", 2],
    ["Who painted the Mona Lisa?", "Van Gogh", "Da Vinci", "Picasso", "Michelangelo", "None", 2],
    ["Which planet is closest to the Sun?", "Venus", "Mars", "Mercury", "Earth", "None", 3],
    ["What year did World War II end?", "1943", "1944", "1945", "1946", "None", 3],
    ["Who is known as the father of modern physics?", "Newton", "Einstein", "Galileo", "Hawking", "None", 2],
    ["What is the largest organ in the human body?", "Brain", "Heart", "Liver", "Skin", "None", 4],
    ["Which company created ChatGPT?", "Google", "Microsoft", "OpenAI", "Meta", "None", 3],
    ["What is the speed of light in kilometers per second?", "200,000", "250,000", "300,000", "350,000", "None", 3],
    ["What is the smallest unit of matter?", "Atom", "Molecule", "Quark", "Electron", "None", 3]
]
   
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000]
money = 0
for i in range(0,len(questions)):
    # questions = questions[i]
    print(f"This Question Value is {levels[i]}")
    print(questions[i][0])  # Print just the question text
    print("a)",questions[i][1]   ,"b)",questions[i][2])  # Print options from current question
    print("c)",questions[i][3]   ,"d)",questions[i][4])
    reply = int(input("Give Your Answer (1-5): "))
    if (reply == 0):
        money = levels[i-1]
        break
    if reply == questions[i][6]:  # Compare with current question's answer
        money = levels[i]  # Set money to current level amount
        print("You won" , levels[i] , "in this question")
        # Update to checkpoint amount at checkpoints
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break 
print(f"Your take home money is {money}")    


