from flask import Flask, render_template, request

app = Flask(__name__)


#import pandas
#from sklearn import linear_model
#names =  ['Words', 'Toxicity', 'Frequency']
#df = pandas.read_csv("coviddepression.csv")
#X = df[['Toxicity']]
#y = df[['Frequency']]

#regr = linear_model.LinearRegression()
#regr.fit(X,y)

#mentalcheck = regr.predict([[45,56]])
#print(mentalcheck)

#Running through a list

import string
import matplotlib.pyplot as plt
from scipy import stats
import time
counter = 0
sadwords = ["depression", "mental", "pain", "trash", "abysmal", "angry", "negative", "sad", "stressed", "die", "stress", "depressed", "unhealthy", "life", "elephant", "belligerent", "barbed", "cant", "contradictory", "evil", "help", "negativity", "negative", "uhh", "slow", "collapse", "shame", "ashamed", "shamed", "personality", "deprived", "despair", "different", "will", "extrem", "extremist", "terror", "ouch", "foolish", "fear","conquerable", "guilt", "heartbroken", "worthless", "haunt", "give", "unfortunate", "zapped", "zombie", "difidet" "apathetic", "zealot", "wrongful", "wrongly", "wrong", "wripped", "wrinkles", "wrinkly", "zealot", "zapped", "vindictive", "diffident", "vindicitious", "revenge","revengeful", "hacker", "spy", "spying", "nle","died", "loved", "never","apathy","emp","rip","rest","peace","freedom", "mind", "crime", "jail", "parkinsons", "crypto", "bit", "no", "tribe", "freak", "frightened", "dark", "night", "will"]

import time
class time_checker():
    def check_speed(self, word, speed):
        average_speed = word/speed
        return average_speed #returns chars per second
#def main():
print("Tell me some text to first analyze your typing ")
time_check_object = time_checker()
int_time = time.time()
word = len(input())
fin_time = time.time()
tot_time = fin_time - int_time
time_taken = time_check_object.check_speed(word,tot_time)
print(time_taken)
    # DRAwING THE MAP
x = [5,7,8,7,2,17,2,9,4,11,12,9,6,56]
y = [time_taken,time_taken*2,time_taken*3,time_taken*4,time_taken*5,time_taken*6,time_taken*7,time_taken*8,time_taken*9,time_taken*10,time_taken*11,time_taken*12,time_taken*13, time_taken*14]

plt.xlabel('Toxicity of each word that was previously typed?')
plt.ylabel('Typing speed for each word')
plt.title('Toxicity of Word just typed with typing speed')
plt.plot(x, y)
plt.show()
#plt.title("Graph relating toxicity level of words to typing speed")
#slope, intercept, r, p, std_err = stats.linregress(x, y)

#def myfunc(x):
#

texttosearch = input("Tell me some text ")
texttosearch = texttosearch.lower()



newlist = texttosearch.split()
mylist = []

#if len(sadwords) > len(newlist):
for i in range(len(newlist)):
    for x in range(len(sadwords)):
        if newlist[i] == sadwords[x]:
            print("Word found", newlist[i])
            counter = counter + 1
            #mylist = mylist.append[newlist[i]]

            

if counter > 0:
    slope = (((len(texttosearch)/(counter))))
    print(slope)

    if slope < 10 and slope > 0:
        print("You are in danger! Lots of depression symptoms have been found.")
    elif slope <30 and slope >10:
        print("A few depression symptoms have been found. You are in mild danger, and must concentrate on the postitivity of the world and life")
    elif slope <50 and slope >30:
        print("A few depression symptoms have been found. You are in mild danger, and must concentrate on the postitivity of the world and life")
    else:  
        print("You don't have depression")


# Finding frequency
def count_substring(nStr, pattern, data_dict):
    count = 0
    start = 0
    while True:
        a = nStr.find(pattern,start)  # find() returns -1 if the word is not found,
        if a == -1:
            break
        else:
            count += 1
            start = a + 1
    data_dict[pattern] = count
    return data_dict
def main():
    _str = texttosearch
    my_list = ["depression", "mental", "pain", "trash", "abysmal", "angry", "negative", "sad", "stressed", "die", "stress", "depressed", "unhealthy", "life", "elephant", "belligerent", "barbed", "cant", "contradictory", "evil", "help", "negativity", "negative", "uhh", "slow", "collapse", "shame", "ashamed", "shamed", "personality", "deprived", "despair", "different", "will", "extrem", "extremist", "terror", "ouch", "foolish", "fear","conquerable", "guilt", "heartbroken", "worthless", "haunt"]
    counts = {}
    for i in my_list:
        counts = count_substring(_str, i, counts)
    print(counts)
    barx1 = list(counts.keys())
    barx2 = list(counts.values())
    plt.xlabel('Most used negative words')
    plt.ylabel('Frequency of the word in your text')
    plt.title("Bar graph for analyzing frequency of negative words written")

    plt.bar(barx1, barx2)

    plt.xticks(rotation=45)
    plt.show()
main()

## BAR GRAPH 2  Words to frequency




## Bar Graph1
### YOUR CODE GOES BELOW
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
barx = ["depression", "mental", "pain", "trash", "abysmal", "angry", "negative", "sad", "stressed", "die", "stress"]
bary = [99, 34, 4, 34, 23, 46, 67, 78, 45, 34, 23]



plt.xlabel('Programming Languages')
plt.ylabel('Toxicity of Word')
plt.title('Bar graph for analyzing depression.')
plt.bar(barx, bary)

plt.xticks(rotation=45)
plt.show()






    
#for i in range(len(texttosearch)):
#    print(texttosearch[i])



