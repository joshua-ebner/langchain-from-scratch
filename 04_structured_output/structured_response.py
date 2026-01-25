from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class DefineAndGiveExample(BaseModel):
    """Define a term and give a usage example."""

    definition: str
    """A concise definition of the term"""
    example: str
    """An example usage illustrating the definition"""


llm = ChatOpenAI(model="gpt-4o-mini")
llm_structured_output = llm.with_structured_output(DefineAndGiveExample)

response = llm_structured_output.invoke(
    "What does the term 'Contribution Margin' mean in a business context?"
    )

#print(response)
print(response.definition)
print(response.example)