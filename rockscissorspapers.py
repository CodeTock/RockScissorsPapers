import random
from urllib.parse import _ParseResultBase
while 1==1: #you can write true ofcourse :D
    choices=["rock","scissors","paper"]
    computer=random.choice(choices)
    player= None
    while player not in choices:
        player=input("please select one object that you have seen... rock,paper,scissors  ==>> ").lower()
    if player==computer:
        print(" player = "+player)
        print(" computer = "+computer)
        print("Tie!")
    elif computer=="rock":
        if player=="scissors":
            print(" player = "+player)
            print(" computer = "+computer)
            print("You lose!")
        if player=="paper":
            print(" player = "+player)
            print(" computer = "+computer)
            print("You win!")    
    elif computer=="scissors":
        if player=="paper":
            print(" player = "+player)
            print(" computer = "+computer)
            print("You lose!")
        if player=="rock":
            print(" player = "+player)
            print(" computer = "+computer)
            print("You win!")                
    elif computer=="paper":
        if player=="rock":
            print(" player = "+player)
            print(" computer = "+computer)
            print("You lose!")
        if player=="scissors":
            print(" player = "+player)
            print(" computer = "+computer)
            print("You win!")
    play_again=None
    while play_again!= "yes" or "no":
        play_again= input("wanna play again???(yes or no)").lower()
        if play_again== "yes":
            break
        elif play_again=="no":
            break
    if play_again=="yes":
        continue
    else:
        break
#yesOrno=["yes","no"]
 #   play_again=None
  #  while play_again not in yesOrno:
   #     play_again=input("wanna play again?(Please ONLY select yes or no)").lower()
        
        
    #if play_again=="yes":
     #   continue
    #else:
     #   break
    
        



    
        


