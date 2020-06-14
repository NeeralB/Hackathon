from flask import Flask
from flask import render_template
from flask import request
import string

app = Flask(__name__)


def spellchecker(input_text):
    return "outout test"

def gamecheck( theBoard, turn, count):
    msg =""
    GameOver =""
    
    # Now we will check if player X or O has won,for every move after 5 moves. 
    if count >= 5:
        #if theBoard['1'] == theBoard['2'] == theBoard['3']== theBoard['4'] == theBoard['5'] != ' ': # across the top
        if theBoard[1] == theBoard[2] == theBoard[3]!= ' ': # across the top 
            GameOver = 'Y'
            WonPlayer = turn             
            #break
        elif theBoard[4] == theBoard[5] == theBoard[6] != ' ': # across the middle
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[7] == theBoard[8] == theBoard[9] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[1] == theBoard[4] == theBoard[7] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[2] == theBoard[5] == theBoard[8] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
    #Vertical
        elif theBoard[3] == theBoard[6] == theBoard[9] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[1] == theBoard[5] == theBoard[9] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[3] == theBoard[5] == theBoard[7] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        
    if GameOver == 'Y' :
        msg = "Game is over, player " + turn + " won !"
    
    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count == 9:
        GameTie = 'Y'
        msg = " Game has been tied "

    # Now we have to change the player after every move.
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'      
    count = count + 1
     
    return (count, turn, msg )  

@app.route("/", methods=['GET', 'POST'])
def initialgame ():
        theBoard  ={}
        theBoard = {1: ' ' , 2: ' ' , 3: ' ',
                   4: ' ' , 5: ' ' , 6: ' ', 
                  7: ' ' , 8: ' ' , 9: ' '} 
            
        turn = 'X'
        count = 1

        return render_template("GameRoom.html", results=theBoard, turn=turn, count=count, msg="")

@app.route("/play", methods=['GET', 'POST'])

def game():
        
        theBoard  ={}
        req = request.form
        print ( req)
        for i in range (1, 10):

            #txt1 = "'"+ str(i) +"'"
            txt1 = str(i)
            cellvalue = request.form[txt1]
            
            #print ( txt1 ," : " , cellvalue)
            
            if cellvalue == 'X' or cellvalue == 'O' or cellvalue == 'x' or cellvalue == 'o':
                theBoard[i] = cellvalue.upper()
            else :
                theBoard[i] = ' '

        turn = request.form["turn"]
        count = request.form["count"]
 
        (newcount, turn, msg) = gamecheck(theBoard, turn, int(count))

        return render_template("GameRoom.html",
                                results=theBoard, turn=turn, count=newcount, msg=msg)

if __name__ == "__main__":
    app.run(port=5000, debug=True)