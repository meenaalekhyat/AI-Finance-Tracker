import React, {useState, useEffect} from "react";
import {Line, Bar} from "react-chartjs-2"
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, BarElement, Filler } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, BarElement);

const ExpenseChart=()=>{
    const [expenses, setExpenses]=useState([]);

    useEffect(()=>{
        fetch("http://localhost:5000/transactions")
        .then((response)=>response.json())
        .then((data)=>{
            const expenseData=data.Transactions.filter(
                (transaction)=>transaction.type==="Expense"
            );
            console.log(expenseData)
            setExpenses(expenseData)
        }).catch((error)=>console.error("Error fetching trabsactions: ", error));
    }, []);

    const expenseCategories=[...new Set(expenses.map((expense)=>expense.data))]

    const expenseDates=[...new Set(expenses.map((expense)=>expense.date))]
    const expenseByDate=expenseDates.map((date)=>{
        return expenses
        .filter((expense)=>expense.date===date)
        .reduce((total,expense)=>total+expense.amount,0)
    })

    const categoryExpenses=expenseCategories.map((category)=>{
        return expenses
        .filter((expense)=> expense.category===category)
        .reduce((total,expense)=>total+expense.amount,0)
    })

    const lineChartData={
        labels:expenseDates,
        datasets:[
            {
                label:"Expense trend over time",
                data:expenseByDate,
                borderColor:"#FF6384",
                backgroundColor: "rgba(255, 99, 132, 0.2)",
                fill:true
            }
        ]
    }

    const barChartData={
        labels:expenseCategories,
        datasets:[
            {
                label: "Expenses by Category",
                data: categoryExpenses,
                backgroundColor: "#36A2EB",
                borderColor: "#36A2EB",
                borderWidth: 1
            }
        ]
    }


    return(
        <div>
            <h2>Expense Charts</h2>
        {/* LINE CHART */}
        {expenses.length===0?(
            <p>No expenses found to display</p>
        ):(
            <div>
                <h3>Expense Trend Over Time</h3>
                <Line data={lineChartData} />
            </div>
        )}
        {/* BAR CHART */}
        {expenses.length === 0 ? (
                <p>No expenses found to display</p>
            ) : (
                <div>
                    <h3>Expenses by Category</h3>
                    <Bar data={barChartData} />
                </div>
            )}



        </div>




    )

}

export default ExpenseChart;