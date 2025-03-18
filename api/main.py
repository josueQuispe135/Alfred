from fastapi import FastAPI, Form
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="alfred"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,password))
    user=cursor.fetchone()
    cursor.close()
    if user:
        return {"message":"Login Success"}
    return {"message":"Login Failed"}

@app.post("/register")
def register(username: str = Form(...), password: str = Form(...)):
    cursor=conn.cursor()
    cursor.execute("INSERT INTO users (username,password) VALUES (%s,%s)",(username,password))
    conn.commit()
    cursor.close()
    return {"message":"Register Success"}

@app.get("/student")
def student():
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    users=cursor.fetchall()
    cursor.close()
    return users

@app.get("/student/{id}")
def student(id:int):
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student WHERE id=%s",(id,))
    user=cursor.fetchone()
    cursor.close()
    return user

#add student
@app.post("/add_student")
def add_student(name:str=Form(...),lastName:str=Form(...),age:int=Form(...)):
    cursor=conn.cursor()
    cursor.execute("INSERT INTO student (name,lastName,age) VALUES (%s,%s,%s)",(name,lastName,age))
    conn.commit()
    cursor.close()
    return {"message":"Add Student Success"}

#update student
@app.put("/update_student/{id}")
def update_student(id:int,name:str=Form(...),age:int=Form(...)):
    cursor=conn.cursor()
    cursor.execute("UPDATE student SET name=%s,age=%s WHERE id=%s",(name,age,id))
    conn.commit()
    cursor.close()
    return {"message":"Update Student Success"}
    
#delete student
@app.delete("/delete_student")
def delete_student(id:int=Form(...)):
    cursor=conn.cursor()
    cursor.execute("DELETE FROM student WHERE id=%s",(id,))
    conn.commit()
    return {"message":"Delete Student Success"}
