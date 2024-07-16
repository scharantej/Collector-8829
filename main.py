
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    
    # Validation
    if not email:
        flash('Email is required.')
        return redirect(url_for('home'))

    # Dummy data for demonstration
    subscribers = []
    subscribers.append(email)
    
    # Flash message
    flash('Subscribed successfully.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
