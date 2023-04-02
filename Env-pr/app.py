from flask import Flask, request, jsonify, render_template
import json
import rasa.shared.utils.io
from rasa.core.agent import Agent
import asyncio

app = Flask(__name__)
model_path = "./models/20230402-044402-colorful-frame.tar.gz"

# load the model
agent = Agent.load(model_path)

# define the endpoint for the chatbot interface
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    response = asyncio.run(agent.handle_text(user_input))
    return jsonify(response)


if __name__ == "__main__":
    app.run()
