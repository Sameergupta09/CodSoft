import random

def games():
    while(True):
        computer=random.choice(['r','p','s'])
        user=input("Enter r for rock,p for paper,s for scissor : ").lower()
    #r>s,s>p,p>r
    
        if (user==computer):
            print("tie")
            
            new=input("Type y to play again or n to exit: ")
            if (new=='y'):
                continue
            else:
                break
        elif (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
            print("you won")
            
            new=input("Type y to play again or n to exit: ")
            if (new=='y'):
                continue
            else:
                break
        elif (computer=='r' and user=='s') or (computer=='s' and user=='p') or (computer=='p' and user=='r'):
            print("you loss")
              
            new=input("Type y to play again or n to exit: ")
            if (new=='y'):
                continue
            else:
                break
        else:
            print("Please enter either r,p,s")
            continue
    
games()  