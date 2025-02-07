from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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


@app.route("/")

def home():
    return jsonify({"message":"Backend is working!"})

#add income
@app.route("/add_income", methods=["POST"])
def add_income():
    try:
        data=request.json
        new_income=Income(source=data["source"], amount=data["amount"])
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
        new_expense=Expense(category=data["category"], amount=data["amount"])
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
    app.run(debug=True)