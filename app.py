import chainlit as cl
from src.llm import ask_bot


@cl.on_message
async def main(user_message: cl.Message):

    response=ask_bot(user_message.content)
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {response.content}",
    ).send()
