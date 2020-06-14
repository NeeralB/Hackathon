from flask import Flask
from flask import render_template
from flask import request
import string

app = Flask(__name__)


def spellchecker(input_text):
    return "outout test"

def gamecheck5( theBoard, turn, count):
    msg =""
    GameOver =""
    
    # Now we will check if player X or O has won,for every move after 5 moves. 
    if count >= 9:
        #if theBoard['1'] == theBoard['2'] == theBoard['3']== theBoard['4'] == theBoard['5'] != ' ': # across the top
        if theBoard[1] == theBoard[2] == theBoard[3]== theBoard[4] == theBoard[5] != ' ': # across the top 
            GameOver = 'Y'
            WonPlayer = turn             
            #break
        elif theBoard[6] == theBoard[7] == theBoard[8]== theBoard[9] == theBoard[10] != ' ': # across the middle
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[11] == theBoard[12] == theBoard[13]== theBoard[14] == theBoard[15] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[16] == theBoard[17] == theBoard[18]== theBoard[19] == theBoard[20] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[21] == theBoard[22] == theBoard[23]== theBoard[24] == theBoard[25] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
    #Vertical
        elif theBoard[1] == theBoard[6] == theBoard[11]== theBoard[16] == theBoard[21] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[2] == theBoard[7] == theBoard[12]== theBoard[17] == theBoard[22] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[3] == theBoard[8] == theBoard[13]== theBoard[18] == theBoard[23] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[4] == theBoard[9] == theBoard[14]== theBoard[19] == theBoard[24] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[5] == theBoard[10] == theBoard[15]== theBoard[20] == theBoard[25] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        #DIAGONAL
        elif theBoard[1] == theBoard[7] == theBoard[13]== theBoard[19] == theBoard[25] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[5] == theBoard[9] == theBoard[13]== theBoard[17] == theBoard[21] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break

    if GameOver == 'Y' :
        msg = "Game is over, player " + turn + " won !"
    
    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count == 25:
        GameTie = 'Y'
        msg = " Game has been tied "

    # Now we have to change the player after every move.
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'      
    count = count + 1
     
    return (count, turn, msg )  

def gamecheck6( theBoard, turn, count):
    msg =""
    GameOver =""
    
    # Now we will check if player X or O has won,for every move after 5 moves. 
    if count >= 11:
        #if theBoard['1'] == theBoard['2'] == theBoard['3']== theBoard['4'] == theBoard['5'] != ' ': # across the top
        if theBoard[1] == theBoard[2] == theBoard[3]== theBoard[4] == theBoard[5] == theBoard[6] != ' ': # across the top 
            GameOver = 'Y'
            WonPlayer = turn             
            #break
        elif theBoard[7] == theBoard[8] == theBoard[9]== theBoard[10] == theBoard[11] == theBoard[12] != ' ': # across the middle
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[13] == theBoard[14] == theBoard[15]== theBoard[16] == theBoard[17] == theBoard[18] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[19] == theBoard[20] == theBoard[21]== theBoard[22] == theBoard[23] == theBoard[24] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[25] == theBoard[26] == theBoard[27]== theBoard[28] == theBoard[29] == theBoard[30] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
    #Vertical
        elif theBoard[31] == theBoard[32] == theBoard[33]== theBoard[34] == theBoard[35] == theBoard[36] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[1] == theBoard[7] == theBoard[13]== theBoard[19] == theBoard[15] == theBoard[31] != ' ':# across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[2] == theBoard[8] == theBoard[14]== theBoard[20] == theBoard[26] == theBoard[32] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[3] == theBoard[9] == theBoard[15]== theBoard[21] == theBoard[27] == theBoard[33] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[4] == theBoard[10] == theBoard[16]== theBoard[22] == theBoard[28] == theBoard[34] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        #DIAGONAL
        elif theBoard[5] == theBoard[11] == theBoard[17]== theBoard[23] == theBoard[29] == theBoard[35] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[6] == theBoard[12] == theBoard[18]== theBoard[24] == theBoard[30] == theBoard[36] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[1] == theBoard[8] == theBoard[15]== theBoard[22] == theBoard[29] == theBoard[36] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break
        elif theBoard[6] == theBoard[11] == theBoard[16]== theBoard[21] == theBoard[26] == theBoard[31] != ' ': # across the bottom
            GameOver = 'Y'
            WonPlayer = turn   
            #break

    if GameOver == 'Y' :
        msg = "Game is over, player " + turn + " won !"
    
    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count == 36:
        GameTie = 'Y'
        msg = " Game has been tied "

    # Now we have to change the player after every move.
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'      
    count = count + 1
     
    return (count, turn, msg )  

@app.route("/tictac", methods=['GET', 'POST'])
def chosesize():
    return render_template("TictactoeSize.html")

@app.route("/size", methods=['GET', 'POST'])
def initialgame ():
        
        size = request.form["sizeT"]
        intSize = int(size)
        theBoard  ={}

        theBoard = {1: ' ' , 2: ' ' , 3: ' ' , 4: ' ' , 5: ' ' ,
                   6: ' ' , 7: ' ' , 8: ' ' , 9: ' ' , 10: ' ' ,
                  11: ' ' , 12: ' ' , 13: ' ' , 14: ' ' , 15: ' ' ,
                 16: ' ' , 17: ' ' , 18: ' ' , 19: ' ' , 20: ' ' ,
                  21: ' ' , 22: ' ' , 23: ' ' , 24: ' ' , 25: ' ' } 
            
        turn = 'X'
        count = 1

        if intSize == 5 :
            tempName = "Tictactoefinal.html"
            theBoard = {1: ' ' , 2: ' ' , 3: ' ' , 4: ' ' , 5: ' ' ,
                   6: ' ' , 7: ' ' , 8: ' ' , 9: ' ' , 10: ' ' ,
                  11: ' ' , 12: ' ' , 13: ' ' , 14: ' ' , 15: ' ' ,
                 16: ' ' , 17: ' ' , 18: ' ' , 19: ' ' , 20: ' ' ,
                  21: ' ' , 22: ' ' , 23: ' ' , 24: ' ' , 25: ' ' } 
            #return render_template("Tictactoefinal.html", results=theBoard, turn=turn, count=count, size=intSize, msg="")
        elif intSize == 6:
            tempName = "6by6.html"
            theBoard = {1: ' ' , 2: ' ' , 3: ' ' , 4: ' ' , 5: ' ' , 6: ' ',
                   7: ' ' , 8: ' ' , 9: ' ' , 10: ' ' , 11: ' ' , 12: ' ',
                  13: ' ' , 14: ' ' , 15: ' ' , 16: ' ' , 17: ' ' , 18: ' ',
                 19: ' ' , 20: ' ' , 21: ' ' , 22: ' ' , 23: ' ' , 24: ' ',
                 25: ' ' , 26: ' ' , 27: ' ' , 28: ' ' , 29: ' ' , 30: ' ',
                  31: ' ' , 32: ' ' , 33: ' ' , 34: ' ' , 35: ' ', 36: ' ' } 
            #return render_template("Tictactoefinal.html", results=theBoard, turn=turn, count=count, size=intSize, msg="")
        else :
            tempName = "Tictactoefinal.html"

        return render_template(tempName, results=theBoard, turn=turn, count=count, sizeT=intSize, msg="")

@app.route("/size/play5", methods=['GET', 'POST'])
def game5():
        
        theBoard  ={}
        req = request.form
        print ( req)
        for i in range (1, 26):

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
 
        (newcount, turn, msg) = gamecheck5(theBoard, turn, int(count))

        return render_template("Tictactoefinal.html",
                                results=theBoard, turn=turn, count=newcount, msg=msg)


@app.route("/size/play6", methods=['GET', 'POST'])
def game6():
        
        theBoard  ={}
        req = request.form
        print ( req)
        for i in range (1, 37):

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
 
        (newcount, turn, msg) = gamecheck6(theBoard, turn, int(count))

        return render_template("6by6.html",
                                results=theBoard, turn=turn, count=newcount, msg=msg)

if __name__ == "__main__":
    app.run(port=5000, debug=True)