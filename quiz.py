
#quiz.py
login_col = "#21325E"
title_col = '#3E497A'

BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = '#3E497A'
BTN_COLOR = '#F0F0F0'
EASY_COL = '#39ED63'
HARD_COL = '#F83333'




import csv
from tkinter import *
import random
import tkinter.messagebox as MessageBox
import tkinter as tk
from PIL import ImageTk



#규정 퀴즈 가져오기
with open("eng_quiz_data.csv","r") as file:
    questions = list(csv.reader(file))

multi_choice = random.sample(questions, 4)
answer = random.randint(0,3)
cur_question = multi_choice[answer]

answer = 0



#규정 퀴즈게임 - 쉬움
def quiz_easy():
    #문제 생성
    def next_question():
        global answer

        for i in range(4):
            buttons[i].config(bg=BTN_COLOR)
        
        multi_choice = random.sample(questions, 4)
        answer = random.randint(0,3)
        cur_question = multi_choice[answer][0]

        question_label.config(text = cur_question)

        for i in range(4):
            buttons[i].config(text=multi_choice[i][1])

    #정답 체크
    def check_answer(idx):
        idx = int(idx)
        if answer == idx:
            #버튼 색 변경
            buttons[idx].config(bg=CORRECT_COLOR)

            #정답 맞추면 넘어감
            window.after(1000, next_question)
        else:
            buttons[idx].config(bg=WRONG_COLOR)

    window = tk.Toplevel()
    window.title("영어 퀴즈")
    window.config(padx = 30, pady = 10, bg=BGCOLOR)


    question_label = Label(window, width=20, height=2, text="test", font=("나눔바른펜", 25, "bold"), bg=BGCOLOR, fg="white")
    question_label.pack(pady=30)

    buttons = []
    for i in range(4):
        btn = Button(window, text=f"{i}번", width=35, height=2, font=("나눔바른펜", 15, "bold"), bg=BTN_COLOR, command=lambda idx=i: check_answer(idx))
        btn.pack()
        buttons.append(btn)

    next_btn = Button(window, text="다음 문제", width=15, height=2, command=next_question, font=("나눔바른펜", 15, "bold"), bg=CORRECT_COLOR)
    next_btn.pack(pady=30)



    next_question()




#규정 퀴즈게임 - 보통
def quiz_normal():
    #문제 생성
    def next_question():
        global answer

        for i in range(4):
            buttons[i].config(bg=BTN_COLOR)
        
        multi_choice = random.sample(questions, 4)
        answer = random.randint(0,3)
        cur_question = multi_choice[answer][0]

        question_label.config(text = cur_question)

        for i in range(4):
            buttons[i].config(text=multi_choice[i][1])

    #정답 체크
    def check_answer(idx):
        idx = int(idx)
        if answer == idx:
            #버튼 색 변경
            buttons[idx].config(bg=CORRECT_COLOR)

            #정답 맞추면 넘어감
            window.after(1000, next_question)
        else:
            buttons[idx].config(bg=WRONG_COLOR)

    window = tk.Toplevel()
    window.title("영어 퀴즈")
    window.config(padx = 30, pady = 10, bg=BGCOLOR)


    question_label = Label(window, width=20, height=2, text="test", font=("나눔바른펜", 25, "bold"), bg=BGCOLOR, fg="white")
    question_label.pack(pady=30)

    buttons = []
    for i in range(4):
        btn = Button(window, text=f"{i}번", width=35, height=2, font=("나눔바른펜", 15, "bold"), bg=BTN_COLOR, command=lambda idx=i: check_answer(idx))
        btn.pack()
        buttons.append(btn)

    next_btn = Button(window, text="다음 문제", width=15, height=2, command=next_question, font=("나눔바른펜", 15, "bold"), bg=CORRECT_COLOR)
    next_btn.pack(pady=30)



    next_question()



#규정 퀴즈게임 - 어려움
def quiz_hard():
    #문제 생성
    def next_question():
        global answer

        for i in range(4):
            buttons[i].config(bg=BTN_COLOR)
        
        multi_choice = random.sample(questions, 4)
        answer = random.randint(0,3)
        cur_question = multi_choice[answer][0]

        question_label.config(text = cur_question)

        for i in range(4):
            buttons[i].config(text=multi_choice[i][1])

    #정답 체크
    def check_answer(idx):
        idx = int(idx)
        if answer == idx:
            #버튼 색 변경
            buttons[idx].config(bg=CORRECT_COLOR)

            #정답 맞추면 넘어감
            window.after(1000, next_question)
        else:
            buttons[idx].config(bg=WRONG_COLOR)

    window = tk.Toplevel()
    window.title("영어 퀴즈")
    window.config(padx = 30, pady = 10, bg=BGCOLOR)
    window.resizable(False, False)

    question_label = Label(window, width=20, height=2, text="test", font=("나눔바른펜", 25, "bold"), bg=BGCOLOR, fg="white")
    question_label.pack(pady=30)

    buttons = []
    for i in range(4):
        btn = Button(window, text=f"{i}번", width=35, height=2, font=("나눔바른펜", 15, "bold"), bg=BTN_COLOR, command=lambda idx=i: check_answer(idx))
        btn.pack()
        buttons.append(btn)

    next_btn = Button(window, text="다음 문제", width=15, height=2, command=next_question, font=("나눔바른펜", 15, "bold"), bg=CORRECT_COLOR)
    next_btn.pack(pady=30)



    next_question()

