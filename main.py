from langchain.llms.openai import OpenAI
from langchain.chat_models.openai import OpenAIChatModel
from langchain.vectorstores.qdrant import Qdrant
from langchain.prompts import PromptTemplate
from context_rephrase import context
import transformers
import os
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(
    model_name="gpt-3.5-turbo-16k", 
    temperature=0.0, 
    max_tokens=64,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    streaming=True,
    use_cache=True,
)

prompt_template = PromptTemplate(
    input_variables=["query","context","system_details"],
    template=
    """
    Context : {context}
    System Details : {system_details}
    Query : {query}

    """
)
obsenity_prompt_template = PromptTemplate(
    input_variables=[f"formal and polite"],
    template=
    """
    Context : {context}
    System Details : {system_details}
    Query : {query}

    """
)