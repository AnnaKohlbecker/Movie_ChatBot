# ChatBot with Open AI API

import time
from dotenv import load_dotenv, find_dotenv
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
import openai

load_dotenv(find_dotenv())


# @backoff.on_exception(backoff.expo, RateLimitError)
# def completions_with_backoff(**kwargs):
#     response = openai.Completion.create(**kwargs)
#     return response

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French. You keep it short."),
    HumanMessage(content="I love programming."),
]

def create_chat_with_rate_limit_handling(max_attempts=5, delay_seconds=60, max_tokens=10):
    for attempt in range(max_attempts):
        try:
            chat = ChatOpenAI(max_tokens=max_tokens)
            return chat
        except openai.RateLimitError:
            print(f"Rate limit reached, retrying in {delay_seconds} seconds. Attempt {attempt + 1} of {max_attempts}.")
            time.sleep(delay_seconds)
    raise Exception("Failed to create ChatOpenAI instance after multiple attempts.")

chat = create_chat_with_rate_limit_handling()
response = chat(messages)
print(response.content)
