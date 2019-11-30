import time, random, easygui
pwa = "python12345678"
f = open("wordbank.txt","r")
word_bank = f.readlines()
f.close()


def print_with(print_out):
    a = ""
    for i in range(0,len(print_out)):
        a = a + str(print_out[i])
    return a

x = random.randint(0,(len(word_bank)-1))
print(word_bank)
print(x)
wordn = word_bank[x]
word = wordn.split("/n")[0]

bonus = random.randint(1,100)
time_left = 10

if bonus > 90:
    have_bonus = 3
    time_left += 3
elif bonus > 70:
    have_bonus = 2
    time_left += 1
else:
    have_bonus = 1
answer = []
show = []
have_letter = []
wrong = []

alphabet = "abcdefghijklmnopqrstuvwxyz"
allow = "no"
while allow != "yes":
    reset = easygui.buttonbox("Reset the scoreboard?", choices = ["yes","no"])
    if reset == "yes":
        pw = easygui.passwordbox("Please enter the password to reset.")
        if pw == pwa:
            g = open("highscore.txt","w")
            g.write(str(0))
            g.close()
            f = open("scoreboard.txt","w")
            for i in range(0,5):
                f.write("(Reset) 0\n")
            f.close()
            easygui.msgbox("Scoreboard has been reset!!")
            allow = "yes"
        else:
            easygui.msgbox("Wrong password, please try again.")
    else:
        allow = "yes"
        
for i in range(0,len(word)-1):
    answer.append(word[i])
    show.append(" _")

easygui.msgbox("Click 'OK' to start the game!!")
if have_bonus == 3:
    easygui.msgbox("LUCKY BONUS!!\nScore Trible!!!\nTimes +3")
elif have_bonus == 2:
    easygui.msgbox("BONUS!!\nScore Double!!\nTimes +1")
start = time.time()
while True:
    if time_left == 0:
        break
    else:
        a = easygui.enterbox("\nGuess wrong time left:" +str(time_left)+"\nWrong letter:"+print_with(wrong)+"\nGuess a letter\n"+print_with(show))
    if a in have_letter:# is "a" allow to game?
        easygui.msgbox("You have already chose letter "+str(a)+" !", image = "!.gif")
    elif a == None:
        easygui.msgbox("You must type something", image = "!.gif")
    elif a not in alphabet:
        easygui.msgbox("This letter might not an English letter!", image = "!.gif")
    elif len(a) != 1:
        easygui.msgbox("Please input a letter, do not empty or more then two!!", image = "!.gif")
    else:# "a" pass all test!!
        have_letter.append(a)
        if a in answer:
            for i in range(len(word)-1):
                if a == answer[i]:
                    show.pop(i)
                    show.insert(i," "+a)
 
        else:
            easygui.msgbox("Letter "+a+" is not the letter in this word!!", image = "X.gif")
            wrong.append(a+", ")
            time_left -= 1

    if " _" not in show:
        break
over = time.time()
final_time = over - start
score = 0
if time_left == 0:
    easygui.msgbox("\nSorry, you didn`t get the word. Answer is:" + word)

else:
    easygui.msgbox("\nYA!! You Win!! Answer is "+ word, image = "congratulations.gif")
    if final_time > 25:
        score = int((10*(time_left)/(final_time/4))*10000/7.5)
    elif final_time > 37.5:
        score = int((10*(time_left)/(final_time/4))*10000/7)
    elif final_time > 50 or time_left <= 5:
        score = int((10*(time_left)/(final_time/4))*10000/6)
    elif final_time > 60 or time_left <= 4 or len(word) >= 8:
        score = int((11*(time_left)/(final_time/4))*10000/5)
    elif final_time > 70 or time_left <= 2 or len(word) >= 10:
        score = int((11*(time_left)/(final_time/4))*10000/4)
    else:
        score = int((11*(time_left)/(final_time/4))*10000/8)

easygui.msgbox("\nUse time: "+"%.2f" % final_time +" sec.\nYour score: "+str(int(score)))

if have_bonus > 1:
    easygui.msgbox("Extra Point: "+str((score * have_bonus) - score)+"\nTotal Score: "+str(score * have_bonus))
f = open("highscore.txt","r")
score = score * have_bonus
high = f.readline()
f.close()
if int(score) > int(high):
    g = open("highscore.txt","w")
    g.write(str(int(score)))
    g.close()
    easygui.msgbox("You are the Highest Score NOW!!", image = "congratulations.gif")
    
      
    
else:
    g = open("highscore.txt","w")
    g.write(str(high))
    g.close()
    g = open("Hiname.txt","r")
    name = g.readline()
    g.close()
    # easygui.msgbox("The Highest Score: "+ str(high)+"\nYou need "+ str(int(high)-int(score)+1)+" more points to over it\nThis Highscore was created by: "+name)
# ===========

f = open("scoreboard.txt","r")
sb_one = f.readlines() #a
f.close()
bbb = []
for i in range(0,len(sb_one)):
    sbItem = sb_one[i]
    sbItem = sbItem.split(" ")
    bbb.append(sbItem)
# bbb = scoreboard_setting_over
Bname = []
Bscore = []
for i in range(0,len(sb_one)):
    Bname.append(bbb[i][0])
    Bscore.append(int(bbb[i][1]))

your_name = easygui.enterbox("What is your name?")
if your_name == "":
    your_name = "(None)"
inRank = "n"
n = 0
while inRank == "n":
    if score < Bscore[len(sb_one)-1]:
        inRank = "notIn"       
    elif score < Bscore[n]:
        n += 1
    elif score > Bscore[n]:
        Bscore.insert(n,score)
        Bname.insert(n,your_name)
        inRank = "y"

        
while len(Bscore) > 5:
    Bscore.pop()
    Bname.pop()
    
writeIn = []
for i in range(0,len(Bscore)):
    writeInString = Bname[i]+" "+str(Bscore[i])+"\n"
    writeIn.append(writeInString)
easygui.msgbox("=====Scoreboard=====\n"+writeIn[0]+writeIn[1]+writeIn[2]+writeIn[3]+writeIn[4])
f = open("scoreboard.txt","w")
f.write(writeIn[0])
f.write(writeIn[1])
f.write(writeIn[2])
f.write(writeIn[3])
f.write(writeIn[4])
f.close()
