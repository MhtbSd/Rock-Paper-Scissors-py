

from random import randint 
from os import system
from datetime import datetime


user_score = 0
pc_score = 0
count = 1
start_time = datetime.now()


while user_score!=3 and pc_score!= 3 :
    user_input = int(input("\n\n1)Rack 2)Paper 3)Scissors : "))
    pc_input = randint(1,3)

    system("cls")


    #region Show Info
    if user_input==1 :
        print("user : Rack", end="-")
        
    elif user_input==2 :
        print("user : Paper", end="-")

    else :
        print("user : Scissors", end="-")


    if pc_input==1 :
        print("pc : Rack")

    elif pc_input==2 :
        print("pc : Paper")

    else :
        print("pc : Scissors")
    #endregion

    #region Check Score
    if (user_input==1 and pc_input==3) or (user_input==2 and pc_input==1) or (user_input==3 and pc_input==2) :
        user_score += 1

    elif (pc_input==1 and user_input==3) or (pc_input==2 and user_input==1) or (pc_input==3 and user_input==2) :
        pc_score += 1
        #endregion


    print("User Score : ", user_score, " - Pc Score : ", pc_score)

    count += 1
    print("cont : ", count)
    
    finish_time = datetime.now()
    print(finish_time - start_time)


if user_score==3 :
    print("Horaaa")

if pc_score==3 :
    print(":(")
