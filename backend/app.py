from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import tensorflow as tf
import numpy as np
import pandas as pd
import os
print(os.listdir('./'))
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
#from models.expense_predictor import train_and_save_model
import joblib


app= Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

#mock database variables
#expenses=[]
#income=[]


app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///finance.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

#Defining models?? I am assuming its an alias for the columns of a table

class Income(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    source=db.Column(db.String(100), nullable=False)
    amount=db.Column(db.Float, nullable=False)
    date=db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return{
            "id":self.id,
            "source":self.source,
            "amount":self.amount,
            "date":self.date.strftime("%Y-%m-%d")
        }

class Expense(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    category=db.Column(db.String(100), nullable=False)
    amount=db.Column(db.Float, nullable=False)
    date=db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return{
            "id":self.id,
            "category":self.category,
            "amount":self.amount,
            "date":self.date.strftime("%Y-%m-%d")
        }


#Create the database table I guess, not sure exactly
with app.app_context():
    
    db.create_all()


#EXPENSE PREDICTOR MOVED HERE
def train_and_save_model():
    with app.app_context():
        expenses=Expense.query.order_by(Expense.date).all()

        expense_data=[]

        for expense in expenses:
            expense_data.append({"date":expense.date, "amount":expense.amount})

        df=pd.DataFrame(expense_data)
        df['month']=pd.to_datetime(df['date']).dt.month
        df['year']=pd.to_datetime(df["date"]).dt.year

        monthly_expenses=df.groupby(['year','month'])['amount'].sum().reset_index()

        X=monthly_expenses[["month"]].values
        y=monthly_expenses['amount'].values

        Scaler=MinMaxScaler()
        
        joblib.dump(Scaler, 'scaler.pkl')

        X_Scaled=Scaler.fit_transform(X)

        print(monthly_expenses.shape)

        # X_train, X_test, y_train, y_test=train_test_split(X_Scaled, y, test_size=0.2, random_state=42)

        model=tf.keras.Sequential([
            tf.keras.layers.Dense(10, input_dim=1, activation='relu'),
            tf.keras.layers.Dense(1)
        ])

        model.compile(optimizer='adam', loss='mean_squared_error')

        model.fit(X_Scaled, y, epochs=100, batch_size=100)

        model.save('expense_predictor.h5')
        return model


#Expense predictor I hope this worksss

@app.route('/predict_expenses', methods=['GET'])
def predict_expenses():
    try:
        
        last_month_data=Expense.query.order_by(Expense.date.desc()).first()
        if not last_month_data:
            return jsonify({"message":"No expense data found."})
        
        last_month=last_month_data.date.month
        X_new=np.array([[last_month+1]])
        Scaler = joblib.load('scaler.pkl')
        X_new_scaled=Scaler.transform(X_new)

        model=tf.keras.models.load_model('expense_predictor.h5')

        predicted_expense=model.predict(X_new_scaled)

        return jsonify({
            "predicted_expense": predicted_expense[0][0]
        })
    except Exception as e:
        print(f"Error in prediction : {e}")
        return jsonify({"error":"Failed to generate prediction."}),500


@app.route("/")

def home():
    return jsonify({"message":"Backend is working!"})

#add income
@app.route("/add_income", methods=["POST"])
def add_income():
    try:
        data=request.json
        new_income=Income(source=data["source"], amount=data["amount"], date=datetime.utcnow())
        db.session.add(new_income)
        db.session.commit()
        return jsonify({"message":"Income Added!", "income":new_income.to_dict()})
    except Exception as e:
        print(f"Error adding income: {e}")
        return jsonify({"error":"Failed to add income"}), 500

#add expense
@app.route("/add_expense", methods=["POST"])
def add_expense():
    try:
        data=request.json
        new_expense=Expense(category=data["category"], amount=data["amount"], date=datetime.utcnow())
        db.session.add(new_expense)
        db.session.commit()
        return jsonify({"message":"Expense Added!", "expense":new_expense.to_dict()})
    except Exception as e:
        print(f"Error adding expense: {e}")
        return jsonify({"error":"Failed to add expense"}), 500

#Summary
@app.route("/summary", methods=["GET"])
def summary():
    total_expense=db.session.query(db.func.sum(Expense.amount)).scalar() or 0
    total_income=db.session.query(db.func.sum(Income.amount)).scalar() or 0
    return jsonify({"total_income": total_income, "total_expense": total_expense})

#List of transactions:

@app.route("/transactions", methods=["GET"])
def get_transactions():
    try:
        income_list=Income.query.all()
        expense_list=Expense.query.all()

        transactions=[]

        for income in income_list:
            transactions.append({
                "type":"Income",
                "source":income.source,
                "amount":income.amount,
                "date": income.date.strftime("%Y-%m-%d")
            })
        
        for expense in expense_list:
            transactions.append({
                "type":"Expense",
                "category":expense.category,
                "amount":expense.amount,
                "date": expense.date.strftime("%Y-%m-%d")
            })
        return jsonify({"Transactions":transactions})
    except Exception as e:
        print(f"Error retrieving transactions:{e}")
        return jsonify({"error":"Failed to retrieve transactions"}), 500


if __name__=="__main__":
    with app.app_context():
        try:
            model=tf.keras.models.load_model('expense_predictor.h5')
            Scaler = joblib.load('scaler.pkl') 
        except:
            train_and_save_model()
            Scaler = joblib.load('scaler.pkl') 
    app.run(debug=True)