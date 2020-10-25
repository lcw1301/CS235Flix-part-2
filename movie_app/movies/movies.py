from flask import Blueprint
from flask import request, render_template, url_for
import movie_app.adapters.repository as repo
import movie_app.movies.services as services

movies_blueprint = Blueprint('movies_bp', __name__)


@movies_blueprint.route('/movies_by_rank', methods=['GET'])
def movies_by_rank():
    movies_per_page = 2

    cursor = request.args.get('cursor')

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    movie_ranks = list(range(1, 1001))

    movies = services.get_movies_by_rank(movie_ranks[cursor:cursor + movies_per_page], repo.repo_instance)
    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if cursor > 0:
        prev_movie_url = url_for('movies_bp.movies_by_rank', cursor=cursor - movies_per_page)
        first_movie_url = url_for('movies_bp.movies_by_rank')

    if cursor + movies_per_page < len(movie_ranks):
        next_movie_url = url_for('movies_bp.movies_by_rank', cursor=cursor + movies_per_page)
        last_cursor = movies_per_page * int(len(movie_ranks) / movies_per_page)
        if len(movie_ranks) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('movies_bp.movies_by_rank', cursor=last_cursor)

    return render_template(
        'movies.html',
        title='Movies',
        movies=movies,
        first_movie_url=first_movie_url,
        last_movie_url=last_movie_url,
        prev_movie_url=prev_movie_url,
        next_movie_url=next_movie_url,
    )
