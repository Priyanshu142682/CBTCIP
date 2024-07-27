a="b"
import random
import sys
from time import sleep,strftime
print("Rock, Paper, Scissors Game")
print("Total 6 rounds in a match")
while a=="b":
    Y=0
    C=0
    l=["Rock","Paper","Scissors"]
    for i in range(1,7):
        choice = random.choice(l)
        print("Round no.",i)
        a=input("Enter Rock or Paper or Scissors:- ")
        print("Your option=",a)
        print("Comp option=",choice)
        sleep(2)
        if a=="Rock" and choice=="Scissors":
            print("You win")
            Y+=1
            print("Comp_score=",C," ","Your_score=",Y)
        elif a=="Rock" and choice=="Paper":
            print("You lost")
            C+=1
            print("Comp_score=",C," ","Your_score=",Y)
        elif a=="Paper" and choice=="Rock":
            print("You win")
            Y+=1
            print("Comp_score=",C," ","Your_score=",Y)
        elif a=="Paper" and choice=="Scissors":
            print("You lost")
            C+=1
            print("Comp_score=",C," ","Your_score=",Y)
        elif a=="Scissors" and choice=="Paper":
            print("You win")
            Y+=1
            print("Comp_score=",C," ","Your_score=",Y)
        elif a=="Scissors" and choice=="Rock":
            print("You lost")
            C+=1
            print("Comp_score=",C," ","Your_score=",Y)
        elif a==choice:
            print("It's a tie")
            print("Comp_score=",C," ","Your_score=",Y)
        i=i+1
    if C>Y:
        print("Final Scorecard is - ")
        print("Comp_score=",C," ","Your_score=",Y)
        sleep(0.4)
        print("YOU LOST THIS MATCH")
    elif C<Y:
        print("Final Scorecard is - ")
        print("Comp_score=",C," ","Your_score=",Y)
        sleep(0.4)
        print("YOU WON THIS MATCH")
    elif C==Y:
        print("Final Scorecard is - ")
        print("Comp_score=",C," ","Your_score=",Y)
        sleep(0.4)
        print("IT'S A DRAW")
    sleep(1)
    a=input("Enter b if you want to play another match or any other key to exit")
    if a !='b':
        print("It will take few seconds to make you exit from the Game")
        sleep(0.4)
        print(".....")
        sleep(2)
        break
print("*****You are now out of the game*****")
sys.exit()
