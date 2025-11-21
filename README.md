🚀 Django API – Setup & Run Guide

This guide explains how to clone, set up, install dependencies, run, and migrate a Django API project from Git.

📥 1. Clone the Repository
```bash
git clone https://github.com/GR-SALMAN/Stech-Shop-Django-API.git
cd yourrepo
```
🐍 2. Create a Virtual Environment
Windows:
```
python -m venv venv
```
macOS/Linux:
```
python3 -m venv venv
```
🔛 3. Activate the Virtual Environment
Windows:
```
venv\Scripts\activate
```
macOS/Linux:
```
source venv/bin/activate
```

📦 4. Install Dependencies

Make sure you are inside the activated virtual environment:
```

pip install -r requirements.txt
```

⚙️ 5. Apply Database Migrations
```
python manage.py migrate
```

▶️ 6. Run the Development Server
```
python manage.py runserver
```


The API will be available at:
```

http://127.0.0.1:8000/products
```

✏️ 7. Making Changes & Creating New Migrations

Whenever you modify models:

Create migration files:
```
python manage.py makemigrations
```

Apply migrations:
```
python manage.py migrate
```

📄 8. Freeze Requirements (If You Installed New Packages)
```
pip freeze > requirements.txt
```


Push this updated file to GitHub.
🧹 9. Recommended .gitignore Items
```
venv/
__pycache__/
*.pyc
db.sqlite3
.env
```

