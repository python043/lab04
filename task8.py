from genericpath import exists
import sys

def rps(c1,c2):
    result =""
    if (c1 == "R" and c2 =="S" ) or(c1=="P" and c2=="R"):
        result="-1"
    if(c1=="R" and c2 =="P") or (c1=="P" and c2 =="S"):
        result="1"
    if(c1=="R" and c2 =="R") or (c1=="P" and c2 =="P") or (c1=="S" and c2 =="S"):
        result="0"
    print("RESULT IS "+result)
def main():
    print("ROCK PAPER SCISSOR GAME")
    print("PLAYER1 SELECT ONE EITHER R, P OR S")
    print("     R:ROCK")
    print("     P:PAPER")
    print("     S:SCISSOR")
    choice1 = input()  # Python 3
    choice1 = choice1.upper()
    print(choice1)
    if choice1 !="R" and choice1 !="S" and choice1 !="P" :
        print("Invalid choice!..")
        exit
    print("PLAYER2 SELECT ONE EITHER R, P OR S")
    print("     R:ROCK")
    print("     P:PAPER")
    print("     S:SCISSOR")
    choice2 = input()  # Python 3
    choice2 = choice2.upper()
    print(choice2)
    if choice2 !="R" and choice2 !="S" and choice2 !="P" :
        print("Invalid choice!..")
        exit
    rps(choice1,choice2)
if __name__ == "__main__":
    main()

