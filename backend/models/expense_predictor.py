
import tensorflow as tf
import numpy as np
import pandas as pd
from datetime import datetime

import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

sys.path.append('../backend')
from app import Expense

# app= Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///finance.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

# db=SQLAlchemy(app)

# class Income(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     source=db.Column(db.String(100), nullable=False)
#     amount=db.Column(db.Float, nullable=False)
#     date=db.Column(db.Date, nullable=False, default=datetime.utcnow)

#     def to_dict(self):
#         return{
#             "id":self.id,
#             "source":self.source,
#             "amount":self.amount,
#             "date":self.date.strftime("%Y-%m-%d")
#         }

# class Expense(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     category=db.Column(db.String(100), nullable=False)
#     amount=db.Column(db.Float, nullable=False)
#     date=db.Column(db.Date, nullable=False, default=datetime.utcnow)

#     def to_dict(self):
#         return{
#             "id":self.id,
#             "category":self.category,
#             "amount":self.amount,
#             "date":self.date.strftime("%Y-%m-%d")
#         }

