login_col = "#21325E"
title_col = '#3E497A'
BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = '#3E497A'
BTN_COLOR = '#F0F0F0'
EASY_COL = '#39ED63'
HARD_COL = '#F83333'
user_col = '#6D6A6A'
column_col = '#323232'


import pymysql
import database   #module database, quiz, mileage
import quiz
import csv
from tkinter import *
import random
import tkinter.messagebox as MessageBox
import tkinter as tk
from PIL import ImageTk


# MySQL DB 연결
conn =pymysql.connect(host="193.123.231.213", user="st02", password="djm06178RE!", database="db_st02")
# Connection 으로부터 Cursor 생성
cur = conn.cursor()
 
# SQL 쿼리 실행
cur.execute("select * from cadets_info")
 
# 데이타 Fetch
rows = cur.fetchall()



cadets_info=[]
for i in range(len(rows)):
    c=[]
    c.append((rows[i])[0])
    c.append((rows[i])[1])
    c.append((rows[i])[2])
    c.append((rows[i])[3])
    c.append((rows[i])[4])
    c.append((rows[i])[5])
    c.append((rows[i])[6])
    b=("금박권 " + str((rows[i])[7]) + "회," + " 상점 2점 " + str((rows[i])[8]) + "회"+ " 제빵소 5천원권 " + str((rows[i])[9]) + "회,"+ " 아침구보 열외권 " + str((rows[i])[10]) + "회")
    c.append(b)
    c.append((rows[i])[-1])
    cadets_info.append(c)

#생도 정보 가져오기

cadets_num=len(cadets_info)


#로그인 성공시 메인 인터페이스
def login():
    p = 0                                   # p = 로그인한 학생의 리스트 순번
    while p <= cadets_num:
        c = cadets_info[p]
        if str(e_id.get()) == str(c[1]) and str(e_password.get()) ==str(c[0]):
            break
        p+=1
        if p == cadets_num:
            break
        
    user_info = cadets_info[p]
    user_id = user_info[1]
    user_name = user_info[3]
    mileage = user_info[6]
    
    programming_info = rows[p]
    f_info = programming_info[7]    #friday
    s_info = programming_info[8]    #twoP
    b_info = programming_info[9]    #voucher
    m_info = programming_info[10]   #morning
    

    #mileage market btn
    def market():
        window = tk.Toplevel(root)
        window.geometry("900x600")
        window.title("규정이")
        window.resizable(False, False)
        
        market_names = Label(window, text = "잔여 마일리지 : " + str(mileage) + " P", font=("나눔바른펜", 21, "bold"))
        market_names.place(x=40, y=50)
        market_names = Label(window, text = "사용자 : " + str(user_id), font=("나눔바른펜", 16, "bold"), fg=user_col)
        market_names.place(x=670, y=30)       
        
        market_names = Label(window, text = "보유 교환권", font=("나눔바른펜", 20, "bold"), fg=title_col)
        market_names.place(x=55, y=123)
        market_names = Label(window, text = "금박권 " + str(f_info) + "회", font=("나눔바른펜", 17, "bold"), fg=column_col)
        market_names.place(x=230, y=125)
        market_names = Label(window, text = "상점 2점 " + str(s_info) + "회", font=("나눔바른펜", 17, "bold"), fg=column_col)
        market_names.place(x=530, y=125)
        market_names = Label(window, text = "제빵소 5천원권 " + str(b_info) + "회", font=("나눔바른펜", 17, "bold"), fg=column_col)
        market_names.place(x=230, y=195)
        market_names = Label(window, text = "아침구보 열외권 " + str(m_info) + "회", font=("나눔바른펜", 17, "bold"), fg=column_col)
        market_names.place(x=530, y=195)
        
        #상품 설명
        global instru_image
        instru_image=tk.PhotoImage(file="instru.png")        
        label=tk.Label(window,image=instru_image)
        label.place(x=55,y=285)   

        #%d = 정수  , %s = 문자열  , %f = 소수점
        def buy_friday():
            sql ="""
            UPDATE cadets_info
            SET
                mileage=%d,
                friday=%d  
            where 
                id=%d
                """                
            cnt = cur.execute(sql % (int(mileage-200), int(f_info+1), int(user_id))) 
            conn.commit()

        def buy_twoP():
            sql ="""
            UPDATE cadets_info
            SET
                mileage=%d,
                twoP=%d  
            where 
                id=%d
                """                
            cnt = cur.execute(sql % (int(mileage-50), int(f_info+1), int(user_id))) 
            conn.commit()


        def buy_voucher():
            sql ="""
            UPDATE cadets_info
            SET
                mileage=%d,
                voucher=%d  
            where 
                id=%d
                """                
            cnt = cur.execute(sql % (int(mileage-100), int(f_info+1), int(user_id))) 
            conn.commit()
 
 
        def buy_morning():
            sql ="""
            UPDATE cadets_info
            SET
                mileage=%d,
                morning=%d  
            where 
                id=%d
                """                
            cnt = cur.execute(sql % (int(mileage-100), int(f_info+1), int(user_id))) 
            conn.commit()

        #purchase button
        purchase_btn = Button(window, text="교환하기", width=5, height=1, font=("나눔바른펜", 14, "bold"),fg="white", bg=login_col, command = buy_friday)
        purchase_btn.place(x=782, y=334)
        purchase_btn = Button(window, text="교환하기", width=5, height=1, font=("나눔바른펜", 14, "bold"),fg="white", bg=login_col, command = buy_twoP)
        purchase_btn.place(x=782, y=390)
        purchase_btn = Button(window, text="교환하기", width=5, height=1, font=("나눔바른펜", 14, "bold"),fg="white", bg=login_col, command = buy_voucher)
        purchase_btn.place(x=782, y=446)
        purchase_btn = Button(window, text="교환하기", width=5, height=1, font=("나눔바른펜", 14, "bold"),fg="white", bg=login_col, command = buy_morning)
        purchase_btn.place(x=782, y=502)



    window = tk.Toplevel(root)
    window.geometry("400x350")
    window.title("규정이")
    window.resizable(False, False)
    
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

    market_btn = Button(window, text="바로가기", width=8, height=1, font=("나눔바른펜", 11, "bold"), bg="white", command = market)
    market_btn.place(x=275, y=168)

    global data_image
    data_image=tk.PhotoImage(file="규정이_라인.png")
    label=tk.Label(window,image=data_image)
    label.place(x=197, y=121)

    global market_image
    market_image=tk.PhotoImage(file="규정이_라인.png")
    label=tk.Label(window,image=market_image)
    label.place(x=197, y=181)



#로그인 버튼 명령어 - 실패
def warn():
    MessageBox.showinfo("알림", "잘못된 로그인 정보입니다.")


#로그인 버튼 명령어
def login_check():
    p = 0
    while p <= cadets_num:
        c = cadets_info[p]
        if str(e_id.get()) == str(c[1]) and str(e_password.get()) ==str(c[0]):
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

# Connection 닫기
conn.close()


    
    
    
    
