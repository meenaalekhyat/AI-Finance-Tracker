import {useState} from "react";

function IncomeForm({refreshData}){
    const[amount, setAmount]=useState("");
    const [source, setSource]=useState("");

    const handleSubmit=async(e)=>{
        e.preventDefault();
        const response=await fetch("http://127.0.0.1:5000/add_income",{
            method: "POST",
            headers:{"Content-Type":"application/json"},
            "body":JSON.stringify({amount:parseFloat(amount), source}),
            
        })
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
            value={source}
            placeholder="Amount"
            onChange={(e)=> setSource(e.target.value)}
            />
            <button type="submit">Add Income</button>

        </form>
    )
}

export default IncomeForm;