"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from flask import render_template, flash, url_for

from application import app
from decorators import login_required, admin_required
#from forms import ExampleForm
#from models import ExampleModel


def home():
    return render_template('home.html')


def contact():
    return render_template('contact.html')


def itservices():
    return render_template('itservices.html')


def disability():
    return render_template('disability.html')


def hooptedoodle():
    return render_template('hooptedoodle.html')


def specials():
    return render_template('specials.html')


def neohermes():
    return render_template('neohermes.html')


def dnamusic():
    return render_template('dnamusic.html')


def about():
    return render_template('about.html')


def presentative():
    return render_template('presentative.html')


def pyxcel():
    return render_template('pyxcel.html')


def products():
    return render_template('products.html')


def timeandtravel():
    return render_template('timeandtravel.html')


def web_pages():
    return render_template('web_pages.html')
