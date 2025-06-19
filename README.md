# 📁 File Management Web App (Streamlit + OOP)

This project is a **file management system** built using **Python** and **Streamlit**, implementing principles of **Object-Oriented Programming (OOP)**. It allows users to:

-  Sign Up & Log In
-  Manage (Add, Update, Delete) text-based records
-  Read and visualize CSV data
-  Perform summary, filtering, and download functions

---

##  Features

- **Streamlit Web App**: For GUI and interactive user input
- **OOP Design**: Code organized using classes and modular structure
- **Login/Signup**: Credentials stored in `users.txt`
- **Data Handling**: CRUD operations with text files
- **CSV Handler**: Preview CSV data, get summary, filter, and download

---

##  Technologies Used

- `Python 3.x`
- `Streamlit`
- `Pandas`
- OOP (Classes, Objects, Encapsulation)

---

##  Folder Structure

file_handler_101/
│
├── main.py # Streamlit main app with login/signup and GUI
├── handler.py # Handles file operations (text file)
├── csv_handler.py # CSV-related operations
├── user_handler.py # Handles user login/signup logic
├── data.txt # Main dataset for file operations
└── users.txt # Stores username/password





---

##  How to Run

1. Install Streamlit if not already:

```bash
pip install streamlit
streamlit run main.py
