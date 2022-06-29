from chatterbot import  ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot('My Bot')

convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Pranav',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in Lucknow',
    'In which language you talk?',
    'I mostly talk in English'

]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

# print("talk to Bot")
# while True:
#     query=input()
#     if query=='exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ",answer)
#
# print(answer)


# creating window




main = Tk()

main.geometry("500x650")
main.title("My Chat Bot")
img = PhotoImage(file="bot1.png")
photoL = Label(main,image=img)

photoL.pack(pady=5)

def ask_from_bot() :
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"you : "+query)
    msgs.insert(END,"bot : "+str(answer_from_bot))
    textF.delete(0,END)


frame = Frame(main)

sc=Scrollbar(frame)
msgs = Listbox(frame, width=80 , height=20)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH , pady=10)
frame.pack()

# creating text field
textF = Entry(main , font=("Verdana",20))
textF.pack(fill=X , pady=10)

btn=Button(main,text="Ask from Bot",font=("Verdana",20), command=ask_from_bot)
btn.pack()
main.mainloop()