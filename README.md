# Fast_API


## 📌 About the Project

In this project, I practice:

- Building REST APIs with FastAPI  
- Designing request and response schemas with Pydantic  
- Connecting databases using SQLAlchemy  
- Performing CRUD operations  
- Handling exceptions and status codes  
- Implementing authentication with JWT  
- Securing routes using OAuth2  
- Using repository pattern for clean architecture  

---

## ⚙️ Environment Setup (Conda)

Create and activate conda environment:

`
```bash
conda create -n fastapi-env python=3.10
conda activate fastapi-env
```

## requirements.txt
```bash
fastapi
uvicorn
sqlalchemy
passlib
bcrypt
python-jose
python-multipart

pip install -r requirements.txt

```

## Run the project
```bash
uvicorn blog.main:app --reload
```
## Project Structure
```bash
blog/
 ├── main.py
 ├── models.py
 ├── schemas.py
 ├── database.py
 ├── routers/
 ├── repository/
 ├── oauth2.py
 ├── token.py


```


## 🛠 Tech Stack

- **FastAPI**  
- **Uvicorn**  
- **SQLAlchemy**  
- **Pydantic**  
- **Passlib + Bcrypt**  
- **JWT (python-jose)**  
- **OAuth2**  
- **SQLite / PostgreSQL**  

---


## 🌟 Contents


- Install and Setup  
- Project Structure Breakdown  
- Path Parameters  
- API Documentation (Swagger UI)  
- Query Parameters  
- Request Body Handling  
- Debugging  
- Pydantic Schemas  
- Database Connection  
- Create Models and Tables  
- Store Blog to Database  
- Get Blog from Database  
- Exception & Status Code  
- Delete a Blog  
- Response Model  
- Create User  
- Hash Password  
- Show User  
- Using Doc Tags  
- Relationship  
- API Router  
- API Router Path Operators  
- Blog & User Repository Pattern  
- Login & Verify Password  
- JWT Access Token  
- Routes Behind Authentication



