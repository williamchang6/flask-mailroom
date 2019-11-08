import os
import base64
import random

from flask import Flask, render_template, request, redirect, url_for, session

from model import db, Donor, Donation 

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
        name_input = request.form['name']
        value_input = request.form['value']
        name_exists = False
        for donor in Donor.select():
            if donor.name == name_input:
                Donation(donor=donor, value=int(value_input)).save()
                name_exists = True
        
        if not name_exists:
            new_donor = Donor(name=name_input)
            new_donor.save()
            new_donation = Donation(donor=new_donor, value=int(value_input))
            new_donation.save()
        
        
        return redirect(url_for('all'))
    else:
        return render_template('create.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

