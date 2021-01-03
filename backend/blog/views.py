from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound


blog_pages = Blueprint('blog', __name__,
                       template_folder='templates', url_prefix='/blog/')


@blog_pages.route('/')
def blog():
    return render_template('blog.html')


@blog_pages.route('/post/')  # add id to dynamic post number
def blog_post():
    return render_template('blog-post.html')
