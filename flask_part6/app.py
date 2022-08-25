from flask import Flask, jsonify, request
from calendar import isleap

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json})
    else:
        return jsonify({'about': 'Hello World'})

@app.route("/keliamieji/<int:metai>", methods=['GET'])
def keliamieji(metai):
    if isleap(metai):
        return jsonify({'result': "Keliamieji"})
    else:
        return jsonify({'result': "NE Keliamieji"})

if __name__ == '__main__':
    app.run()


# from flask import Flask, request
# from flask_restful import Resource, Api
# from calendar import isleap

# app = Flask(__name__)
# api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return{'about' :'Hello world!'}

#     def post(self):
#         some_json = request.get_json()
#         return {'you sent': some_json}, 201

# class Keliamieji(Resource):
#     def get(self, metai):
#         if isleap(metai):
#             return {'result': "Keliamieji"}
#         else:
#             return {'result': "NE Keliamieji"}

# api.add_resource(HelloWorld, '/')
# api.add_resource(Keliamieji, '/keliamieji/<int:metai>')

# if __name__ == '__main__':
#     app.run(debug=True)