# Python Quiz Game 
# Tuple of question 
questions=("What is the capital city of Nepal?",
          "Which is the highest mountain in Nepal and the world?",
          "Which river is considered sacred in Nepal?",
          "Which festival in Nepal is known as the 'Festival of Lights'?",
          "What is the national flower of Nepal?",
          "Which famous national park in Nepal is known for Bengal tigers and one-horned rhinoceros?",
          "What year was the current constitution of Nepal adopted?",
          "Which lake is the largest freshwater lake in Nepal?",
          
          "Which UNESCO World Heritage Site is known as the 'City of Devotees'?"
          )
# 2D Tuple for Option 
options=(
         ("A. Pokhara","B. Kathmandu","C. Bhaktapur","D. Lalitpur"),
         ("A. K2","B. Kanchenjunga","C. Mount Everest (Sagarmatha)","D. Annapurna"),
         ("A. Karnali","B. Bagmati","C. Koshi","D. Rapti"),
         ("A. Dashain","B. Tihar","C. Holi","D. Teej"),
         ("A. Rhododendron","B. Lotus","C. Orchid","D. Marigold"),
         ("A. Langtang National Park","B. Sagarmatha National Park","C. Chitwan National Park","D. Shey Phoksundo National Park"),
         ("A. 2006","B. 2015","C. 2008","D. 2012"),
         ("A. Phewa Lake","B. Rara Lake","C. Tilicho Lake","D. Begnas Lake"),
     
         ("A. Patan","B. Kathmandu","C. Bhaktapur","D. Lumbini")
)
# 1D Tuple of answer
answers=("B","C","B","B","A","C","B","B","C")

guesses =[]

score=0

Question_no=0

# displaying question from the tuple as the tuple are iterable 
for question in questions:
    print("--------------------------")
    print(question)
    for option in options[Question_no]:
        print(option)
    print("--------------------------")


    guess=input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[Question_no]:
        score+=1
        print("Correct ✔️")
        print("--------------------------")
    else:
        print("Incorrect ❌")
        print(f"{answers[Question_no]} is the correct answer")
        print("--------------------------")



    Question_no+=1


print("--------------------------")
print("       Result             ")
print("--------------------------")
print(f"You Scored:{score}")
score=int(score/len(questions)*100)
print(f"You give  {score}% Answer are correct")