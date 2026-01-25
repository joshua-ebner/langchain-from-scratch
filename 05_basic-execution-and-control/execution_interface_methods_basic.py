from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# INVOKE A MODEL WITH A SINGLE TEXT PROMPT
simple_prompt = "In one sentence, what is contribution margin?"
completion = llm.invoke(simple_prompt)
# Example output: a single text response


# CALL A MODEL ON A BATCH OF MULTIPLE PROMPTS
batch_prompt = [
    "In one sentence, what is contribution margin?",
    "In one sentence, what is customer acquisition cost?",
]
completions = llm.batch(batch_prompt)
# Example output: a list of text responses


# CALL A MODEL TO CREATE A STREAMING OUTPUT
stream_prompt = "Explain EBITDA in one sentence."
for chunk in llm.stream(stream_prompt):
    print(chunk.content, end="", flush=True)
    # Example output: text printed incrementally
    
print("\n")  # newline after streaming completes