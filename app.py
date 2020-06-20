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




app = Flask(__name__)

@app.route('/chatbot/', methods=['POST'])
def home():
     # txt = text
     if request.method == 'POST':
          trainer = ListTrainer(chatbot)
          trainer.train(conversation)
          txt = str(request.form['message'])
          resp = stream_with_context(chatbot.get_response(txt))
          return Response(resp, status=200, mimetype='application/json')
          


if __name__ == '__main__':
     app.run(debug=True)
