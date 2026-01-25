from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


# SIMPLE LANGCHAIN COMPONENTS
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant specializing "
                   "in business and technology."
         ),
        ("human", "{question}"),
    ]
)


# COMBINE COMPONENTS INTO A FUNCTION
# The @chain decorator wraps a plain Python function
# and exposes standard LangChain runnable methods (e.g., .invoke()).

@chain
def chat_assistant(chat_inputs):
    prompt = chat_template.invoke(chat_inputs)
    return llm.invoke(prompt)


# use it

response = chat_assistant.invoke(
    {"question": (
        "What are some good use cases "
        "for AI in business?"
        )
    }
)
print(response.content)
