
from pydantic import  BaseModel , ConfigDict
from typing import List

class BlogBase(BaseModel):
    title: str
    body: str
    

class Blog(BlogBase):
      class Config():
            model_config = ConfigDict(from_attributes=True)
      




class User(BaseModel):
      name:str
      email:str
      password:str




class ShowUser(BaseModel):
      name:str
      email:str
      blogs: List[Blog] = []
      class Config():
            model_config = ConfigDict(from_attributes=True)



class ShowBlog(BaseModel):
        title:str
        body:str
        creator: ShowUser
        class Config():
            model_config = ConfigDict(from_attributes=True)





class Login(BaseModel):
      username:str
      password:str