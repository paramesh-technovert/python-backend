This is a modular FastAPI backend for utility operations, including:

🧮 Number operations: addition, subtraction, multiplication, division

🔤 String operations: reverse, concatenate, check anagram

It also includes:

Auto virtual environment creation

Environment variable support using .env

Bash script for one-command startup

🗂️ Folder Structure
python_backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── numberOperations.py
│   │   └── stringOperations.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── numbers.py
│   │   └── strings.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── giveaptname.py
├── .env
├── requirements.txt
├── run.sh
⚙️ Setup Instructions (Windows)
✅ 1. Open Terminal in Project Folder
Use Git Bash, WSL, or Windows Terminal:
cd path/to/python-backend
✅ 2. Run the App
bash run.sh
✔ This will:

Auto-create a virtual environment if it doesn't exist

Activate the environment

Install required dependencies

Start the FastAPI server

🌐 API Usage
Visit the interactive API docs at
http://127.0.0.1:8000/docs
➤ Number Operations
Endpoint	Method	Example Input
/numbers/add	POST	{ "numbers": [1, 2, 3] }
/numbers/subtract	POST	{ "a": 10, "b": 4 }
/numbers/multiply	POST	{ "numbers": [2, 3, 4] }
/numbers/divide	POST	{ "a": 10, "b": 2 }

➤ String Operations
Endpoint	Method	Example Input
/strings/reverse	POST	{ "text": "hello" }
/strings/concat	POST	{ "first": "hello", "second": "world" }
/strings/isanagram	POST	{ "first": "listen", "second": "silent" }

🔐 Environment Configuration
Create a .env file in the project root:


⚠️ Notes
Run only with python -m uvicorn app.main:app — avoid calling .venv/Scripts/uvicorn directly (causes permission issues).

Use Git Bash or WSL for executing run.sh on Windows.

Ensure .env and .venv are in the root folder.
