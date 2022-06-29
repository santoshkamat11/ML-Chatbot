from chatterbot import  ChatBot
from chatterbot.trainers import ListTrainer

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

print("talk to Bot")
while True:
    query=input()
    if query=='exit':
        break
    answer = bot.get_response(query)
    print("bot : ",answer)

print(answer)

