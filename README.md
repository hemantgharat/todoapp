# To-Do App 📋

A simple **Django-based To-Do application** that allows users to add, update, and delete tasks with completion status.

## Features 🚀
- ✅ **Add new tasks**
- 🔄 **Update existing tasks**
- 🗑️ **Delete tasks**
- 🟢 **Mark tasks as completed or not completed**
- ⏳ **Display task creation and update timestamps**
- 🎨 **User-friendly UI with Bootstrap**

## Installation & Setup ⚙️

### 1️⃣ Clone the Repository
git clone https://github.com/hemantgharat/todo-app.git
cd todo-app

### 2️⃣ Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Run Migrations
python manage.py migrate

### 5️⃣ Start the Django Development Server
python manage.py runserver