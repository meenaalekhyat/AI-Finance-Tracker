import React, {useState, useEffect} from "react";
import axios from 'axios';

 const ExpensePredictor=()=>{
    const[prediction, setPrediction]=useState(null);

    useEffect(()=>{
        axios.get('http://localhost:5000/predict_expenses')
        .then(response=> setPrediction(response.data.predicted_expenses))
        .catch(error=> console.error('Error fetching prediction', error))
    }, []);

    return(
        <div>
            <h2>Expense Predictor</h2>
            {prediction!==null ? (
                <p>Predicted expense for the next month: ₹{prediction.toFixed(2)}</p>
            ):(
                <p>Loading prediction...</p>
            )

            }

        </div>
    )
}

export default ExpensePredictor;