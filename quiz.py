from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
Score=0
root = Tk()
root.geometry("700x700")
def destroying():
    dest = Tk()
    dest.geometry("400x400")
    dest.destroy()
    exit()
    dest.mainloop()
def closes():
    window = Tk()
    window.geometry("200x100")
    window.title("Leave Site")
    label = Label(window, text = "You will not able to play")
    label.pack()
    button2 = Button(window , text = "OK", command = destroying)
    button2.pack()
    window.mainloop()
def right():
    global Score
    messagebox.showinfo("showinfo","Answer is correct")
    Score = Score + 1
def submission():
    global Score
    messagebox.showinfo("showinfo", "Score is : " + str(Score))
def wrong():
    messagebox.showinfo("showinfo","Answer is wrong")
def getval():
    quiz = Tk()
    quiz.geometry("800x800")
    quiz.title("Quiz Begins")
    label2=Label(quiz ,font = "10" , text ='''Q1. What is a correct syntax to output "Hello World" in Python?''')
    label2.place(x=0,y=0)
    button2 = Button(quiz, text = '''A. p("Hello World")''', command = wrong)
    button2.place(x=0,y=25)
    button3= Button(quiz, text = '''B. print("Hello World")''',command= right )
    button3.place(x=0,y=50)
    button4 = Button(quiz, text = '''C. echo("Hello World")''', command = wrong)
    button4.place(x=0,y=75)
    label3=Label(quiz, font = "10" , text ='''Q2. What is the output for \n S = [['him', 'sell'], [90, 28, 43]] \n S[0][1][1]''')
    label3.place(x=0,y=115)
    button5=Button(quiz, text = "A. 'e'", command = right)
    button5.place(x=0,y=175)
    button6=Button(quiz,text="B. 'i'", command = wrong)
    button6.place(x=0,y=200)
    button7=Button(quiz,text="C. '90'", command = wrong)
    button7.place(x=0,y=225)
    label4=Label(quiz,font="10", text="Q3. Which is invalid in python for z = 5 ?")
    label4.place(x=0,y=265)
    button8=Button(quiz,text="A. z = ++z", command = wrong)
    button8.place(x=0,y=290)
    button9=Button(quiz,text="B. z = z++", command = right)
    button9.place(x=0,y=315)
    button10=Button(quiz,text="C. z += 1", command = wrong)
    button10.place(x=0,y=340)
    label5=Label(quiz, font="10",text="Q4. How can we generate random numbers in python using methods?")
    label5.place(x=0,y=380)
    button11=Button(quiz,text="A. random.uniform ()", command = wrong)
    button11.place(x=0,y=405)
    button12 = Button(quiz, text="B. random.randint()", command = wrong)
    button12.place(x=0, y=430)
    button13 = Button(quiz, text="C. random.random()", command = wrong)
    button13.place(x=0, y=455)
    button14=Button(quiz,text="D. All of the above", command = right)
    button14.place(x=0,y=480)
    label5=Label(quiz,font="10",text="Q5. What is output of following\n print('any'.encode())")
    label5.place(x=0,y=530)
    button15=Button(quiz,text="A. 'any'", command = wrong)
    button15.place(x=0,y=575)
    button16=Button(quiz,text="B. 'yan'", command = wrong)
    button16.place(x=0,y=600)
    button17=Button(quiz,text="C. b'any'", command = right)
    button17.place(x=0,y=625)
    button18=Button(quiz,font = "20",text="Submit",command=submission)
    button18.place(x=200,y=700)
    quiz.mainloop()
root.title("Quiz Game")
image = Image.open("photo.jpeg")
size=(500,500)
image=image.resize(size)
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.pack()
frame = Frame(bg = "green", borderwidth = 9)
frame.pack()
frame1 = Frame(bg = "red", borderwidth = 9)
frame1.pack()
button = Button(frame, font = "comicsansms 20" , fg = "red" , text = "Start Quiz", command= getval)
button.pack()
button1 = Button(frame1, font = "comicsansms 20" , fg = "green" , text = "Leave Site", command = closes)
button1.pack()
root.mainloop()
