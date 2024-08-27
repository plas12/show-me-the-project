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
        
    print(fdc)

def order(text):
    orlist.insert(END, text)

def X(event):
    print(orlist.curselection())
    
    orlist.delete( int( orlist.curselection()[0] ) )

def bey():
    global bay
    bay += 1
    if bay == 1:
        orlbl['text'] = "주문?"
    if bay == 2:
        time.sleep(1)
        orlbl['text'] = "주문완료!"
        bay = 0
        orlist.delete(0, END)
        sleep()

def sleep():
    time.sleep(1)
        

win = Tk()

kf = ['짜장면', '떢볶이', '김치찌개', '삼겹살']
jf = ['초밥', '라멘', '소바', '우동']
af = ['햄버거', '핫도그', '치킨', '팝콘']

fd = ['짜장면', '떢볶이', '김치찌개', '삼겹살']
fdc = 0

bay = 0

f1btn = Button(win, text = fd[0], width = 10, height = 6, bg = "gray", command = lambda : order(f1btn['text']))
f2btn = Button(win, text = fd[1], width = 10, height = 6, bg = "gray", command = lambda : order(f2btn['text']))
f3btn = Button(win, text = fd[2], width = 10, height = 6, bg = "gray", command = lambda : order(f3btn['text']))
f4btn = Button(win, text = fd[3], width = 10, height = 6, bg = "gray", command = lambda : order(f4btn['text']))
orbtn = Button(win, text = "결재", width = 20, height = 4, bg = "skyblue", command = bey)
fdbtn = Button(win, text = "한국음식", width = 20, height = 4, bg = "white", command = fdC)

orlbl = Label(win, text = "주문하세요", width = 20, height = 4, bg = "white")
ylbl = Label(win, text = "영수증", width = 10, height = 4)

orlist = Listbox(win, width = 10, height = 24)

fdbtn.grid(row = 0, column = 1, columnspan = 2)
f1btn.grid(row = 1, column = 1)
f2btn.grid(row = 1, column = 2)
f3btn.grid(row = 2, column = 1)
f4btn.grid(row = 2, column = 2)
orlbl.grid(row = 4, column = 1, columnspan = 2)
orbtn.grid(row = 6, column = 1, columnspan = 2)
orlist.grid(row = 1, column = 5, rowspan = 6)
ylbl.grid(row = 0, column = 5)

orlist.bind("<Double-Button-1>", X)

win.mainloop()






                
