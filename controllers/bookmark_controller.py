from flask.views import MethodView
from flask import jsonify
from services.bookmark_service import BookmarkService

class BookmarkController(MethodView):

    def get(self):
        return jsonify(BookmarkService.get_bookmark())

   