import os

import chainlit as cl
import openai

os.environ['OPENAI_API_KEY'] = ''
openai.api_key = ''


@cl.on_message
async def main(message: str):
    response = openai.ChatCompletion.create(
        model='gpt-4',
        message=[
            {"role": "assistant", "content": "you are a helpful assistant"},
            {"role": "user", "content": message}
        ],
        temperature=1,
    )
    await cl.Message(content=f"{response['choices'][0]['message']['content']}",).send()
