import os
import smtplib
from flask import Flask,render_template,request,redirect

app = Flask(__name__)

students=[]
PASSWORD= "kimtaeb0ww"
@app.route("/")
def home_page():
    return render_template("home.html")
'''
@app.route("/registrants") 
def registrants():
    return render_template("registered.html",students=students)    
 '''    
@app.route("/register",methods=['POST'])
def register():
    name = request.form.get("name")
    dorm = request.form.get('dorm')
    email = request.form.get('email')
    
    if not name or not dorm or not email:
       return render_template("failure.html") 
   
    message = "Your registration is successful."
    server = smtplib.SMTP("smtp.gmail.com",587)# what server to send emai
    server.starttls()
    server.login("kim.tae.bow@gmail.com",os.getenv("PASSWORD"))
    server.sendmail("kim.tae.bow@gmail.com",email,message)
    return render_template("success.html") 
'''  
    students.append(f"{name} is from {dorm} and email id is {email}")
    return redirect("/registrants")
'''
 
    
   
    
