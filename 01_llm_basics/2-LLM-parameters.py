from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model = "gpt-4o-mini"
                 ,temperature = .1
                 ,max_tokens = 100
                 ,top_p = 1
                 )

response = llm.invoke("Tell me 4 interesting things about the USA.")

print(response.content)