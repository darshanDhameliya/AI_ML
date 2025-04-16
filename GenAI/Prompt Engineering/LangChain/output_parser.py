from typing import List, Dict, Any

from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

class SummaryModelLinkdin(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")
    key_skills: List[str] = Field(description="there kry skills")
    def to_dict(self)->Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts, "key_skills": self.key_skills}

summary_parser_linkedin = PydanticOutputParser(pydantic_object=SummaryModelLinkdin)


class MyInfo(BaseModel):
    technologies:List = Field(description="Technologies which i know", title="technology")

    def to_dict(self)->Dict[str, Any]:
        return {"technology": self.technology}
    
    @classmethod
    def model_json_schema(cls) -> Dict[str, Any]:
        return cls.schema()
    

summary_parser_my_info = PydanticOutputParser(pydantic_object=MyInfo)