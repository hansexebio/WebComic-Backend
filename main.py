from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import genres, users, categories

app = FastAPI()

# app = FastAPI(openapi_url='/api/v1/test',
#               docs_url='/api/v1/docs')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
    )

app.include_router(users.router, prefix='/api/users')
app.include_router(genres.router, prefix='/api/genres')
app.include_router(categories.router, prefix='/api/categories')

@app.get("/")
def read_root():
    return {"Hello": "World"}

#add middleware
#app - FaastApi(openapi_url)

# uvicorn main:app --reload