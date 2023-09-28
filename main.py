import chainlit as cl
import openai
import os

os.environ['OPENAI_API_KEY'] = ''

@cl.on_messsage
async def main(message: str):
    await cl.Message(content = message).send()