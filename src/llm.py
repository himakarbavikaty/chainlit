import os
from dotenv import load_dotenv
#from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
load_dotenv()


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY'] =GOOGLE_API_KEY

def ask_bot(model_name):
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    response = llm.invoke(message)
    return response.content

if __name__ == '__main__':
    print("Welcome to the chat bot!")
    message = ask_bot("what is a meaning of large language models?")
    print(message)