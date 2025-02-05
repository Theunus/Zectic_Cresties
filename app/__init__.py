from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'thnsjnr.okelly33@gmail.com'
app.config['MAIL_PASSWORD'] = 'dsgmduvjlobylwwv'

mail = Mail(app)

# Import the routes
from app import routes