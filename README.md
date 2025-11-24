# 📝 Task Manager (To-Do List App)

This project is a web-based task management application developed as part of the practical assignments for the **Python Programming Bootcamp** (Tokio School). It allows users to create, organize, modify, and delete tasks, with visual tracking of deadlines.

## 🚀 Features

The application features a complete CRUD (Create, Read, Update, Delete) system:

* **Create Tasks:** Add new tasks with a description, category, and deadline.
* **Status Visualization:**
    * Tasks are visually marked if they are **done** (strikethrough).
    * Color indicators for deadlines:
        * 🟢 **Green:** Task is on time.
        * 🔴 **Red:** The deadline has passed.
* **Editing:** Modify the content, category, or date of an existing task.
* **Deletion:** Delete tasks you no longer need.
* **Data Persistence:** All tasks are saved in an SQLite database.

## 🛠️ Technologies Used

* **Backend:**
    * [Python 3.12](https://www.python.org/)
    * [Flask](https://flask.palletsprojects.com/) (Web Framework)
    * [SQLAlchemy](https://www.sqlalchemy.org/) (ORM for database management)
* **Frontend:**
    * HTML5 / CSS3
    * **Bootstrap 4** ([Bootswatch Sketchy](https://bootswatch.com/sketchy/) theme for a "hand-drawn" style).
    * Jinja2 (Template engine).
    * FontAwesome (Icons).
* **Database:**
    * SQLite

## 📂 Project Structure

```text
├── database/           # Contains the database (tareas.db)
├── static/             # CSS files (main.css)
├── templates/          # HTML Templates (index, create, modify)
├── db.py               # Database connection configuration
├── main.py             # Main file (Application routes)
├── models.py           # Data models (Task Class)
└── requirements.txt    # Project dependencies
```

## 🔧 Installation and Execution

Follow these steps to run the project locally on your machine:

### 1. Clone the repository
```bash
git clone https://github.com/RiquelmeRiquelme/GestorTareas.git
cd GestorTareas
```

### 2. Create and activate a virtual environment (Optional but recommended)
* Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
* macOS / Linux::
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
Install the required libraries listed in requirements.txt:
```bash
pip install -r requirements.txt
```

### 4. Run the application
Execute the main file to start the Flask server:
```bash
python main.py
```

### 5. Access the App
Open your web browser and go to: ```http://127.0.0.1:5000```
