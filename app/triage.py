from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.language_models.chat_models import BaseChatModel

def classify_error(llm: BaseChatModel, input_dict: dict):
    prompt = ChatPromptTemplate.from_template("""
Respond strictly in this JSON format:

{{
  "cause": "...",
  "component": "...",
  "severity": "..."
}}

Do NOT include markdown or explanation outside the JSON.

Error:
{error}

Stack Trace:
{stack}

Language:
{lang}
""")

    chain = prompt | llm | JsonOutputParser()
    return chain.invoke(input_dict)
