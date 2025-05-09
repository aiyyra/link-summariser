from langchain_groq import ChatGroq
from configs.settings import GROQ_API_KEY
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.prompt_loader import load_prompt

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama3-8b-8192" #"mixtral-8x7b-32768"
)

def summarize_text(text: str) -> str:

    prompt_template_str = load_prompt("summary_prompt.txt")
    prompt = PromptTemplate(
        input_variables=["content"],
        template=prompt_template_str
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(content=text[:3000])
