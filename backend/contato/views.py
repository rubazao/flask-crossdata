from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound


bp_contato = Blueprint('contato', __name__, template_folder='templates',
                       url_prefix='/contato/')


@bp_contato.route('/')
def contato():
    return render_template('contato.html')
