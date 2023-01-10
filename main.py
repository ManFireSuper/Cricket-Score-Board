from tkinter import *
from tkinter import ttk
import random as r
import pygame
pygame.mixer.init()
def music_maker():
    pygame.mixer.music.load("Music/mixkit-whill-chake-632.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=3)
music_maker()
class window2:    #  For Team  1
    def creator(self):

        global i ,dic
        dic = {}
        i=0
        win_2=Tk()
        win_2.geometry("370x330")
        win_2.title("Team 1")
        win_2.config(bg="black")
        Label(win_2,text="Registration window for team1",bg="black",fg="light green",font=(10)).pack(pady=5)
        Label(win_2,text="Welcome, this is a window for registering the players of team1.\nAfter registering the players of team1,\nthe team2 registration window will appear.",bg="black",fg="white").pack(pady=5)
        List_1 = Listbox(win_2, bg="black",fg="white")
        List_1.pack(pady=5)
        name_var = StringVar()
        Field_1 = Entry(win_2, textvariable=name_var,bg="black",fg="white").pack()
        def entry_maker():
            global i
            name = name_var.get()
            List_1.insert(0,name)
            dic[i] = name
            print(dic)
            i=i+1
            if(i==3):
                win_2.destroy()
            name_var.set("")
        Button(win_2, text="Add", command=entry_maker,bg="black",fg="white").pack(pady=5)
        mainloop()
class window3:    #  For Team  2

    def creator(self):
        global j, dic_1
        dic_1 = {}
        j=0
        win_3=Tk()
        win_3.geometry("370x330")
        win_3.title("Team 2")
        win_3.config(bg="black")
        Label(win_3, text="Registration window for team2", bg="black", fg="Red", font=(10)).pack(pady=5)
        Label(win_3,
              text="Welcome, this is a window for registering the players of team2.\nAfter registering the players of team2,\nthe main score board window will appear.",
              bg="black", fg="white").pack(pady=5)
        List_1 = Listbox(win_3, bg="black",fg="white")
        List_1.pack(pady=5)
        name_var = StringVar()
        Field_1 = Entry(win_3, textvariable=name_var,bg="black",fg="white").pack()
        def entry_maker():
            global j
            name = name_var.get()
            List_1.insert(0,name)
            dic_1[j] = name
            print(dic_1)
            j = j + 1
            if(j==3):
                win_3.destroy()
            name_var.set("")

        button=Button(win_3, text="Add", command=entry_maker,bg="black",fg="white")
        button.pack(pady=5)
        mainloop()
obj2= window2()
obj2.creator()

obj3= window3()
obj3.creator()
root= Tk()
root.geometry("400x400")
root.config(bg="black")
myy_notebook = ttk.Notebook(root)
myy_notebook.pack(pady=5,padx=5)
my_fram1=Frame(myy_notebook, bg="#ffe4e1")
my_fram1.pack(fill= BOTH)

# For team 1
Label_1 = Label(my_fram1,text="Team 1:", bg="#ffe4e1",fg="blue", font=(10))
Label_1.place(x=20, y=10)
# for team 2
Label_2 = Label(my_fram1, text="Team 2:", bg="#ffe4e1", fg="red", font=(10))
Label_2.place(x=230,y=10)
# for list taem 1
List_3 = Listbox(my_fram1, bg="#d0bab8")
List_3.place(x=20,y=60)
# for list team 2
List_4 = Listbox(my_fram1, bg="#d0bab8")
List_4.place(x=230,y=60)
global dic,dic_1,dic_extra

# For team 1 status tab
def entry_maker_1():
    for k in range(3):

        List_3.insert(0,f"{3-k} ---->>  {dic[k]}")
entry_maker_1()
# for team 2 status tabzz
def entry_maker_2():
    for k in range(3):

        List_4.insert(0,f"{3-k} ---->>  {dic_1[k]}")
entry_maker_2()
# For Toss status
Label_3 = Label(my_fram1, text="Toss:", bg="#d0bab8", fg="black", font=(10)).place(x=160,y=210)


def choice(option):
    if option == "Bat":

        l2 = Label(my_fram1, text=f"Team Chooses {option}.", bg="#d0bab8")
        l2.place(x=200, y=300)
        b2.destroy()
        b3.destroy()
    else:

        l3 = Label(my_fram1, text=f"Team Chooses {option}.", bg="#d0bab8")
        l3.place(x=200, y=300)
        b2.destroy()
        b3.destroy()
name_var = StringVar()
def toss():
    # toss_coin()
    global b2, b3
    extra1 = name_var.get()
    list2 = ["Tail", "Heads"]
    random_no = r.choice(list2)
    if random_no == "Heads":
        l1 = Label(my_fram1, text=f"The toss came to be heads.", bg="#d0bab8")
        l1.place(x=20, y=310)
        sub_btn.destroy()
    else:
        l2 = Label(my_fram1, text=f"The toss came to be tails.", bg="#d0bab8")
        l2.place(x=20, y=310)
        sub_btn.destroy()
    if extra1 == random_no:
        l2 = Label(my_fram1, text=f"{ran} win the toss,\nchoose among these.", bg="#d0bab8")
        l2.place(x=200, y=250)
        b2 = Button(my_fram1, text="Balling", bg="#d0bab8", command=lambda: choice("Ball"))
        b3 = Button(my_fram1, text="Batting", bg="#d0bab8", command=lambda: choice("Bat"))
        b2.place(x=200, y=310)
        b3.place(x=270, y=310)
    else:
        l3 = Label(my_fram1, text=f"{ran} loss the toss,\nother team chooses. ", bg="#d0bab8")
        l3.place(x=200, y=250)
        b2 = Button(my_fram1, text="Balling", bg="#d0bab8", command=lambda: choice("Ball"))
        b3 = Button(my_fram1, text="Batting", bg="#d0bab8", command=lambda: choice("Bat"))
        b2.place(x=200, y=310)
        b3.place(x=270, y=310)
def submit():
    global ran, name_2
    name_2 = name_var.get()
    list = ["team_1", "team_2"]
    ran = r.choice(list)
    global sub_btn
    name_label = Label(my_fram1, text=f"Heads or Tail : {ran}", bg="#d0bab8")
    name_entry = Entry(my_fram1, textvariable=name_var,bg="#d0bab8")
    sub_btn = Button(my_fram1, text='Now toss', bg="#d0bab8", command=toss)
    name_label.place(x=20, y=250)
    name_entry.place(x=20, y=275)
    sub_btn.place(x=20, y=310)
submit()
my_fram2=Frame(myy_notebook, width=400, height=400, bg="#ff4500")
my_fram1.pack(fill="both", expand=1)
my_fram2.pack(fill="both", expand=1)
#### For score
run_team1 = 0
balls_team1 = 12
outcounter = 0
b6 = Label(my_fram2, text="Status:", bg="#f9ca24")
b6.place(x=10, y=10)
run1 = Button(my_fram2, text="+1", bg="#869ed6", command=lambda: sum_team1(1), width=5)
run1.place(x=10, y=40)
run2 = Button(my_fram2, text="+2", bg="#869ed6", command=lambda: sum_team1(2), width=5)
run2.place(x=60, y=40)
run3 = Button(my_fram2, text="+3", bg="#869ed6", command=lambda: sum_team1(3), width=5)
run3.place(x=10, y=70)
run4 = Button(my_fram2, text="Four", bg="#869ed6", command=lambda: sum_team1(4), width=5)
run4.place(x=60, y=70)
run5 = Button(my_fram2, text="Six", bg="#869ed6", command=lambda: sum_team1(6), width=5)
run5.place(x=10, y=130)
run6 = Button(my_fram2, text="Free", bg="#869ed6", command=lambda: sum_team1(7), width=5)
run6.place(x=60, y=130)
out_1 = Button(my_fram2, text="OUT", bg="#869ed6", command=lambda: sum_team1(8), width=5)
out_1.place(x=10, y=160)
def sum_team1(num):
    global run_team1, balls_team1
    if(num == 7):
        run_team1 = run_team1+1
    elif (num == 8):
        global outcounter
        outcounter = outcounter + 1
        balls_team1 = balls_team1 - 1
        if outcounter == 10:
            run1.destroy()
            run2.destroy()
            run3.destroy()
            run4.destroy()
            run5.destroy()
            run6.destroy()
            out_1.destroy()
            run_team2_fun()
        Label(my_fram2, text="Wickets Lost:", bg="#f9ca24").place(x=10, y=250)
        Label(my_fram2, text=outcounter,bg="#869ed6").place(x=100, y=250)
        Label(my_fram2, text=balls_team1,bg="#869ed6").place(x=70, y=220)
        if balls_team1 == 0:
            run1.destroy()
            run2.destroy()
            run3.destroy()
            run4.destroy()
            run5.destroy()
            run6.destroy()
            out_1.destroy()
            run_team2_fun()
        Label(my_fram2, text="Wickets Lost:", bg="#f9ca24").place(x=10, y=250)
        Label(my_fram2, text=outcounter,bg="#869ed6").place(x=100, y=250)
        Label(my_fram2, text=balls_team1,bg="#869ed6").place(x=70, y=220)
    else:
        run_team1 = run_team1+num
        balls_team1 = balls_team1-1
        if balls_team1 == 0:
            run1.destroy()
            run2.destroy()
            run3.destroy()
            run4.destroy()
            run5.destroy()
            run6.destroy()
            out_1.destroy()
            run_team2_fun()
        Label(my_fram2, text="Wickets Lost:", bg="#f9ca24").place(x=10, y=250)
        Label(my_fram2, text=outcounter,bg="#869ed6").place(x=100, y=250)
        Label(my_fram2, text=balls_team1,bg="#869ed6").place(x=70, y=220)
    Label(my_fram2, text="Runs:", bg="#f9ca24").place(x=10, y=190)
    Label(my_fram2, text=run_team1,bg="#869ed6").place(x=60, y=190)
    Label(my_fram2, text="Balls left:", bg="#f9ca24").place(x=10, y=220)
    Label(my_fram2, text=balls_team1, bg="#869ed6").place(x=70, y=220)
run_team2 = 0
balls_team2 = 12
def run_team2_fun():
    global run_1, run_2, run_3, run_4, run_5, run_6, out_2
    b6 = Label(my_fram2, text="Status_2:", bg="#f9ca24")
    b6.place(x=210, y=10)
    run_1 = Button(my_fram2, text="+1", bg="#869ed6", command=lambda: sum_team2(1), width=5)
    run_1.place(x=210, y=40)
    run_2 = Button(my_fram2, text="+2", bg="#869ed6", command=lambda: sum_team2(2), width=5)
    run_2.place(x=260, y=40)
    run_3 = Button(my_fram2, text="+3", bg="#869ed6", command=lambda: sum_team2(3), width=5)
    run_3.place(x=210, y=70)
    run_4 = Button(my_fram2, text="Four", bg="#869ed6", command=lambda: sum_team2(4), width=5)
    run_4.place(x=260, y=70)
    run_5 = Button(my_fram2, text="Six", bg="#869ed6", command=lambda: sum_team2(6), width=5)
    run_5.place(x=210, y=130)
    run_6 = Button(my_fram2, text="Free", bg="#869ed6", command=lambda: sum_team2(7), width=5)
    run_6.place(x=260, y=130)
    out_2 = Button(my_fram2, text="OUT", bg="#869ed6", command=lambda: sum_team2(8), width=5)
    out_2.place(x=210, y=160)
outcounter_1 = 0
def sum_team2(num):
    global run_team2, balls_team2
    if(num == 7):
        run_team2 = run_team2+1
    elif(num == 8):
        global outcounter_1
        outcounter_1 = outcounter_1 + 1
        balls_team2 = balls_team2-1
        if outcounter_1 == 10:
            run_1.destroy()
            run_2.destroy()
            run_3.destroy()
            run_4.destroy()
            run_5.destroy()
            run_6.destroy()
            out_2.destroy()
            check()
        Label(my_fram2, text="Wickets Lost:", bg="#f9ca24").place(x=210, y=250)
        Label(my_fram2, text=outcounter_1, bg="#869ed6").place(x=300, y=250)
        Label(my_fram2, text=balls_team2, bg="#869ed6").place(x=270, y=220)
        if balls_team2 == 0:
            run_1.destroy()
            run_2.destroy()
            run_3.destroy()
            run_4.destroy()
            run_5.destroy()
            run_6.destroy()
            out_2.destroy()
            check()
        Label(my_fram2, text="Wickets Lost:", bg="#f9ca24").place(x=210, y=250)
        Label(my_fram2, text=outcounter_1, bg="#869ed6").place(x=300, y=250)
        Label(my_fram2, text=balls_team2, bg="#869ed6").place(x=270, y=220)
    else:
        run_team2 = run_team2 + num
        balls_team2 = balls_team2 - 1
        if balls_team2 == 0:
            run_1.destroy()
            run_2.destroy()
            run_3.destroy()
            run_4.destroy()
            run_5.destroy()
            run_6.destroy()
            out_2.destroy()
            check()
    Label(my_fram2, text="Runs:", bg="#f9ca24").place(x=210, y=190)
    Label(my_fram2, text=run_team2, bg="#869ed6").place(x=260, y=190)
    Label(my_fram2, text="Balls left:", bg="#f9ca24").place(x=210, y=220)
    Label(my_fram2, text=balls_team2, bg="#869ed6").place(x=270, y=220)
    Label(my_fram2, text="Wickets Lost:", bg="#f9ca24").place(x=210, y=250)
    Label(my_fram2, text=outcounter_1, bg="#869ed6").place(x=300, y=250)
def check():
    if run_team1 > run_team2:
        di = run_team1-run_team2
        Label(my_fram2, text=f" Team_1 is the winner by {di} runs.", bg="#f9ca24",font=(10)).place(
            x=50, y=80)
    elif run_team2 > run_team1:
        di = run_team2-run_team1
        Label(my_fram2, text=f" Team_2 is the winner by {di} runs.", bg="#f9ca24",font=(10)).place(
            x=50, y=80)
    else:
        Label(my_fram2, text=f"Tie", bg="#f9ca24", font=(10)).place(x=150, y=80)
myy_notebook.add(my_fram1, text="Teams")
myy_notebook.add(my_fram2, text="Score Board")
root.title("Cricket Score Board")
root.mainloop()