import tkinter as tk
import numpy as np
import os
import sys
import random as rn
import time
import csv

# Directory Path
dir_path = os.path.dirname(os.path.realpath(__file__))

# Background color and font
bg1="#C0C0C0"
bg2="#A9A9A9"
bg3="#7B7B7B"

game_mode = False

# Take height, width and mines variables and close selecting window
def startGame(hgt, wdt, mns):
    global height
    height = int(hgt)
    global width
    width = int(wdt)
    global mines
    mines = int(mns)

    global game_mode
    if (height, width, mines) == (9, 9, 10):
        game_mode = "Beginner"
    elif (height, width, mines) == (16, 16, 40):
        game_mode = "Intermediate"
    elif (height, width, mines) == (16, 30, 99):
        game_mode = "Expert"
    else:
        game_mode = False

    if height > 30 or height < 1:
        sys.exit("Please enter the number of height between 1-30")
    if width > 60 or width < 1:
        sys.exit("Please enter the number of width between 1-60")
    if mines > 360 or mines < 1:
        sys.exit("Please enter the number of mines between 1-360")
    if height*width < mines:
        sys.exit("Please enter the number of mines less than total number of squares")

# Create "Customization Window"
def cstmWin():
    cstm_win = tk.Toplevel()
    cstm_win.resizable(False, False)
    cstm_win.title("")
    icon = tk.PhotoImage(file=dir_path+r"\icons\cstm.ico")
    cstm_win.iconphoto(False, icon)
    cstm_win.configure(bg=bg1)
    frm = tk.Frame(master=cstm_win, relief=tk.RIDGE, borderwidth=10, bg=bg1)


    # Create the spinboxes and labels
    hgt_lbl = tk.Label(master=frm, text="Height:", font=("Small Fonts", 12), bg=bg1)
    hgt_lbl.grid(column=0, row=0, sticky="e")
    hgt_spn = tk.Spinbox(master=frm, from_=1, to=30, width=6, font=("Small Fonts", 10, "bold"))
    hgt_spn.grid(column=1, row=0, padx=5, pady=5, stick="w")

    wdt_lbl = tk.Label(master=frm, text="Width:", font=("Small Fonts", 12), bg=bg1)
    wdt_lbl.grid(column=0, row=1, sticky="e")
    wdt_spn = tk.Spinbox(master=frm, from_=1, to=60, width=6, font=("Small Fonts", 10, "bold"))
    wdt_spn.grid(column=1, row=1, padx=5, pady=5, stick="w")

    mns_lbl = tk.Label(master=frm, text="Mines:", font=("Small Fonts", 12), bg=bg1)
    mns_lbl.grid(column=0, row=2, sticky="e")
    mns_spn = tk.Spinbox(master=frm, from_=1, to=360, width=6, font=("Small Fonts", 10, "bold"))
    mns_spn.grid(column=1, row=2, padx=5, pady=5, stick="w")


    # Create start button
    strt_btn = tk.Button(master=frm, text="START!", font=("Small Fonts", 12), bg=bg1, activebackground=bg1, command=select_win.destroy)
    strt_btn.bind("<ButtonRelease>", lambda x: startGame(hgt_spn.get(), wdt_spn.get(), mns_spn.get()))
    strt_btn.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

    
    frm.columnconfigure([0,1], minsize=80)
    frm.rowconfigure([0,1,2], minsize=30)
    frm.rowconfigure([3], minsize=40)

    frm.pack(padx=5, pady=5)
    cstm_win.mainloop()

# Create "Highscores Window"
def highWin():
    high_win = tk.Toplevel()
    high_win.resizable(False, False)
    high_win.title("High Scores")
    icon = tk.PhotoImage(file=dir_path+r"\icons\high.ico")
    high_win.iconphoto(False, icon)
    high_win.configure(bg=bg1)
    frm = tk.Frame(master=high_win, relief=tk.RIDGE, borderwidth=10, bg=bg1)
    global frm2
    frm1 = tk.Frame(master=frm, bg=bg1)
    frm2 = tk.Frame(master=frm, bg=bg1)
    frm3 = tk.Frame(master=frm, bg=bg1)

    high_ico = tk.PhotoImage(file=dir_path+r"\icons\high.ico")
    
    title = tk.Label(master=frm1, text="High Scores ", image=high_ico, compound=tk.RIGHT, font=("Small Fonts", 18, "bold"), bg=bg1)
    title.pack()

    game_mode = "Beginner"


    def sortHigh(game):
        
        # Clear other scores
        global frm2
        frm2.destroy()
        frm2 = tk.Frame(master=frm, bg=bg1)
        frm2.grid(row=1,column=0,padx=5,pady=0)
        frm2.columnconfigure([1], minsize=180)

        global game_mode
        game_mode=game
        with open(dir_path+r"\highscore.csv", "r") as f:
            tk.Label(master=frm2,text=" Rank", font=("Small Fonts", 12, "bold"), bg=bg1).grid(row=0,column=0)
            tk.Label(master=frm2,text="User", font=("Small Fonts", 12, "bold"), bg=bg1).grid(row=0,column=1,padx=20,sticky="w")
            tk.Label(master=frm2,text="Score", font=("Small Fonts", 12, "bold"), bg=bg1).grid(row=0,column=2)
            next(f)
            high_lst = [each for each in list(csv.reader(f)) if game_mode == each[0]]
            high_lst.sort(key=lambda x: int(x[2]))
            for index, user in enumerate(high_lst): 
                if index < 10:
                    tk.Label(master=frm2,text="#"+str(1+index), font=("Small Fonts", 10, "bold"), bg=bg1).grid(row=1+index,column=0)
                    tk.Label(master=frm2,text=user[1], font=("Small Fonts", 10, "bold"), bg=bg1).grid(row=1+index,column=1,padx=20,sticky="w")
                    tk.Label(master=frm2,text=user[2], font=("Small Fonts", 10, "bold"), bg=bg1).grid(row=1+index,column=2)

    sortHigh(game_mode)    


    h_beg_btn = tk.Button(master=frm3,text="Beginner",width=10,font=("Small Fonts", 10, "bold"), bg=bg1, activebackground=bg1)
    h_beg_btn.grid(row=0,column=0,pady=2)
    h_beg_btn.bind("<ButtonRelease>",lambda x: sortHigh("Beginner"))

    h_int_btn = tk.Button(master=frm3,text="Intermediate",width=10,font=("Small Fonts", 10, "bold"), bg=bg1, activebackground=bg1)
    h_int_btn.grid(row=0,column=1,pady=2,padx=5)
    h_int_btn.bind("<ButtonRelease>",lambda x: sortHigh("Intermediate"))

    h_exp_btn = tk.Button(master=frm3,text="Expert",width=10,font=("Small Fonts", 10, "bold"), bg=bg1, activebackground=bg1)
    h_exp_btn.grid(row=0,column=2,pady=2)
    h_exp_btn.bind("<ButtonRelease>",lambda x: sortHigh("Expert"))

    frm.pack(padx=5,pady=5)
    frm1.grid(row=0,column=0,padx=5,pady=5)
    frm2.grid(row=1,column=0,padx=5,pady=0)
    frm3.grid(row=2,column=0,padx=5,pady=5)
    frm2.columnconfigure([1], minsize=180)

    high_win.mainloop()
    

# Create "Selecting Window"
select_win = tk.Tk()
select_win.title("Minesweeper")
icon = tk.PhotoImage(file=dir_path+r"\icons\mine.ico")
select_win.iconphoto(False, icon)
select_win.resizable(False, False)
select_win.configure(bg=bg1)

# Create internal and external frame
extrnl_frm = tk.Frame(master=select_win, relief=tk.RAISED, borderwidth=5, bg=bg1)
intrnl_frm1 = tk.Frame(master=extrnl_frm, relief=tk.SUNKEN, borderwidth=5, bg=bg2)
intrnl_frm2 = tk.Frame(master=extrnl_frm, relief=tk.SUNKEN, borderwidth=5, bg=bg2)

# Create "Select Difficulty" label
select_lbl = tk.Label(master=intrnl_frm1, text="Select Difficulty", font=('Small Fonts', 30, 'bold') ,bg=bg2)
select_lbl.grid(column = 0, row = 0)
intrnl_frm1.rowconfigure([0], minsize = 50)

# Create difficulty buttons
beg_ico = tk.PhotoImage(file=dir_path+r"\icons\beg.ico")
beg_btn = tk.Button(master=intrnl_frm2, width=140, text="Beginner", image=beg_ico, compound=tk.LEFT, borderwidth=3, font=('Small Fonts', 14), bg=bg1, activebackground=bg1, command=select_win.destroy)
beg_btn.bind("<ButtonRelease>", lambda x: startGame(9,9,10))
beg_btn.grid(column=0, row=0)

int_ico = tk.PhotoImage(file=dir_path+r"\icons\int.ico")
int_btn = tk.Button(master=intrnl_frm2, width=140, text="Intermediate", image=int_ico, compound=tk.LEFT, borderwidth=3, font=('Small Fonts', 14), bg=bg1, activebackground=bg1, command=select_win.destroy)
int_btn.bind("<ButtonRelease>", lambda x: startGame(16,16,40))
int_btn.grid(column=1, row=0)

exp_ico = tk.PhotoImage(file=dir_path+r"\icons\exp.ico")
exp_btn = tk.Button(master=intrnl_frm2, width=140, text="Expert", image=exp_ico, compound=tk.LEFT, borderwidth=3, font=('Small Fonts', 14), bg=bg1, activebackground=bg1, command=select_win.destroy)
exp_btn.bind("<ButtonRelease>", lambda x: startGame(16,30,99))
exp_btn.grid(column=0, row=1)

# Create "Custom Button"
cstm_ico = tk.PhotoImage(file=dir_path+r"\icons\cstm.ico")
cstm_btn = tk.Button(master=intrnl_frm2, width=140, text="Custom", image=cstm_ico, compound=tk.LEFT, borderwidth=3, font=('Small Fonts', 14), bg=bg1, activebackground=bg1, command=cstmWin)
cstm_btn.grid(column=1, row=1)

# Create "Highscore Button"
high_ico = tk.PhotoImage(file=dir_path+r"\icons\high.ico")
high_btn = tk.Button(master=intrnl_frm2, width=140, text="Highscore", image=high_ico, compound=tk.LEFT, borderwidth=3, font=('Small Fonts', 14), bg=bg1, activebackground=bg1, command=highWin)
high_btn.grid(column=0, row=2, columnspan=2)

# Configure the rows and columns
intrnl_frm1.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
intrnl_frm2.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

intrnl_frm1.columnconfigure([0], minsize=350)
intrnl_frm1.rowconfigure([0], minsize=75)

intrnl_frm2.columnconfigure([0,1], minsize=175)
intrnl_frm2.rowconfigure([0,1,2], minsize=70)
extrnl_frm.pack(padx=5, pady=5)

select_win.mainloop()


# Exit the program if height, width and mines are not given
if "height" not in globals():
    sys.exit()
elif "width" not in globals():
    sys.exit()
elif "mines" not in globals():
    sys.exit()

game_over = False

# Detonate all bombs and open "Game Over Window"
def gameOver():
    global game_over
    game_over = True
    global im
    im = tk.PhotoImage(file=dir_path+r"\icons\dead.ico")
    rst_btn['image'] = im
    mine_coor = np.where(Square.matrix == -1)
    for s in range(mine_coor[0].size):
        i, j = mine_coor[0][s], mine_coor[1][s]
        global square_list
        for sqr in square_list:
            if sqr.get_coor() == (i, j):
                sqr.button.grid_remove()
                tk.Label(master=intrnl_frm2, image=mine_ico, compound=tk.CENTER, bg=bg2).grid(row=i,column=j)


# Look for zeros near the clicked square and open them
def lookForZero(i, j, sqr):
    for elm in [(1,0),(-1,0),(0,1),(0,-1)]:
        if i+elm[0] < 0 or j+elm[1] < 0 or i+elm[0] >= height or j+elm[1] >= width:
            continue
        if Square.matrix[i+elm[0]][j+elm[1]] == 0:
            for x in square_list:
                if x.opened:
                    continue
                if x.get_coor() == (i+elm[0],j+elm[1]):
                    opens(i+elm[0],j+elm[1],x)


# Save username and score in highscore.csv
def saveUser(username,save_win):
    with open(dir_path+r"\highscore.csv", "a", newline='') as f:
        writer = csv.writer(f)
        global game_mode
        writer.writerow([game_mode,username,timer_int])
        restart()
        save_win.destroy()

# Save username and exit
def saveUserExit(username,save_win):
    saveUser(username,save_win)
    sys.exit(1)

# Open given square
def opens(i, j, sqr):
    global game_over
    if game_over:
        return False
    if sqr.flg:
        return True
    sqr.button.grid_remove()
    sqr.opened = True
    Square.unopened -= 1
    num = Square.matrix[i][j]
    if num == -1:
        tk.Label(master=intrnl_frm2, image=mine_ico, compound=tk.CENTER, bg="#FF0000").grid(row=i,column=j)
        Square.matrix[i][j] = 0
        gameOver()
        return False
    elif num == 0:
        lookForZero(i, j, sqr)
        for y in range(-1,2):
            for x in range(-1,2):
                for w in square_list:
                    if w.opened:
                        continue
                    if w.get_coor() == (i+y,j+x):
                        opens(i+y,j+x,w)
        tk.Label(master=intrnl_frm2, image=zero_ico, compound=tk.CENTER, bg=bg2).grid(row=i,column=j)
    elif num == 1:
        tk.Label(master=intrnl_frm2, image=one_ico, compound=tk.CENTER, bg=bg2).grid(row=i,column=j)
    elif num == 2:
        tk.Label(master=intrnl_frm2, image=two_ico, compound=tk.CENTER, bg=bg2).grid(row=i,column=j)
    elif num == 3:
        tk.Label(master=intrnl_frm2, image=three_ico, compound=tk.CENTER, bg=bg2).grid(row=i,column=j)
    elif num == 4:
        tk.Label(master=intrnl_frm2, image=four_ico, compound=tk.CENTER, bg=bg2).grid(row=i,column=j)
    elif num == 5:
        tk.Label(master=intrnl_frm2, image=five_ico, compound=tk.CENTER, bg=bg2).grid(row=i,column=j)
    elif num == 6:
        tk.Label(master=intrnl_frm2, image=six_ico, compound=tk.CENTER, bg=bg2).grid(row=i,column=j)
    elif num == 7:
        tk.Label(master=intrnl_frm2, image=seven_ico, compound=tk.CENTER, bg=bg2).grid(row=i,column=j)
    elif num == 8:
        tk.Label(master=intrnl_frm2, image=eight_ico, compound=tk.CENTER, bg=bg2).grid(row=i,column=j)
    
    # I Use won, create "Save Score Window"
    if mines == Square.unopened:
        game_over = True

        global win_ico
        win_ico = tk.PhotoImage(file=dir_path+r"\icons\win.ico")
        rst_btn['image'] = win_ico

        save_win = tk.Toplevel()
        save_win.resizable(False, False)
        save_win.title("You won!")
        icon = tk.PhotoImage(file=dir_path+r"\icons\high.ico")
        save_win.iconphoto(False, icon)
        save_win.configure(bg=bg1)
        save_frm = tk.Frame(master=save_win, relief=tk.RIDGE, borderwidth=10, bg=bg1)
        save_frm.pack(padx=5,pady=5)

        if game_mode:
            tk.Label(master=save_frm,text=f"You finished {game_mode} Mode in {timer_int} seconds!", font=("Small Fonts", 12, "bold"), bg=bg1).grid(row=0,column=0,pady=7,padx=7,columnspan=2)
        else:
            tk.Label(master=save_frm,text=f"You finished Custom Mode in {timer_int} second!", font=("Small Fonts", 12, "bold"),bg=bg1).grid(row=0,column=0,pady=7,padx=7,columnspan=2)

        tk.Label(master=save_frm,text="    Enter username:", font=("Small Fonts", 10, "bold"),bg=bg1).grid(row=1,column=0,pady=5,sticky="e")
        usr_ent = tk.Entry(master=save_frm,font=("Small Fonts", 10))
        usr_ent.bind("<Return>", lambda x: saveUser(usr_ent.get(),save_win))
        usr_ent.grid(row=1,column=1,sticky="w")

        bttm_frm = tk.Frame(master=save_frm, bg=bg1)
        bttm_frm.grid(row=2,column=0,columnspan=2, sticky="nsew")
        restart_btn = tk.Button(master=bttm_frm,text="Save and Restart", font=("Small Fonts", 10, "bold"),bg=bg1,activebackground=bg1,width=15)
        restart_btn.grid(row=0,column=0, pady=10,sticky="n")
        restart_btn.bind("<ButtonRelease-1>", lambda x: saveUser(usr_ent.get(),save_win))

        ext_btn = tk.Button(master=bttm_frm,text="Save and Exit", font=("Small Fonts", 10, "bold"),bg=bg1,activebackground=bg1,width=15)
        ext_btn.grid(row=0,column=1, pady=10,sticky="n")
        ext_btn.bind("<ButtonRelease-1>", lambda x: saveUserExit(usr_ent.get(),save_win))

        bttm_frm.columnconfigure([0,1],weight=1)

        save_win.mainloop()
        return True

# This is a timer
timer_int = 0
def timer():
    if not game_over and not first_click:
        global timer_int
        timer_int += 1
        timer_lbl['text'] = f"{timer_int:03}"
        game_win.after(1000,timer)

# Start the game after first click
first_click = True
def firstClick(i, j):
    global first_click
    if first_click:
        first_click = False
        addMine(mines,i,j)
        addNumber()
        game_win.after(1000,timer)

# Create "Square Object"
class Square:
    matrix = np.zeros((height, width),dtype=np.int8)
    unflagedmines = 0
    unopened = height*width

    def __init__(self, coor, num):
        self.coor = coor
        self.num = num
        self.flg = False
        self.opened = False
        self.button = tk.Button(master=intrnl_frm2, font=("Small Fonts", 2), bg=bg2, activebackground=bg2, borderwidth=3, compound=tk.CENTER)
        self.button.grid(row=self.coor[0], column=self.coor[1], sticky="nsew")
        self.button.bind("<Button-1>", lambda x: firstClick(self.coor[0],self.coor[1]))
        self.button.bind("<ButtonRelease-1>",lambda x: opens(self.coor[0],self.coor[1],self))
        self.button.bind("<Button-3>", lambda x: self.flag(self.coor[0],self.coor[1],self.button))
    def get_coor(self):
        return self.coor
    def get_num(self):
        return self.num

    # Flag given square
    def flag(self, i, j, btn):
        if not self.flg:
            btn['image'] = flag_ico
            self.flg = True
            Square.unflagedmines -= 1
        else:
            btn['image'] = ""
            self.flg = False
            Square.unflagedmines += 1
        mine_counter['text']=f"{Square.unflagedmines:03}"


# Add mines to matrix. -1 represents mine
def addMine(mines, i, j):
    while Square.unflagedmines != mines:
        temp1 = rn.randint(0,height-1)
        temp2 = rn.randint(0,width-1)
        if Square.matrix[temp1][temp2] != -1:
            if (not (temp1 == i or temp1 == i+1 or temp1 == i-1)) or (not (temp2 == j or temp2 == j+1 or temp2 == j-1)):
                Square.matrix[temp1][temp2] = -1
                Square.unflagedmines += 1
    
# Add numbers to matrix
def addNumber():
    for i in range(height):
        for j in range(width):
            if Square.matrix[i][j] == -1:
                continue
            for y in range(-1,2):
                for x in range(-1,2):
                    if i+y < 0 or j+x < 0:
                        continue
                    try:
                        if Square.matrix[i+y][j+x] == -1:
                            Square.matrix[i][j] += 1
                    except:
                        continue

square_list = []

# Add buttons to window
def addButton():
    for i in range(height):
        for j in range(width):
            square_list.append(Square((i,j), Square.matrix[i][j]))
            intrnl_frm2.columnconfigure([j], minsize=21)
        intrnl_frm2.rowconfigure([i], minsize=21)

# Restarts the game
def restart():
    global timer_int
    timer_int = 0
    timer_lbl['text'] = f"{timer_int:03}"
    global game_over
    game_over = False
    global im
    im = tk.PhotoImage(file=dir_path+r"\icons\beg.ico")
    rst_btn['image'] = im
    global square_list
    global first_click
    first_click = True
    for i in range(len(square_list)-1,-1,-1):
        square_list[i].button.grid_remove()
        square_list.pop(i)
    Square.matrix = matrix = np.zeros((height, width),dtype=np.int8)
    Square.unflagedmines = 0
    Square.unopened = height*width
    mine_counter['text']=f"{mines:03}"
    addButton()


# Create "Game Window"
game_win = tk.Tk()
game_win.title("Minesweeper")
icon = tk.PhotoImage(file=dir_path+r"\icons\mine.ico")
game_win.iconphoto(False, icon)
game_win.resizable(False, False)
game_win.configure(bg=bg1)

# Create icon variables
mine_ico = tk.PhotoImage(file=dir_path+r"\icons\mine.ico")
zero_ico = tk.PhotoImage(file=dir_path+r"\icons\0.ico")
one_ico = tk.PhotoImage(file=dir_path+r"\icons\1.ico")
two_ico = tk.PhotoImage(file=dir_path+r"\icons\2.ico")
three_ico = tk.PhotoImage(file=dir_path+r"\icons\3.ico")
four_ico = tk.PhotoImage(file=dir_path+r"\icons\4.ico")
five_ico = tk.PhotoImage(file=dir_path+r"\icons\5.ico")
six_ico = tk.PhotoImage(file=dir_path+r"\icons\6.ico")
seven_ico = tk.PhotoImage(file=dir_path+r"\icons\7.ico")
eight_ico = tk.PhotoImage(file=dir_path+r"\icons\8.ico")
flag_ico = tk.PhotoImage(file=dir_path+r"\icons\flag.ico")

# Create internal and external frame
extrnl_frm = tk.Frame(master=game_win, relief=tk.RAISED, borderwidth=5, bg=bg1)
intrnl_frm1 = tk.Frame(master=extrnl_frm, relief=tk.SUNKEN, borderwidth=5, bg=bg2)
intrnl_frm2 = tk.Frame(master=extrnl_frm, relief=tk.SUNKEN, borderwidth=5, bg=bg3)

# Create top section of window
rst_ico = tk.PhotoImage(file=dir_path+r"\icons\beg.ico")
rst_btn = tk.Button(master=intrnl_frm1, image=rst_ico, compound=tk.CENTER, bg=bg2, activebackground=bg2)
rst_btn.grid(row=0,column=1)
rst_btn.bind("<ButtonRelease-1>", lambda x: restart())


timer_lbl = tk.Label(master=intrnl_frm1, text=f"{timer_int:03}", bg="#202020", fg="#FF0000",font=("Small Fonts", 18, "bold"))
timer_lbl.grid(row=0,column=2,padx=5,pady=5, sticky="we") 
intrnl_frm1.columnconfigure([1], weight=1)

# Counts how many mines are left
mine_counter = tk.Label(master=intrnl_frm1, text=f"{mines:03}", bg="#202020", fg="#FF0000",font=("Small Fonts", 18, "bold"))
mine_counter.grid(row=0,column=0,padx=5,pady=5, sticky="we")
intrnl_frm1.columnconfigure([0,2], minsize=65)

# Create down section of window
addButton()

# Configure frames
extrnl_frm.pack(padx=5, pady=5)
intrnl_frm1.grid(column=0, row=0, padx=4, pady=4, sticky="nsew")
intrnl_frm2.grid(column=0, row=1, padx=4, pady=4, sticky="nsew")


game_win.mainloop()
