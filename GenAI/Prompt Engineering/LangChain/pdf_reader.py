import PyPDF2
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv
from output_parser import summary_parser_my_info

load_dotenv()

llm = ChatOpenAI(temperature=0.7)

file_path = '/home/darshan/dev/DR/training/AI_ML/datafiles/Divya Waghmare Resume.pdf'

with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    pdf_data = ""
    for page in reader.pages:
        pdf_data += page.extract_text()

template = """
context: {pdf_data}.

task: {task}

instruction: if answer is out of context reply: sorry, i have not a answer.
"""

prompt = PromptTemplate(input_variables=["task"], template=template, partial_variables={"pdf_data": pdf_data})
chain = LLMChain(llm=llm, prompt=prompt)

input = {
    "task": "What is name?"
}
res = chain.invoke(input=input)

print(res)