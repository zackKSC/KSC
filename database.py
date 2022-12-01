import sqlite3
import csv
from tkinter import *
import random
import tkinter.messagebox as MessageBox
import tkinter as tk
from PIL import ImageTk
import tkinter.ttk as ttk

# SQLite DB 연결
conn = sqlite3.connect("/home/pi/mydb2")
 
# Connection 으로부터 Cursor 생성
cur = conn.cursor()
 
# SQL 쿼리 실행
cur.execute("select * from cadets_info")
 
# 데이타 Fetch
rows = cur.fetchall()
for row in rows:
    print(row)
 
# Connection 닫기
conn.close()


#quiz.py
login_col = "#21325E"
title_col = '#3E497A'

BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = '#3E497A'
BTN_COLOR = '#F0F0F0'
EASY_COL = '#39ED63'
HARD_COL = '#F83333'




#규정 퀴즈게임 - 쉬움
def data_inter():
    window = tk.Toplevel()
    window.geometry("800x450")
    window.title("규정이")
    window.resizable(False, False)
    
    Squadron_list=["1중대","2중대","3중대","4중대","5중대","6중대","7중대","8중대"]
    combobox=ttk.Combobox(window)
    combobox.config(width=10, height=1, values=Squadron_list, font=("나눔바른펜", 18), state="readonly")
    combobox.set("Select")
    combobox.pack()
    combobox.place(x=130, y=46)
    
    table_names = Label(window, text = "중대", font=("나눔바른펜", 19, "bold"), fg=title_col)
    table_names.place(x=55, y=45)

    quiz_btn = Button(window, text="조회하기", width=6, height=1, font=("나눔바른펜", 13, "bold"),fg="white", bg=BGCOLOR)
    quiz_btn.place(x=305, y=45)

    lbl = tk.Label(window, text="")
    lbl.pack(pady=50)
    lbl_right_x = tk.Label(window, text="")
    lbl_right_x.pack(side="right", fill="y", padx=23)
    lbl_bottom_y = tk.Label(window, text="")
    lbl_bottom_y.pack(side="bottom", fill="x", pady=10)


    scroll_bar = tk.Scrollbar(window)
    treeview=tk.ttk.Treeview(window, columns=["one", "two","three"], displaycolumns=["one","two","three"], yscrollcommand=scroll_bar.set)
    scroll_bar.pack(side="right", fill="y")
    treeview.pack(side="right",fill="y")


    scroll_bar.config( command = treeview.yview)

    treeview.column("#0", width=180, anchor="center")
    treeview.heading("#0", text="index")

    treeview.column("#1", width=180, anchor="center")
    treeview.heading("one", text="name", anchor="center")

    treeview.column("#2", width=180, anchor="center")
    treeview.heading("two", text="score", anchor="center")

    treeview.column("#3", width=150, anchor="center")
    treeview.heading("three", text="rank", anchor="center")


    treelist=[(7512111, "Tom", 80, 3), (7512112, "Bani", 71, 5), (7512113, "Boni", 90, 2), (7512114, "Dannel", 78, 4), (7512111, "Minho", 93, 1), (7612342, "Minho", 93, 1), (7512110, "Minho", 93, 1), (7512161, "Minho", 93, 1), (7512142, "Minho", 93, 1)]


    for i in range(len(treelist)):
        treeview.insert('', 'end', text=(treelist[i])[0], values=(treelist[i])[1:], iid=str(i)+"번")




