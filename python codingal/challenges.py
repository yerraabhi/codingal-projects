#Create a Tic Tac Toe game. You can use different modules and functions to create this game. Make sure that you print the board after every move.

theboard={"7":" ","8":" ","9":" ",
          "4":" ","5":" ","6":" ",
          "1":" ","2":" ","3":" "}

boardkeys=[]

for key in theboard:
    boardkeys.append(key)

def printboard(board):
    print(board["7"]+"|"+board["8"]+"|"+board["9"])
    print("-+-+-")
    print(board["4"]+"|"+board["5"]+"|"+board["6"])
    print("-+-+-")
    print(board["1"]+"|"+board["2"]+"|"+board["3"])

def game():
    turn="X"
    count=0

    for i in range(10):
        printboard(theboard)
        print("It is your turn."+turn+"Move to which place")

        move=input()

        if theboard[move]==" ":
            theboard[move]=turn
            count+=1
        else:
            print("The place  is already filled.\nMove to which place")
            continue

        if count>=5:
            if theboard["7"]==theboard["8"]==theboard["9"] !=" ":
                printboard(theboard)
                print("\nGame Over\n")
                print(("****"+turn+"won ****"))
                break
            elif theboard["4"]==theboard["5"]==theboard["6"] !=" ":
                printboard(theboard)
                print("\nGame Over\n")
                print(("****"+turn+"won ****"))
                break
            elif theboard["1"]==theboard["2"]==theboard["3"] !=" ":
                printboard(theboard)
                print("\nGame Over\n")
                print(("****"+turn+"won ****"))
                break
            elif theboard["7"]==theboard["4"]==theboard["1"] !=" ":
                printboard(theboard)
                print("\nGame Over\n")
                print(("****"+turn+"won ****"))
                break
            elif theboard["8"]==theboard["5"]==theboard["2"] !=" ":
                printboard(theboard)
                print("\nGame Over\n")
                print(("****"+turn+"won ****"))
                break
            elif theboard["9"]==theboard["6"]==theboard["3"] !=" ":
                printboard(theboard)
                print("\nGame Over\n")
                print(("****"+turn+"won ****"))
                break
            elif theboard["7"]==theboard["5"]==theboard["3"] !=" ":
                printboard(theboard)
                print("\nGame Over\n")
                print(("****"+turn+"won ****"))
                break
            elif theboard["9"]==theboard["5"]==theboard["1"] !=" ":
                printboard(theboard)
                print("\nGame Over\n")
                print(("****"+turn+"won ****"))
                break
        if count==9:
            print("\nGame Over")
            print("It is a  tie")
        
        if turn=="X":
            turn="O"
        else:
            turn="X"

    restart=input("Do  you want to play the game again(y/n)")
    if restart=="y" or restart=="Y":
        for key in boardkeys:
            theboard[key]=" "

if __name__=="__main__":
    game()