print("enter the number of coins")
coinnum=int(input())
x = 0
z = 0
test = 0
while True:
    print("player1 : your turn")
    x=int(input())
    while True :    
        if (x>0 and x<=coinnum and x<=(2*z)):
            break
        elif (x>0 and x < coinnum and test == 0 ) :
            break
        else :
            x=int(input("please enter the coins correctly : "))
    coinnum = coinnum - x
    test = 1 
    print ( " Remaining Coins : " , coinnum )
    if (coinnum == 0):
        print ("player1 wins")
        break
    print ("player2 : your turn")
    z=int(input())
    while True:
        if ( z>0 and z<=(2*x)and z<=coinnum ):
             break
        else:
            z=int(input("please enter the coins correctly : "))
    coinnum = coinnum - z
    print ( " Remaining Coins : " , coinnum )
    if ( coinnum == 0):    
        print ( "player2 wins" )
        break
