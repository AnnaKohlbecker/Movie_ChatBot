# ChatBot with Hugging Face

import os
from dotenv import load_dotenv, find_dotenv
from langchain.schema import HumanMessage, SystemMessage
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_community.llms.huggingface_text_gen_inference import HuggingFaceTextGenInference
from huggingface_hub import login
# from huggingface_hub.utils._headers
load_dotenv(find_dotenv())

# https://huggingface.co/api/models
# http://localhost:8010/
# "https://api.endpoints.huggingface.cloud/v2/endpoint/AnnaKohlbecker"
ENDPOINT_URL = "http://localhost:8010/"
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
HF_TOKEN='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'

login(token=HF_TOKEN)
llm = HuggingFaceTextGenInference(
    inference_server_url=ENDPOINT_URL,
    max_new_tokens=200,
    top_k=10,
    temperature=0.1,
    repetition_penalty=1.03,
    token=HF_TOKEN,
    server_kwargs={
        "headers": {
            "Authorization": f"Bearer {HF_TOKEN}",
            "Content-Type": "application/json",
        }
    },
)
from langchain.schema import (
    HumanMessage,
    SystemMessage,
)

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French. You keep it short."),
    HumanMessage(
        content="I love programming."
    ),
]

chat_model = ChatHuggingFace(llm=llm, token=HF_TOKEN)
res = chat_model.invoke(messages)
print(res.content)