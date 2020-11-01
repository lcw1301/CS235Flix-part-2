import os

from flask import Flask

import movie_app.adapters.repository as repo
from movie_app.adapters import memory_repository
from movie_app.adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = os.path.join('movie_app', 'adapters', 'data')

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    if app.config['REPOSITORY'] == 'memory':
        repo.repo_instance = memory_repository.MemoryRepository()
        memory_repository.populate(data_path, repo.repo_instance)

    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    with app.app_context():

        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .movies import movies
        app.register_blueprint(movies.movies_blueprint)

    return app
