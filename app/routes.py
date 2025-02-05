from flask import render_template, request, flash, redirect, url_for
from app import app
from app.forms import ContactForm, AboutForm

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    form = AboutForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        inquiry = form.inquiry.data
        # Handle the form submission, e.g., send email or save to database
        flash('Thank you for your inquiry!', 'success')
        return redirect(url_for('about'))
    return render_template('about.html', form=form)

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        # Handle the form submission, e.g., send email or save to database
        flash('Thank you for your message!', 'success')
        return redirect(url_for('contact_us'))
    return render_template('contact_us.html', form=form)