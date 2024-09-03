from tkinter import *
import time

def fdC():
    global fdc
    fdc += 1
    if fdc > 2:
        fdc = 0

    if fdc == 0:
        fdbtn['text'] = '한국음식'
        
        f1btn['text'] = kf[0]
        f2btn['text'] = kf[1]
        f3btn['text'] = kf[2]
        f4btn['text'] = kf[3]
        
    elif fdc == 1:
        fdbtn['text'] = '일본음식'

        f1btn['text'] = jf[0]
        f2btn['text'] = jf[1]
        f3btn['text'] = jf[2]
        f4btn['text'] = jf[3]
        
    else:
        fdbtn['text'] = '미국음식'
        
        f1btn['text'] = af[0]
        f2btn['text'] = af[1]
        f3btn['text'] = af[2]
        f4btn['text'] = af[3]
        


def order(text, bay):
    global bap, bac, top
    if fdc == 0:
        if bac.count(text) == 0:
            bac.append(text)
            bap.append(kfc[bay])
            balen.append(1)

            top += kfc[bay]
            orlist.insert(END, text + " : " + str(bap[int(bac.index(text))]) + " : " + str(balen[int(bac.index(text))]))
        else:
            bap[bac.index(text)] += kfc[bay]
            balen[bac.index(text)] += 1

            top += kfc[bay]
            orlist.delete(bac.index(text))
            orlist.insert(bac.index(text), text + " : " + str(bap[int(bac.index(text))]) + " : " + str(balen[int(bac.index(text))]))

        
    if fdc == 1:
        
        if bac.count(text) == 0:
            bac.append(text)
            bap.append(jfc[bay])
            balen.append(1)

            top += jfc[bay]
            orlist.insert(END, text + " : " + str(bap[int(bac.index(text))]) + " : " + str(balen[int(bac.index(text))]))
        else:
            bap[bac.index(text)] += jfc[bay]
            balen[bac.index(text)] += 1

            top += jfc[bay]
            orlist.delete(bac.index(text))
            orlist.insert(bac.index(text), text + " : " + str(bap[int(bac.index(text))]) + " : " + str(balen[int(bac.index(text))]))

    if fdc == 2:
        
        if bac.count(text) == 0:
            bac.append(text)
            bap.append(afc[bay])
            balen.append(1)

            top += afc[bay]
            orlist.insert(END, text + " : " + str(bap[int(bac.index(text))]) + " : " + str(balen[int(bac.index(text))]))
        else:
            bap[bac.index(text)] += afc[bay]
            balen[bac.index(text)] += 1

            top += afc[bay]
            orlist.delete(bac.index(text))
            orlist.insert(bac.index(text), text + " : " + str(bap[int(bac.index(text))]) + " : " + str(balen[int(bac.index(text))]))

    plbl['text'] = "합계 : " + str(top)

def X(event):
    global bap, bac, balen, top

    
    if balen[sum(orlist.curselection())]  <  2:
        if kf.count(bac[sum(orlist.curselection())]) == 1:
  
            top -= kfc[kf.index(bac[sum(orlist.curselection())])]
        elif jf.count(bac[sum(orlist.curselection())]) == 1:

            top -= jfc[jf.index(bac[sum(orlist.curselection())])]
        else:

            top -= afc[af.index(bac[sum(orlist.curselection())])]
            
        bac.remove( bac[sum(orlist.curselection()) ] )
        bap.remove( bap[sum(orlist.curselection())] )
        balen.remove( balen[sum(orlist.curselection())] )
        orlist.delete( sum( orlist.curselection()) )
        
    else:
        if kf.count(bac[sum(orlist.curselection())]) == 1:
            bap[sum(orlist.curselection())] -= kfc[kf.index(bac[sum(orlist.curselection())])]
            top -= kfc[kf.index(bac[sum(orlist.curselection())])]
            
        elif jf.count(bac[sum(orlist.curselection())]) == 1:
            bap[sum(orlist.curselection())] -= jfc[jf.index(bac[sum(orlist.curselection())])]
            top -= jfc[jf.index(bac[sum(orlist.curselection())])]
            
        else:
            bap[sum(orlist.curselection())] -= afc[af.index(bac[sum(orlist.curselection())])]
            top -= afc[af.index(bac[sum(orlist.curselection())])]

        balen[sum(orlist.curselection())] -= 1
        orlist.delete([sum(orlist.curselection())])
        orlist.insert(sum(orlist.curselection()), bac[sum(orlist.curselection())] + " : " + str(bap[sum(orlist.curselection())]) + " : " + str(balen[sum(orlist.curselection())]))
       
    plbl['text'] = "합계 : " + str(top)
        
def bey():
    global bay, top
    bay += 1
    if bay == 1:
        orlbl['text'] = "!확인!"
    if bay == 2:
        time.sleep(1)
        orlbl['text'] = ""
        bay = 0
        orlist.delete(0, END)
        sleep()
        print("-----------------------------------------------------------------")
        for i in range( len( balen)):
            print(bac[i], " : ", bap[i], "원 : ", balen[i], "개")
        print("\n합계 : ", top)
        top = 0
        plbl['text'] = "합계 : "
        restart()

def sleep():
    time.sleep(1)

def restart():
    global bac, bap, balen, fdc

    bac = []
    bap = []
    balen = []

    if fdc == 1:
        fdC()
        fdC()
    if fdc == 2:
        fdC()

win = Tk()

kf = ['짜장면', '떢볶이', '김치찌개', '삼겹살']
kfc = [7150, 4850, 8000, 18000]

jf = ['초밥', '라멘', '소바', '우동']
jfc = [16000, 12000, 4850, 9500]


af = ['햄버거', '핫도그', '치킨', '팝콘']
afc = [3900, 1800, 21000, 4500]


fd = ['짜장면', '떢볶이', '김치찌개', '삼겹살']
fdc = 0

bay = 0

bap = []
bac = []
balen = []
top = 0

f1btn = Button(win, text = fd[0], width = 10, height = 6, bg = "gray", command = lambda : order(f1btn['text'], 0))
f2btn = Button(win, text = fd[1], width = 10, height = 6, bg = "gray", command = lambda : order(f2btn['text'], 1))
f3btn = Button(win, text = fd[2], width = 10, height = 6, bg = "gray", command = lambda : order(f3btn['text'], 2))
f4btn = Button(win, text = fd[3], width = 10, height = 6, bg = "gray", command = lambda : order(f4btn['text'], 3))
orbtn = Button(win, text = "결재", width = 20, height = 4, bg = "skyblue", command = bey)
fdbtn = Button(win, text = "한국음식", width = 20, height = 4, bg = "white", command = fdC)

orlbl = Label(win, text = "", width = 20, height = 4, bg = "white")
ylbl = Label(win, text = "영수증", width = 20, height = 4)
plbl = Label(win, text = "합계 : 0", width = 20, height = 4, bg = "skyblue")

orlist = Listbox(win, width = 20, height = 24)

fdbtn.grid(row = 0, column = 1, columnspan = 2)
f1btn.grid(row = 1, column = 1)
f2btn.grid(row = 1, column = 2)
f3btn.grid(row = 2, column = 1)
f4btn.grid(row = 2, column = 2)
orlbl.grid(row = 4, column = 1, columnspan = 2)
orbtn.grid(row = 6, column = 1, columnspan = 2)
orlist.grid(row = 1, column = 5, rowspan = 5)
ylbl.grid(row = 0, column = 5)
plbl.grid(row = 6, column =  5)

orlist.bind("<Double-Button-1>", X)

win.mainloop()






                
