# Create a program capable of displaying questions to the user like KBC. 
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

#SOLUTION

questions = [
    ["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", 2],
    
    ["Who is known as the Father of the Nation in India?", 
     "Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "Subhash Chandra Bose", 1],
    
    ["Which language is used to create web pages?", 
     "Python", "C++", "HTML", "Java", 3],
    
    ["Which planet is known as the Red Planet?", 
     "Earth", "Mars", "Jupiter", "Venus", 2],
    
    ["Who wrote the National Anthem of India?", 
     "Rabindranath Tagore", "Bankim Chandra", "Premchand", "Sarojini Naidu", 1],
    
    ["How many days are there in a leap year?", 
     "365", "366", "364", "367", 2],
    
    ["Which is the largest ocean in the world?", 
     "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", 3],
    
    ["Which gas do plants absorb from the atmosphere?", 
     "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],
    
    ["Who was the first Prime Minister of India?", 
     "Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "Rajendra Prasad", 2],
    
    ["Which is the smallest prime number?", 
     "0", "1", "2", "3", 3],
    
    ["Which device is used to measure temperature?", 
     "Barometer", "Thermometer", "Ammeter", "Voltmeter", 2],
    
    ["How many players are there in a cricket team?", 
     "9", "10", "11", "12", 3],
    
    ["Which is the fastest land animal?", 
     "Lion", "Cheetah", "Tiger", "Horse", 2],
    
    ["Who invented the telephone?", 
     "Thomas Edison", "Alexander Graham Bell", "Newton", "Einstein", 2],
    
    ["Which country is known as the Land of the Rising Sun?", 
     "China", "Japan", "South Korea", "Thailand", 2]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 32000, 640000, 1250000, 2500000,5000000, "1 Crore"]
money = 0
i = 0
for i in range(0, len(questions)):
    question = questions[i]
    # print(questions[0])
    print(f"\nQuestion for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")
    reply = int(input("Enter your answer (1-4) "))
    if(reply == question[-1]):
        print(f"Correct answer, You have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = "1 Crore"
    else:
        print("Wrong answer")
        break

print(f"Your take home money is {money}")