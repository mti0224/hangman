import random,time
word_bank = ["able","above","across","add","against","ago","almost","among","animal","answer","become","began","behind","being","better","black","best","body","book","boy","brought","call","cannot","car","certain","change","children","city","close","cold","country","course","cut","dog","done","door","draw","during","early","earth","eat","enough","ever","example","eye","face","family","far","father","feel","feet","fire","fish","five","food","form","four","front","gave","given","got","green","ground","group","grow","half","hand","hard","heard","high","himself","however","idea","important","inside","John","keep","kind","knew","known","land","later","learn","let","letter","life","light","live","living","making","mean","means","money","morning","mother","move","near","night","nothing","once","open","order","page","paper","parts","perhaps","picture","play","point","ready","red","remember","rest","room","run","school","sea","second","seen","sentence","several","short","shown","since","six","slide","sometime","soon","space","states","story","sun","sure","table","though","today","told","took","top","toward","tree","try","turn","united","until","upon","using","usually","white","whole","wind","without","yes","yet","young","situation","massage","character","importance","successful","gradually","yesterday","progress","recognize","disappear","arrangement","relationship","discussion","manufacturing","neighborhood","occasionally","satellites"]
alphabeta = "abcdefghijklmnopqrstuvwxyz"


def doNothing():
    a = 1
for yee in range(0,999**999):
    w = 0
    n = random.randint(0,len(word_bank)-1)
    word = word_bank[n]
    print("這個單字的字數:",len(word))
    correct = "wrong"
    yes = []
    wrong  = []
    time_left = 13
    W_O_R_D = []
    answer = []
    for v in range(0,len(word)):
        answer.append(word[v])
    for i in range(0,len(word)):
        W_O_R_D.append("_")
    print(W_O_R_D)
    while not correct == "correct":
        x = 0
        print("剩餘"+str(time_left)+"次")
        letter = input("猜一個英文字母(請使用小寫)")
        if letter in alphabeta and len(letter) == 1:
            if letter in word:
                print("這個單字含有"+letter)
                if letter in yes:
                    doNothing()
                else:
                    yes.append(letter)
                for k in range(0,len(word)):
                    if letter == answer[k]:
                        del W_O_R_D[k]
                        W_O_R_D.insert(k,letter)
            else:
                print("這個單字沒有"+letter)
                if letter in wrong:
                    doNothing()
                else:
                    wrong.append(letter)
            print("有的:",yes)
            print("沒有的:",wrong)
            time_left -= 1
        else:
            error = random.randint(1000,9999)
            print("錯誤--代碼#"+str(error))
        print()
        print(W_O_R_D)
        if "_" not in W_O_R_D:
            correct = "correct"
        if time_left == 0 or time_left < 0:
            break
    print("\n\n\n")
    if correct == "correct": 
        print("你答對了!!")
    else:
        print("你輸了!!答案是:",word)
    time.sleep(1)
    
    print("\n\n\n\n\n\n\n\n\n")
    



