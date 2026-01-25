from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


# SIMPLE LANGCHAIN COMPONENTS
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are a helpful assistant specializing in business and technology."
        ),
        ("human", "{question}"),
    ]
)


# DECLARATIVE COMPOSITION USING THE `|` OPERATOR
# This pipes the output of the prompt template directly into the model.

chat_assistant = chat_template | llm


# INVOKE THE COMPOSED CHAIN
response = chat_assistant.invoke(
    {
        "question": (
            "In one sentence, what are common business use cases for AI?"
        )
    }
)
print(response.content)


# STREAMING OUTPUT
for chunk in chat_assistant.stream(
    {
        "question": "In one sentence, what does EBITDA measure?"
    }
):
    print(chunk.content, end="", flush=True)

print("\n")  # newline after streaming completes
