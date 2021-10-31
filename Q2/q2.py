import random

def findNimSum(n1, n2):

    nim_sum = n1^n2
    nim_sum = bin(nim_sum)[2:]
    # print("NimSum = "+str(nim_sum))
    return nim_sum
    
def chooseMove(n1, n2):
    # for two piles, making a move so that the piles have equal no. of stones is enough to make the nimsum 0
    if n1 == n2:
        #nimsum = 0, make a random move
        p = random.choice([1,2])
        if p == 1:
            s = random.choice(list(range(1,n1+1)))
            # n1 = n1 - s
        elif p == 2:
            s = random.choice(list(range(1,n2+1)))
            # n2 = n2 - s
    elif n1>n2:
        p = 1
        s = n1-n2
    else:
        p = 2
        s = n2-n1
    
    return [p,s]

def main():
    print("\nMinimax Algorithm game\n-----------------------")
    n1 = int(input("Enter number of stones in pile 1: "))
    n2 = int(input("Enter number of stones in pile 2: "))

    # if int(findNimSum(n1,n2)) == 0:
    #     print("Computer wins!")
    # else:
    #     print("Player wins!")
    
    userTurn = True
    while (True):

        if userTurn == True:
            print("\n-----------PLAYER'S TURN:-----------")
            p,s = input("Pile, No. of stones : ").split()
            p = int(p)
            s = int(s)

            if((p != 1 and p != 2) or (p==1 and s>n1) or (p==2 and s>n2)):
                print("Invalid numbers. Enter again.")
                continue
            elif p==1:
                n1=n1-s
            else:
                n2=n2-s

            userTurn = False
            print("\n\t\tPILE 1 : "+str(n1)+"   ::   PILE 2 : "+str(n2))
            if(n1==0 and n2==0):
                print("PLAYER WINS!!")
                exit()
        
        elif userTurn == False:
            print("\n-----------COMPUTER'S TURN:-----------")            
            [p,s] = chooseMove(n1, n2)
            print("Pile, No. of stones : "+str(p)+" "+str(s))
            if p==1:
                n1 = n1 - s
            elif p==2:
                n2=n2-s
            print("\n\t\tPILE 1 : "+str(n1)+"   ::   PILE 2 : "+str(n2))
            if(n1==0 and n2==0):
                print("\nCOMPUTER WINS!!")
                exit()
            userTurn = True


if __name__ == "__main__":
    main()