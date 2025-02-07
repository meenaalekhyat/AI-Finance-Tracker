import React, {useState, useEffect} from "react";

const TransactionList=(props)=>{
    const [transactions, setTransactions]=useState([]);

    useEffect(()=>{
        fetch("http://localhost:5000/transactions")
        .then((response)=>{
            if(!response.ok){
                throw new Error("Network response was not okay")
            }
            return response.json()})
        .then((data)=>{
            console.log(data);
            if(data && data.Transactions){
                setTransactions(data.Transactions)
            }
            else{
                console.error("Transactions not found in response");
                setTransactions([]);
            }
        
        })
        .catch((error)=>console.error("Error fetching transactions: ", error));
    },[]);


    if (!transactions || transactions.length === 0) {
        return <div>Loading...</div>;  // Show a loading message if data is not loaded
      }
    
    return(

        <div>
            <h2>Transaction List</h2>
            <table>
                <thead>
                    <tr>
                        <th>Type</th>
                        <th>Source/Category</th>
                        <th>Amount</th>
                    </tr>
                </thead>
                <tbody>
                    {transactions.map((transaction, index)=>{
                        return(
                            <tr key={index}>
                            <td>{transaction.type}</td>
                            <td>{transaction.source || transaction.category}</td>
                            <td>{transaction.amount}</td>
                        </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>

    )

}

export default TransactionList;