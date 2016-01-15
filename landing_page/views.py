from landing_page import app
from flask import request, render_template, flash, redirect, url_for
from .forms import SubscribeForm


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SubscribeForm()
    if form.validate_on_submit():
        # form.save()
        flash('You have successfully subscribed')
        return render_template('index.html', form=form, subscribe=False)
    return render_template('index.html', form=form, subscribe=True)
