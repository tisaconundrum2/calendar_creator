import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG_ID")
openai.engine = "davinci"

def some_foo(data):
    # Take the data and pass it to OpenAI's API along with the instsruction that we want to create a calendar event from the details of an email
    # The response will be a JSON object with the details of the calendar event
    # Return the JSON object
    response = openai.Completion.create(
        engine="davinci",
        prompt=data,
        temperature=0.3,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
