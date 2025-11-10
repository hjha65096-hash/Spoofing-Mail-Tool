import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = "xmail_secret"  # You can change this

# --- Helper function ---
def env_ready():
    return all([
        os.getenv("SMTP_SERVER"),
        os.getenv("SMTP_PORT"),
        os.getenv("SMTP_USER"),
        os.getenv("SMTP_PASS")
    ])

# Load env (if exists)
if os.path.exists(".env"):
    load_dotenv()

@app.route("/", methods=["GET", "POST"])
def index():
    if not env_ready():
        return redirect(url_for("setup"))

    from email.message import EmailMessage
    import smtplib

    if request.method == "POST":
        from_name = request.form["from_name"]
        from_email = request.form["from_email"]
        to_email = request.form["to_email"]
        subject = request.form["subject"]
        body = request.form["body"]

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = f"{from_name} <{from_email}>"
        msg["To"] = to_email
        msg.set_content(body)

        try:
            with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as smtp:
                smtp.starttls()
                smtp.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
                smtp.send_message(msg)

            flash("Email sent successfully!", "success")
        except Exception as e:
            flash(f"Error: {e}", "danger")

    return render_template("index.html")


@app.route("/setup", methods=["GET", "POST"])
def setup():
    if request.method == "POST":
        smtp_server = request.form["smtp_server"]
        smtp_port = request.form["smtp_port"]
        smtp_user = request.form["smtp_user"]
        smtp_pass = request.form["smtp_pass"]

        with open(".env", "w") as f:
            f.write(f"SMTP_SERVER={smtp_server}\n")
            f.write(f"SMTP_PORT={smtp_port}\n")
            f.write(f"SMTP_USER={smtp_user}\n")
            f.write(f"SMTP_PASS={smtp_pass}\n")

        flash("Setup complete! Restarting app...", "success")
        return redirect(url_for("index"))

    return render_template("setup.html")


if __name__ == "__main__":
    app.run(debug=True)
