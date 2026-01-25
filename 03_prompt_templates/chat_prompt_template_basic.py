from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Define chat prompt template with roles
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that answers concisely."),
        ("human", "{question}"),
    ]
)

# Fill variables
messages = prompt.invoke(
    {
        "question": "What are practical AI use cases for mid-sized businesses?"
    }
)

# Define model
llm = ChatOpenAI(model="gpt-4o-mini"
                 , temperature=0.2
                 )


# Execute
response = llm.invoke(messages)


print(response.content)