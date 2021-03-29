from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app=Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres321@localhost/data_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://yacyhbxjuqdnro:13c240cbcd7ad805fdc95bd93afe60f3aaacc38c2b0ee42b3bc9fd31f0c28968@ec2-18-210-180-94.compute-1.amazonaws.com:5432/dekc2l2kotj4hf?sslmode=require'

db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    name_=db.Column(db.String(30))
    email_=db.Column(db.String(120), unique=True)
    message_=db.Column(db.String(300))
    

    def __init__(self, name_, email_, message_):
        self.name_=name_
        self.email_=email_
        self.message_=message_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        name=request.form["name"]
        email=request.form["email"]
        message=request.form["message"]
        print(name, email, message)
        if db.session.query(Data).filter(Data.email_ == email).count()== 0:
            user_data=Data(name, email, message)
            db.session.add(user_data)
            db.session.commit()
            send_email(name, email, message)
            return render_template("success.html")
    return render_template('index.html', text="Seems like we got something from that email once!")



if __name__ == '__main__':
    app.debug=False
    app.run()
    app.run(debug=False)
