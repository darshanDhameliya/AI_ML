from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain
from output_parser import summary_parser_linkedin
import os
import requests

load_dotenv()
print(os.environ["OPENAI_API_KEY"])

profile_url = "https://gist.githubusercontent.com/ProfYash/334a960a354fdcfd9dffff72da19104b/raw/248dba53feec7d898e49ae8e888355d766741977/gistfile1.txt"
response= requests.get(profile_url,timeout=10)

linkedin_info = response.json();

summary = """
            give linkedin information of {information}
            give info like this:
            1. summary
            2. 2 interesting facts about him
            3. skills
            \n
            {output_formate}
        """

prompt = PromptTemplate(input_variables=["information"], template=summary, partial_variables={"output_formate": summary_parser_linkedin.get_format_instructions()})
llm = ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo')

# chain = LLMChain(llm=llm, prompt=prompt)
chain = prompt | llm | summary_parser_linkedin
res = chain.invoke(input={"information": linkedin_info})

print(res.__dict__)
