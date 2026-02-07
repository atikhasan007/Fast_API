
from pydantic import  BaseModel , ConfigDict




class Blog(BaseModel):
    title: str
    body: str




class ShowBlog(BaseModel):
        title:str
        body:str
        class Config():
            model_config = ConfigDict(from_attributes=True)

class User(BaseModel):
      name:str
      email:str
      password:str




class ShowUser(BaseModel):
      name:str
      email:str
      class Config():
            model_config = ConfigDict(from_attributes=True)
    