from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]


chatbot = ChatBot('Jarvis')

trainer = ListTrainer(chatbot)

trainer.train(conversation)


response = chatbot.get_response("That is good to hear")
print(response)
