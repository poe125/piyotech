from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Your SMTP server
app.config['MAIL_PORT'] = 587  # SMTP port (usually 587)
app.config['MAIL_USERNAME'] = 'your-email@example.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'your-password'  # Your email password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject=subject,
                  sender='your-email@example.com',  # Your email address
                  recipients=['recipient@example.com'])  # Recipient email address

    msg.body = f"Message from: {name}\nEmail: {email}\n\n{message}"

    try:
        mail.send(msg)
        return 'Message sent!'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
