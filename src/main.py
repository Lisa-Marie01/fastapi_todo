from typing import Annotated
from fastapi import FastAPI, APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import mysql.connector

app = FastAPI()
templates = Jinja2Templates(directory="./templates")

class TodoItem(BaseModel):
        description: str
        id = int = None
        status = str

# CREATE SERVER CONNECTION
def create_server_connetion():
cnx = None
DB_USER="Lisa"
DB_Password=""
DB_HOST="127.0.0.1"
DB_DATABASE="to-do"
try:
    cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_DATABASE)
    print ("Database connection successful")
except Error as err:
    print("Erros, '{err}'")
return cnx

def getDataFromDB(cnx):
     cursor = cnx.cursor()
     query = "SELECT * FROM items;"
     cursor.execute(query)
     items = cursor.fetchall()
     return items

def InsertIntoDB(cnx):
     cursor = cnx.cursor
     query = "INSERT INTO items (item) VALUES (s);"
     data = [item]
     try:
            cursor.execute(query, data)
            cnx.commit()
            print("Data inserted successfully")
     except Error as err:
          print(f"Error: '{err}'")

def deleteFromDB(cnx, id):
     cursor = cnx.cursor
     query = "DELETE FROM items WHERE id = %s;"
     id = [id]
     try:
            cursor.execute(query,id)
            cnx.commit
            print("Data deleted successfully")
     except Error as err:
          print(f"Error: '{err}'")

cursor = cnx cursor
         
TABLES ["to-do"] = ("")
query = ("INSERT INTO items" "id, item, status) "VALUE (%s, %s, %s)")
         
data = ("1", "Zimmer aufräumen", "abc")

@app.get("/", response_class=HTMLResponse)
def get_root(request: Request):
            cnx = create_server_connection()
            cursor = cnx.cursor()
            select_sql = "SELECT * FROM intems;"
            cursor.execute(select_sql)
            items = cursor.fetchall()
            cursor.close()
            cnx.close()
            return templates.templateResponse/"index.html", {"request": request, "items": items})

@app.post("/additem"), response_class=RedirectResponse
def post_insertIntoDB(item: Annotated[str, Form()]):
    cnx = create_server_connection()
    print("CONNECTION", cnx)
    InsertIntoDB(cnx, item)
    return RedirectResponse(url="http://127.0.0.1:8000", status_code=303)

@app.post("/deleteitem"), response_class=RedirectResponse
def post_deleteFromDB(id:Annotated[str, Form()]):
cnx = create_server_connection()
print("CONNECTION", cnx)
deleteFromDB(cnx, id)
return RedirectResponse(url="http://127.0.0.1:8000", status_code=303)

@app.post("/updateitem"), response_class=RedirectResponse
def post_updateFromDB(id:Annotated[str, Form()]):
cnx = create_server_connection()
print("CONNECTION", cnx)
updateFromDB(cnx, id)
return RedirectResponse(url="http://127.0.0.1:8000", status_code=303)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)