from flask import Flask, render_template, request, Response, stream_with_context
# from chatbot import chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

with open('train.txt') as f:
    conversation = f.readlines()

chatbot = ChatBot('Jarvis',
                  logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                  'chatterbot.logic.TimeLogicAdapter',
                                  'chatterbot.logic.BestMatch'])


trainer = ListTrainer(chatbot)
trainer.train(conversation)

app = Flask(__name__)

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/myjsbot/<text>')
def bot_response(text):
     # txt = text
     # if request.method == 'POST':
     txt = text
     # resp = chatbot.get_response(txt)
     print(type(txt))
     return str(chatbot.get_response(txt))
          # return str(resp)
          


if __name__ == '__main__':
     app.run(debug=True)
