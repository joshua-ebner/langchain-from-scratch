from langchain_core.output_parsers import CommaSeparatedListOutputParser

parser = CommaSeparatedListOutputParser()

# Demonstrates parsing comma-separated text into a Python list
response = parser.invoke("revenue, profit, EBITDA, contribution margin")
print(response)