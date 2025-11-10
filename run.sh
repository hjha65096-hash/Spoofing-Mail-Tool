#!/usr/bin/env bash
set -e

# quick setup and run script for Linux/macOS
# usage: ./run.sh
if [ ! -f ".env" ]; then
  cp .env.example .env
  echo ".env created from .env.example — edit .env with real SMTP credentials before continuing."
  echo "Open .env in your editor, set SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASS then re-run ./run.sh"
  exit 0
fi

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

export FLASK_APP=app.py
export FLASK_ENV=development

echo "Starting Flask dev server on http://127.0.0.1:5000"
flask run --host=127.0.0.1 --port=5000
