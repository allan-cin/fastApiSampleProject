# BG tasks
# from fastapi import BackgroundTasks, FastAPI
#
# app = FastAPI()
#
#
# def write_notification(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         content = f"notification for {email}: {message}"
#         email_file.write(content)
#
#
# @app.post("/send-notification/{email}")
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notification")
#     return {"message": "Notification sent in the background"}


# metadata
# from fastapi import FastAPI
#
# description = """
# ChimichangApp API helps you do awesome stuff. 🚀
#
# ## Items
#
# You can **read items**.
#
# ## Users
#
# You will be able to:
#
# * **Create users** (_not implemented_).
# * **Read users** (_not implemented_).
# """
#
# app = FastAPI(
#     title="ChimichangApp",
#     description=description,
#     version="0.0.1",
#     terms_of_service="http://example.com/terms/",
#     contact={
#         "name": "Deadpoolio the Amazing",
#         "url": "http://x-force.example.com/contact/",
#         "email": "dp@x-force.example.com",
#     },
#     license_info={
#         "name": "Apache 2.0",
#         "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
#     },
# )
#
#
# @app.get("/items/")
# async def read_items():
#     return [{"name": "Katana"}]


# doc url
# from fastapi import FastAPI
#
# app = FastAPI(docs_url="/documentation", redoc_url=None)
#
#
# @app.get("/items/")
# async def read_items():
#     return [{"name": "Foo"}]


# static files
# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
#
# app = FastAPI()
#
# app.mount("/static", StaticFiles(directory="static"), name="static")


# Testing
# from fastapi import FastAPI
# from fastapi.testclient import TestClient
#
# app = FastAPI()
#
#
# @app.get("/")
# async def read_main():
#     return {"msg": "Hello World"}
#
#
# client = TestClient(app)
#
#
# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}


# Extended test
# from fastapi import FastAPI, Header, HTTPException
# from pydantic import BaseModel
#
# fake_secret_token = "coneofsilence"
#
# fake_db = {
#     "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
#     "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
# }
#
# app = FastAPI()
#
#
# class Item(BaseModel):
#     id: str
#     title: str
#     description: str | None = None
#
#
# @app.get("/items/{item_id}", response_model=Item)
# async def read_main(item_id: str, x_token: str = Header()):
#     if x_token != fake_secret_token:
#         raise HTTPException(status_code=400, detail="Invalid X-Token header")
#     if item_id not in fake_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return fake_db[item_id]
#
#
# @app.post("/items/", response_model=Item)
# async def create_item(item: Item, x_token: str = Header()):
#     if x_token != fake_secret_token:
#         raise HTTPException(status_code=400, detail="Invalid X-Token header")
#     if item.id in fake_db:
#         raise HTTPException(status_code=400, detail="Item already exists")
#     fake_db[item.id] = item
#     return item


# debugging
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
