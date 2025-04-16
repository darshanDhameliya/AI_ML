from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv
from output_parser import summary_parser_my_info

load_dotenv()

llm = ChatOpenAI(temperature=0.7)

template = """
context: I am javascript developer. and currently i am learning AI and work on AI project.

task: {task}

instruction: if answer is out of context reply: sorry, i have not a answer.

\n {formate_instruction}
"""

prompt = PromptTemplate(input_variables=["task"], template=template, partial_variables={"formate_instruction": summary_parser_my_info.get_format_instructions()})
chain = LLMChain(llm=llm, prompt=prompt)

input = {
    "task": "tell me something about my technology."
}
res = chain.invoke(input=input)

print(res)