import os
from flask import Flask


def create_app():
    app = Flask(__name__)

    from .main.views import main_index
    app.register_blueprint(main_index)

    from .blog.views import blog_pages
    app.register_blueprint(blog_pages)

    return app
