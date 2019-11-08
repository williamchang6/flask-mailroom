import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donor, Donation 

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)
    
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_donor = Donor(name=request.form['name'])
        new_donor.save()
        new_donation = Donation(donor=new_donor, value=int(request.form['value']))
        new_donation.save()
        
        return redirect(url_for('all'))
    else:
        return render_template('create.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

