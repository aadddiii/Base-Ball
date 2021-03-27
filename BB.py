import random

tossListA = ['base','ball']
tossListB = ['batting','balling']

player = False

while player == False:
    tossA = int(input('base(odd) or ball(even)? (enter 0 for odd and 1 for even) '))
    
    if tossA == 0 or tossA == 1:
        tossA1 = tossListA[tossA]
        print('you chose' , tossA1)
        player = True
    else:
        print('please give a valid input')
        player = False

player1 = False    
while player1 == False:

    tossB = int(input('enter number for toss '))
    if tossB > 3:
        print('please enter a nuber between 1 and 3')
        player1 = False
        continue
    else:
        player1 = True

tossC = random.randint(1,3)

tossD = tossB + tossC

tossE = random.randint(0,1)

print('the coputer chose' , tossC)

turnA = None
turnB = None

if tossA1 == 'base':
    if tossD%2 != 0:
            print('you win the toss!')
            playerSelect1 = int(input('do you want to bat or ball? (enter 0 for batting and 1 for balling) '))
            turnA = tossListB[playerSelect1]
            print('okay! the player will now do' , turnA)
    elif tossD%2 == 0:
            print('the computer won the toss')
            turnB = tossListB[tossE]
            print('the computer will now do' , turnB)

elif tossA1 == 'ball':
        if tossD%2 != 0:
            print('the computer won the toss')
            turnB = tossListB[tossE]
            print('the computer will now do' , turnB)
        elif tossD%2 == 0:
            print('you win the toss!')
            playerSelect1 = int(input('do you want to bat or ball? (enter 0 for batting and 1 for balling) '))
            turnA = tossListB[playerSelect1]
            print('okay! the player will now do' , turnA)


if turnA == "batting" or turnB == "balling":
    i = 0
    j = 0
    playerTurn = False
    run = []
    total = 0
    while i <= 2:
        computerBall = random.randint(1,3)       
        while playerTurn == False: 
            playerBat = int(input('please enter a number for batting '))
            if playerBat > 3:
                print('please enter a number between 1 and 3')
                playerTurn = False
                continue
            else:
                playerTurn = True
        print('the computer chose' , computerBall)
        if computerBall == playerBat:
            print('home run!')
            score = playerBat+playerBat
            run.append(score)
            i = 0
            playerTurn = False
            continue
        elif playerBat != computerBall:
            print('Strike!!')
            i = i+1
            score = 0
            playerTurn = False
            continue
    if i >= 3:
        print('you are out')
        playerTurn2 = True        
    for ele in range(0, len(run)): 
        total = total + run[ele] 
    print('your total score is' , total)
    
    i2 = 0
    j2 = 0
    playerTurn2 = False
    run2 = []
    total2 = 0
    while i2 <= 2:
        computerBat = random.randint(1,3)       
        while playerTurn2 == False: 
            playerBall = int(input('please enter a number for balling '))
            if playerBat > 3:
                print('please enter a number between 1 and 3')
                playerTurn2 = False
                continue
            else:
                playerTurn2 = True
        print('the computer chose' , computerBat)
        if computerBat == playerBall:
            print('home run!')
            score2 = computerBat+computerBat
            run2.append(score2)
            i2 = 0
            playerTurn2 = False
            continue
        elif playerBall != computerBat:
            print('Strike!!')
            i2 = i2+1 
            score2 = 0
            playerTurn2 = False
            continue
    if i2 >= 3:
        print('the computer is out')
        playerTurn2 = True
    for ele2 in range(0, len(run2)): 
        total2 = total2 + run2[ele2] 
    print('computers total score is' , score2)

    if total > total2:
        print('the player wins')
               
    elif total < total2:
        print('the computer wins')
        
    elif total == total2:
        print('the match is tie')
        
    
if turnA == "balling" or turnB == "batting":
    i = 0
    j = 0
    playerTurn = False
    run = []
    total = 0
    while i <= 2:
        computerBat = random.randint(1,3)       
        while playerTurn == False: 
            playerBall = int(input('please enter a number for balling '))
            if playerBall > 3:
                print('please enter a number between 1 and 3')
                playerTurn = False
                continue
            else:
                playerTurn = True
        print('the computer chose' , computerBat)
        if computerBat == playerBall:
            print('home run!')
            score = computerBat+computerBat
            run.append(score)
            i = 0
            playerTurn = False
            continue
        elif playerBall != computerBat:
            print('Strike!!')
            i = i+1
            score = 0
            playerTurn = False
            continue
    
    if i >= 3:
        print('you are out')
        playerTurn = True        
    for ele in range(0, len(run)): 
        total = total + run[ele] 
    print('computers total score is' , score)
    
    i2 = 0
    j2 = 0
    playerTurn2 = False
    run2 = []
    total2 = 0
    while i2 <= 2:
        computerBall = random.randint(1,3)       
        while playerTurn2 == False: 
            playerBat = int(input('please enter a number for batting '))
            if playerBat > 3:
                print('please enter a number between 1 and 3')
                playerTurn2 = False
                continue
            else:
                playerTurn2 = True
        print('the computer chose' , computerBall)
        if computerBall == playerBat:
            print('home run!')
            score2 = playerBat+playerBat
            run.append(score2)
            i2 = 4
            continue
        elif playerBat != computerBall:
            print('Strike!!')
            i2 = i2+1 
            score2 = 0
            playerTurn2 = False
            continue
    if i2 >= 3:
        print('you are out')
        playerTurn2 = True        
    for ele in range(0, len(run2)): 
        total2 = total2 + run2[ele2] 
    print('your total score is' , score2)

    if total2 > total:
        print('the player wins')
             
    elif total2 < total:
        print('the computer wins')
       
    elif total == total:
        print('the match is tie')
        
Play_again  = input('do you want to play again? (0 for yes 1 for no) ')
if Play_again == 0:
	player = False
	player1 = False 
	playerTurn = False
	playerTurn2 = False
else:
	pass