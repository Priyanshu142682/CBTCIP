print("!!!MASTERMIND GAME!!!")

a="b"
import sys
from time import sleep,strftime
while a=="b":
    guessOf2=0
    Player1=int(input("Player 1 select a multi-digit number - "))
    print("Now Player2 will guess the number")
    while True:
        GuessPlayer2=int(input("Player 2, Enter your number - "))
        guessOf2+=1 
        if GuessPlayer2==Player1:
            print("Player 2 has guessed the correct number & Now it's time for player 1 to guess the number")
            break
        else:
            digit=0
            Correct=[]
            Player1=str(Player1)
            GuessPlayer2=str(GuessPlayer2)
            for i in GuessPlayer2:
                if i in Player1:
                    digit+=1
                    Correct.append(i)
            print("Not the right number but you did get", digit, "digits correct and those are : ")
            for j in Correct:
                print(j,sep=",")
            Player1=int(Player1)

    guessOf1=0       
    Player2=int(input("Player 2 select a multi-digit number - "))
    print("Now Player1 will guess the number")
    while True:
        GuessPlayer1=int(input("Player 1, enter your number - "))
        guessOf1+=1
        if GuessPlayer1==Player2:
            print("Player 1 has guessed the correct number ")
            break
        else:
            digit2=0
            Correct2=[]
            Player2=str(Player2)
            GuessPlayer1=str(GuessPlayer1)
            for i in GuessPlayer1:
                if i in Player2:
                    digit2+=1
                    Correct2.append(i)
            print("Not the right number but you did get", digit2, "digits correct and those are : ")
            for j in Correct2:
                print(j,sep=",")
            Player2=int(Player2)

    print("Calculating Results")
    for i in range(3):
        sleep(1)
        print(".")
    if (guessOf1>guessOf2):
        print("Player 2 is the MASTERMIND, guessed the number in",guessOf2,"Guesses whereas Player 1 took",guessOf1,"Guesses" )
    elif (guessOf1<guessOf2):
        print("Player 1 is the MASTERMIND, guessed the number in",guessOf1,"Guesses whereas Player 2 took",guessOf2,"guesses")
    else:
        print("Both Player 1 and 2 are the MASTERMINDS, both guessed the number in ",guessOf1,"Guesses")

    a=input("Enter b if you want to play another match or any other key to exit - ")
    if a !='b':
        print("It will take few seconds to make you exit from the Game")
        sleep(0.4)
        print(".....")
        sleep(2)
        break
print("*****You are now out of the game*****")
sys.exit()



                
