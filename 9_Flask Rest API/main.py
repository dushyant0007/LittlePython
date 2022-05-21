from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


####################

####################

class bluePrint(Resource): 
    def get(self, name, age):
        # return {"data":"Hello World"}
        return {"name": name, "age": age}

    def post(self):
        return {"data": "Post Data"}


# api.add_resource(bluePrint,"/helloworld")


videos = {}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video")
video_put_args.add_argument("like", type=int)
video_put_args.add_argument("views", type=int)
video_put_args.add_argument("description", type=str)


class video(Resource):
    def get(self, videoId):
        if videoId in videos:
            return videos[videoId]
        else:
            return {"Error": "Id not exist"}

    def put(self, videoId):
        if videoId in videos:
            return {"Error": "The VideoId Already Exist"}
        else:
            data = video_put_args.parse_args()
            videos[videoId] = data
            return videos[videoId]

    def delete(self, videoId):
        if videoId not in videos:
            return {"Error": "The VideoId does't Exist"}
        else:
            del videos[videoId]
 

api.add_resource(video, "/video/<int:videoId>")

if __name__ == "__main__":
  
    app.run(debug=True)
