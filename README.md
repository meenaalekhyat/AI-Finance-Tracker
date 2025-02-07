# AI Finance Tracker

An application that helps users track their finances, analyze trends, and make informed decisions using **AI**. The project is built with **React** for the front-end, and **Flask** with **SQLAlchemy** for the back-end.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies](#technologies)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The **AI Finance Tracker** combines powerful financial tracking tools with machine learning predictions to help users manage their personal finances. Built with a modern **React** front-end for user-friendly interaction and a **Flask** back-end with **SQLAlchemy** for data handling and storage, this application provides seamless integration and a secure environment.

## Features

- **AI-Powered Financial Predictions:** Predict your future financial trends using machine learning models.
- **Budget Tracker:** Track your income and expenses in an easy-to-use interface.
- **Data Visualizations:** View your financial data with graphs and charts for better decision-making.
- **Mobile-Responsive Design:** Fully responsive UI for a smooth experience on mobile devices.

## Technologies

- **Frontend:** React, React Router, Redux (optional)
- **Backend:** Flask, SQLAlchemy (ORM for database interaction)
- **Database:** SQLite (or PostgreSQL, depending on configuration)
- **Machine Learning:** Scikit-learn, Pandas, Numpy


## Installation

### Prerequisites

- **Node.js** and **npm** (for the React front-end)
- **Python 3.8+** (for the Flask back-end)
- **pip** (Python package manager)


### Steps to Install

#### **Frontend Setup (React)**

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/AI-Finance-Tracker.git
    ```

2. Navigate to the `frontend` directory:
    ```sh
    cd AI-Finance-Tracker/frontend
    ```

3. Install the React dependencies:
    ```sh
    npm install
    ```

4. Start the React development server:
    ```sh
    npm start
    ```

The React app should open in your browser (usually at `http://localhost:3000`).

#### **Backend Setup (Flask with SQLAlchemy)**

1. Navigate to the `backend` directory:
    ```sh
    cd ../backend
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```

4. Install the Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Set up the database:
    - Run the following command to create the database tables:
        ```sh
        python setup_db.py  # Or the script that initializes your database
        ```

6. Start the Flask back-end server:
    ```sh
    python app.py  # Or the file that runs your Flask app
    ```

The Flask server should now be running on `http://localhost:5000`.

### Connecting the Frontend and Backend

- Ensure both the **React front-end** and **Flask back-end** are running.
- The React app will interact with the backend through API calls (e.g., `http://localhost:5000/api`).

## Usage

Once the app is running, follow these steps:

1. Open the **React front-end** in your browser (`http://localhost:3000`).
2. Enter your financial data and use the AI-powered features to predict trends and track expenses.
3. The application will send API requests to the Flask back-end to process data and store it in the database.

### Example API Request:
```bash
curl -X GET "http://localhost:5000/api/financial-trends" -H "Authorization: Bearer <your_token>"
