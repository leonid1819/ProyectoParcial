from flask import Flask, redirect, render_template,request, url_for, jsonify
from controller.bot import bot

app = Flask(__name__)

@app.route('/bot')
def robot():
    return render_template('bot.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	return str(bot(userText))

if __name__=='__main__':
    app.run(debug=True)


