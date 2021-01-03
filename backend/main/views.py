from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound


main_index = Blueprint('index', __name__,template_folder='templates')

@main_index.route('/')
@main_index.route('/home/')
def index():
    return render_template('index.html')