from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# Set up flask and the Api
app = Flask(__name__)
api = Api(app)

# classes for the API and how to handle their get requests
#Class for information on api, when called will return its use case
class Info(Resource):

    def get(self):
        return jsonify({'1 URL layout':'/(comparetype)/(maxvalue)/(comparevalue)',
                        '2 Compare types':'/compareInt for integers or /compareFloat for floats',
                        '3 API CALL':'to call the api /max should be your max value /comparevalue will be the value compared to max', 
                        '4 API Return':'API will return SAFE as "Warning: 0" if value <= max or DANGER as "Warning: 1" if value > max'})
    
    def post(self):
        data = request.get_json()
        return jsonify({'data': data}), 201
    
# Class for the comparison API will take max then value to compare and return a warning of 0 for safe and 1 for danger
class CompareInt(Resource):
    def get(self, max, num):
        if max>=num:
            return jsonify({"Warning": 0})
        elif max<num:
            return jsonify({"Warning": 1})
        
class CompareFloat(Resource):
    def get(self, max, num):
        if max>=num:
            return jsonify({"Warning": 0})
        elif max<num:
            return jsonify({"Warning": 1})
    
api.add_resource(Info, '/')
api.add_resource(CompareInt, '/compareInt/<int:max>/<int:num>')
api.add_resource(CompareFloat,'/compareFloat/<float:max>/<float:num>')

if __name__ == '__main__':
    app.run(port=5010)