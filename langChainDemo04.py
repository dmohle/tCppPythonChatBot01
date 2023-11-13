# langChainDemo04.py
# Nov 12, 2023
# dH, Fresno, CA

import chainlit as cl
import os
import openai
from constants import apikey

os.environ['OPENAI_API_KEY'] = apikey
openai.api_key = apikey


@cl.on_message
async def main(message: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        # model = "gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": "you are a python programmer assistant!"},
            # message is the message variable that is from the user
            {"role": "user", "content": message.content}
        ],
        temperature=0.7
    )

    #  await cl.Message(content = message.content).send()
    # await cl.Message(content=str(response)).send()
    await cl.Message(content=response["choices"][0]["message"]["content"]).send()
