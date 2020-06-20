from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

with open('train.txt') as f:
    data = f.readlines()


conversation = data


chatbot = ChatBot('Jarvis')

trainer = ListTrainer(chatbot)

trainer.train(conversation)


response = chatbot.get_response("What is Javascript")
print(response)
