from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]


chat_model = AzureChatOpenAI(deployment_name="GPT4-turbo", temperature=0)
chat_model(messages)
