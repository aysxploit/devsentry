import os
from dotenv import load_dotenv
from app.triage import classify_error
from app.fixgen import generate_fix
from app.schemas import ErrorReportSchema
from langchain_core.runnables import RunnableMap
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.callbacks.tracers import LangChainTracer
from langchain.callbacks import tracing_v2_enabled

load_dotenv()

def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        google_api_key=os.getenv("GEMINI_API_KEY"),
        model_kwargs={"stream": False}
    )

async def process_error(report: ErrorReportSchema):
    llm = get_llm()
    chain = RunnableMap({
        "classification": lambda x: classify_error(llm, x),
        "fix_suggestion": lambda x: generate_fix(llm, x)
    })

    inputs = {
        "error": report.error_message.strip(),
        "stack": report.stack_trace.strip(),
        "lang": report.language.lower().strip()
    }

    with tracing_v2_enabled(project_name="devsentry"):
        return await chain.ainvoke(inputs)
