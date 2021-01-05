import os
from flask import Flask


def create_app():
    app = Flask(__name__)

    from .main.views import main_index
    from .blog.views import blog_pages
    from .dados.views import bp_dados
    from .contato.views import bp_contato
    app.register_blueprint(main_index)
    app.register_blueprint(blog_pages)
    app.register_blueprint(bp_dados)
    app.register_blueprint(bp_contato)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
