import React, {useEffect, useState} from "react";
import './App.css';
import ExpenseForm from "./components/ExpenseForm";
import IncomeForm from "./components/IncomeForm";
import TransactionList from "./components/TransactionList";
import ExpenseChart from "./components/ChartDivision";
import ExpensePredictor from "./components/ExpensePredictor";

function App() {
  const [summary, setSummary]=useState({total_expense:0, total_income: 0});
  

  const fetchSummary= ()=>{
    fetch("http://127.0.0.1:5000/summary")
    .then((res)=>res.json())
    .then((data)=>setSummary(data)).catch(error => console.log(error));
  };

  useEffect(()=>{
    fetchSummary();
  }, []);
  return (
   
    <div >
      <h1>Finance Tracker</h1>
      <div>
        <h2>Total Income: INR {summary.total_income}</h2>
      </div>
      
      <div>
      <h2>Total Expense: INR {summary.total_expense}</h2>
      </div>
      
      <div>
      <ExpenseForm refreshData={fetchSummary}/>
      </div>
      

      <div>
      <IncomeForm refreshData={fetchSummary}/>

      </div>

      <div>
        <TransactionList refreshData={fetchSummary}/>
      </div>

      <div>
        <ExpenseChart refreshData={fetchSummary}/>
      </div>

      <div>
        <ExpensePredictor refreshData={fetchSummary}/>
      </div>
      
    </div>
  );
}

export default App;
