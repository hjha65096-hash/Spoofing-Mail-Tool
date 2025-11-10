@echo off
REM Windows helper: run.bat
IF NOT EXIST .env (
  copy .env.example .env
  echo .env created from .env.example. Edit .env and add SMTP credentials, then re-run run.bat
  pause
  exit /b 0
)

python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

set FLASK_APP=app.py
set FLASK_ENV=development

echo Starting server at http://127.0.0.1:5000
flask run --host=127.0.0.1 --port=5000
