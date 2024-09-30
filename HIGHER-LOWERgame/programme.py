from random import randint
from art import logo
from art import vs
from data import data
import os
 
score=0
def game():
    print(logo)
    person1=data[randint(0,49)]
    # print(person1)
    print(f"Compare A: {person1["name" ]},{person1["description"]},{person1["country"]}\n")
    global follower_of_A
    follower_of_A=person1["follower_count"]
    print(vs)
    
    person2=data[randint(0,49)]
    # print(person2)
    print(f"Against B: {person2["name" ]},{person2["description"]},{person2["country"]}\n")
    global follower_of_B
    follower_of_B=person2["follower_count"]



    should_end=True

    while  should_end:
        user_answer=input("Who has more followers on instagram. Type 'A' or 'B': ")

        if user_answer=="A":
            if follower_of_A-follower_of_B>0:
                global score # Ek baar check karo ki ae global score nikal kar bhi code kaam kar raaha hh ki nahi
                score+=1
                game()
            else:
                print(f"Oh!, that's wrong. your total score is : {score}")
        elif user_answer=="B":
            if follower_of_B-follower_of_A>0:
                score+=1
                game()
                
            else:
                print(f"Oh!, that's wrong. your total score is : {score}")
        else:
            print("You enter invalid input")
        should_end=False

    
game()

if input("Would you try it again. Type 'Yes' or 'No': ").lower()=="yes":
    os.system('cls' if os.name=="nt" else clear)
    game()
else:
    print("Thank you for visiting......")
 
 
 