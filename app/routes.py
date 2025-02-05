from flask import render_template, request, flash, redirect, url_for
from flask_mail import Message
from app import app, mail
from app.forms import ContactForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # Send email
        msg = Message('New Contact Us Message',
                      sender=email,
                      recipients=['thnsjnr.okelly33@gmail.com'])  # Replace with your actual email address
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        mail.send(msg)

        flash('Thank you for your message!', 'success')
        return redirect(url_for('contact_us'))
    return render_template('contact_us.html', form=form)