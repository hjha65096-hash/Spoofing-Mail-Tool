XMail — Local SMTP Email Sender (No Manual .env Editing)

This tool lets you send emails through any SMTP provider using a simple web interface.
On first launch, the app opens a Setup Page in your browser.
You just enter your SMTP details once — the app saves them automatically.

Features:
- Clean web UI
- Works with Gmail, Outlook, Yahoo, SendGrid, Mailgun, etc.
- First-run Setup Wizard (no .env editing)
- Remembers credentials
- Runs fully local

Requirements:
- Python 3.9+ OR Docker

Windows Run:
1. Extract the project.
2. Double-click run.bat
3. Browser opens → fill SMTP setup form → done.

Mac / Linux Run:
chmod +x run.sh
./run.sh
Browser opens → fill setup → done.

SMTP Credentials Guide:

Gmail (must use App Password):
SMTP Server: smtp.gmail.com
SMTP Port: 587
SMTP User: your@gmail.com
SMTP Pass: 16-character App Password

Outlook / Office365:
SMTP Server: smtp.office365.com
SMTP Port: 587
SMTP User: your email
SMTP Pass: your password or app password

Yahoo (requires App Password):
SMTP Server: smtp.mail.yahoo.com
SMTP Port: 587
SMTP User: your@yahoo.com
SMTP Pass: App Password

SendGrid:
SMTP Server: smtp.sendgrid.net
SMTP Port: 587
SMTP User: apikey
SMTP Pass: YOUR_SENDGRID_API_KEY

Docker Run:
docker build -t xmail .
docker run --env-file .env -p 5000:5000 xmail

Common Issues:
- Gmail: use App Password, not normal password.
- Port blocked: try port 465 instead of 587.
- Deliverability issues: use SendGrid/Mailgun for production.

To generate a Windows .exe:
Ask developer: "Make EXE"
