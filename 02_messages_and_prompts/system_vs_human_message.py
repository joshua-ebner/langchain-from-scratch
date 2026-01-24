from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model = "gpt-4o-mini")

system_message = SystemMessage(
    """You are an AI assistant that replies to questions with 'Answer: ' 
       and then your reply"""
)

human_message = HumanMessage("What is the home of deep dish pizza?")

response = llm.invoke([system_message, human_message])

print(response.content)