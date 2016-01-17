from landing_page import app, UserDetail
from flask import render_template, flash
from .forms import SubscribeForm


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SubscribeForm()
    if form.validate_on_submit():
        if UserDetail.query.filter_by(email=form.email.data).first() is None:
            form.save()
            flash('You have successfully subscribed!')
        else:
            flash('You are already registered!')
        return render_template('index.html', form=form, subscribe=False)
    return render_template('index.html', form=form, subscribe=True)
