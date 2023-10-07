from flask.views import MethodView
from flask import request,jsonify
from services.bookmark_service import BookmarkService

class BookmarkController(MethodView):

    def get(self):
        return jsonify(BookmarkService.get_bookmark())
    
    def post(self):
        # POSTリクエストのJSONデータを取得
        data = request.get_json()
        
        # 例: JSONデータ内の特定のキーの値を取得
        bookmark_name = data.get('name', None)
        
        # ... その他の処理 ...

        return jsonify({"message": "Data received", "name": bookmark_name})

   