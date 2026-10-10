# My Notes — Notes Management Application

My Notes is a desktop-based notes management application built using Python. It allows users to create, view, edit, rename, and delete notes through a simple graphical user interface.

The application uses Tkinter for the frontend, FastAPI for the backend, and SQLite for storing note data.

## Features

- Create new notes
- View and select saved notes
- Edit and save note content
- Rename existing notes
- Delete notes
- Store note data in an SQLite database
- Communicate between the frontend and backend using REST APIs

## Tech Stack

- **Language:** Python
- **Frontend:** Tkinter
- **Backend:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Data Validation:** Pydantic
- **HTTP Requests:** Requests
- **API Server:** Uvicorn

## Project Structure

My-Notes/
├── backend/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── database/
├── frontend/
│   └── app.py
├── .gitignore
├── README.md
└── requirements.txt


## How It Works

1. The user interacts with the Tkinter desktop interface.
2. The frontend sends HTTP requests to the FastAPI backend using Requests.
3. The backend processes the requested CRUD operation.
4. SQLAlchemy communicates with the SQLite database.
5. The result is returned to the frontend and displayed to the user.

### Architecture


Tkinter Frontend
       |
       v
   Requests
       |
       v
  FastAPI Backend
       |
       v
    SQLAlchemy
       |
       v
   SQLite Database


## Installation and Setup

### Prerequisites

- Python 3.10 or later, compatible with the project's dependencies
- Git
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Karthikeyan-Sivakumar349/My-notes.git
```

### 2. Navigate to the project directory

```bash
cd My-notes
```

### 3. Create a virtual environment

```bash
python -m venv environment
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\environment\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the FastAPI backend

Open a terminal in the project directory and run:

```bash
uvicorn backend.main:app --reload
```

If your project uses a different module path, adjust this command to match your existing backend configuration.

The API is typically available at:

`http://127.0.0.1:8000`

You can explore the API documentation at:

`http://127.0.0.1:8000/docs`

### 7. Run the desktop application

Open a second terminal in the project directory, activate the virtual environment, and run:

```powershell
python frontend/app.py
```

Make sure the backend is running before opening the desktop application.

## Database

The application uses SQLite to store notes. The database file is local and is excluded from GitHub using `.gitignore`.

Ensure the application initializes the database and creates the required tables when running for the first time.

## Learning Outcomes

Through this project, I gained practical experience with:

- Building a desktop application using Tkinter
- Developing REST APIs with FastAPI
- Performing CRUD operations
- Integrating Python applications with SQLite
- Working with SQLAlchemy models and database sessions
- Handling HTTP requests between a frontend and backend
- Organizing a Python project into separate modules

## Future Improvements

- Add search functionality for notes
- Improve the user interface
- Add note categories and tags
- Implement automated testing
- Package the application for easier installation

## Author

Karthikeyan Sivakumar

GitHub: [Karthikeyan-Sivakumar349](https://github.com/Karthikeyan-Sivakumar349)

---

If you find this project useful, feel free to explore the repository and share your feedback.
