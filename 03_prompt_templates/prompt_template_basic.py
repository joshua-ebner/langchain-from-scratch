from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


# Define prompt template
template = PromptTemplate.from_template(
    """This example demonstrates a prompt template with dynamic inputs.

Context:
{context}

Question:
{question}
"""
)


# Fill template variables
prompt = template.invoke(
    {
        "context": "AI and LLMs are changing how companies operate, improving efficiency and decision-making.",
        "question": "What are practical AI use cases for startups and mid-sized businesses?",
    }
)

# Define model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

# Execute
response = llm.invoke(prompt)

print(response.content)