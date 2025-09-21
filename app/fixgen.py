from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.language_models.chat_models import BaseChatModel

def generate_fix(llm: BaseChatModel, input_dict: dict):
    prompt = ChatPromptTemplate.from_template("""
Respond strictly in this JSON format:

{{
  "explanation": "...",
  "fix": "...",
  "code": "..."
}}

Do NOT include markdown or code fences.

Error:
{error}

Stack Trace:
{stack}

Language:
{lang}
""")

    chain = prompt | llm | JsonOutputParser()
    return chain.invoke(input_dict)
