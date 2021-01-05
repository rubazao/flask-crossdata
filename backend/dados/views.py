from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound


bp_dados = Blueprint('dados', __name__, template_folder='templates',
                     url_prefix='/dados/')


@bp_dados.route('/')
def dados():
    return render_template('dados.html')
