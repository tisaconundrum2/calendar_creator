"""
[ ] Flask app to create calendar events from text
    [x] Create a Flask app
    [x] Create a route for the API endpoint to receive a POST request with a string of text
    [ ] Create a function that takes the string
        [ ] Function will take that string and pass it to OpenAI's API
        [ ] Function will ask OpenAI's API to see if there is any content that looks like a calendar event
        [ ] If there is a calendar event, return an output JSON payload with the event details
        [ ] If there is no calendar event, return an output JSON payload with a message saying no event was found
        [ ] Return the output JSON payload
    [ ] Return the output JSON payload to the API endpoint
"""

from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import openai
load_dotenv()

app = Flask(__name__)


@app.route("/import-event", methods=["POST"])
def get_event():
    data = request.get_json()
    some_foo(data)
    return jsonify(response)
