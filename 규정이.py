login_col = "#21325E"
title_col = '#3E497A'

BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = '#3E497A'
BTN_COLOR = '#F0F0F0'
EASY_COL = '#39ED63'
HARD_COL = '#F83333'

import database
import quiz
import csv
from tkinter import *
import random
import tkinter.messagebox as MessageBox
import tkinter as tk
from PIL import ImageTk



#생도 정보 가져오기
with open("cadet_info.csv","r", encoding="UTF-8-sig") as file:
    cadets_info = list(csv.reader(file))
    
cadets_num=len(cadets_info)

#로그인 성공시 메인 인터페이스
def login():
    p = 0                                   # p = 로그인한 학생의 리스트 순번
    while p <= cadets_num:
        c = cadets_info[p]
        if str(e_id.get()) == str(c[0]) and str(e_password.get()) ==str(c[1]):
            break
        p+=1
        if p == cadets_num:
            break

    user_info = cadets_info[p]
    user_name = user_info[2]
    mileage = user_info[3]

    
    window = tk.Toplevel(root)
    window.geometry("400x350")
    window.title("규정이")

    table_names = Label(window, text = "퀴즈", font=("나눔바른펜", 16, "bold"), fg=title_col)
    table_names.place(x=30, y=50)
    table_names = Label(window, text = "데이터베이스", font=("나눔바른펜", 16, "bold"), fg=title_col)
    table_names.place(x=30, y=110)
    table_names = Label(window, text = "마일리지 마켓", font=("나눔바른펜", 16, "bold"), fg=title_col)
    table_names.place(x=30, y=170)
    table_names = Label(window, text = str(user_name) + "님의 잔여 마일리지 : " + str(mileage) + " P", font=("나눔바른펜", 17, "bold"))
    table_names.place(x=25, y=245)


    quiz_btn = Button(window, text="어려움", width=5, height=1, font=("나눔바른펜", 11, "bold"),fg="white", bg=HARD_COL, command = quiz.quiz_easy)
    quiz_btn.place(x=120, y=48)
    quiz_btn = Button(window, text="보 통", width=5, height=1, font=("나눔바른펜", 11, "bold"),fg="white", bg=login_col)
    quiz_btn.place(x=205, y=48)
    quiz_btn = Button(window, text="쉬 움", width=5, height=1, font=("나눔바른펜", 11, "bold"),fg="white", bg=EASY_COL)
    quiz_btn.place(x=290, y=48)

    database_btn = Button(window, text="바로가기", width=8, height=1, font=("나눔바른펜", 11, "bold"), bg="white", command = database.data_inter)
    database_btn.place(x=275, y=108)

    market_btn = Button(window, text="바로가기", width=8, height=1, font=("나눔바른펜", 11, "bold"), bg="white")
    market_btn.place(x=275, y=168)

    data_image=tk.PhotoImage(file="규정이_라인.png")
    label=tk.Label(window,image=data_image)
    label.place(x=190, y=117)

    market_image=tk.PhotoImage(file="규정이_라인.png")
    label=tk.Label(window,image=market_image)
    label.place(x=190, y=177)





#로그인 버튼 명령어 - 실패
def warn():
    MessageBox.showinfo("알림", "잘못된 로그인 정보입니다.")

#로그인 버튼 명령어
def login_check():
    p = 0
    while p <= cadets_num:
        c = cadets_info[p]
        if str(e_id.get()) == str(c[0]) and str(e_password.get()) ==str(c[1]):
            login()
            break
        p+=1
        if p == cadets_num:
            warn()
            break
        

#로그인 창
root = tk.Tk()
root.geometry("330x300")
root.title("규정이")
root.resizable(False, False)


table_names = Label(root, text = "규정이", font=("나눔바른펜", 15, "bold"), fg=title_col)
table_names.place(x=135, y=200)

image=tk.PhotoImage(file="규정이.png")
label=tk.Label(root,image=image)
label.place(x=117, y=22)

table_names = Label(root, text = "교 번", font=("나눔바른펜", 10, "bold"))
table_names.place(x=45, y=240)
table_names = Label(root, text = "비밀번호", font=("나눔바른펜", 10, "bold"))
table_names.place(x=35, y=265)

e_id = Entry(root)
e_id.place(width=120, height=20, x=105, y=240)
e_password = Entry(root)
e_password.place(width=120, height=20, x=105, y=265)

login_btn = Button(text="로그인", width=5, height=2, font=("나눔바른펜", 10, "bold"),fg="white", bg=login_col, command = login_check)
login_btn.place(x=245, y=240)

root.mainloop()




    
    
    