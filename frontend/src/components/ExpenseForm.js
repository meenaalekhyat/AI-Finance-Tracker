import {useState} from "react";

function ExpenseForm({refreshData}){
    const[amount, setAmount]=useState("");
    const [category, setCategory]=useState("");

    const handleSubmit=async(e)=>{
        e.preventDefault();
        const response=await fetch("http://127.0.0.1:5000/add_expense",{
            method: "POST",
            headers:{"Content-Type":"application/json"},
            "body":JSON.stringify({amount:parseFloat(amount), category}),
            
        })

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        await response.json();
        refreshData();
    }

    return(
        <form onSubmit={handleSubmit}>
            <input
            type="number"
            value={amount}
            placeholder="Amount"
            onChange={(e)=> setAmount(e.target.value)}
            />
            <input
            type="text"
            value={category}
            placeholder="Amount"
            onChange={(e)=> setCategory(e.target.value)}
            />
            <button type="submit">Add Expense</button>

        </form>
    )
}

export default ExpenseForm;