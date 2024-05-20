from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# Create flask
app = Flask(__name__)
# API object
api = Api(app)

# fuctiosn of the microservices

class Info(Resource):

    def get(self):
        return jsonify({'/compare/max/comparevalue':'/compare to call the api /max should be your max value /comparevalue will be the value compared to max', 
                        'API Return':'API will return SAFE as "Warning: 0" if value <= max or DANGER as "Warning: 1" if value > max'})
    
    def post(self):
        data = request.get_json()
        return jsonify({'data': data}), 201
    
    
class Comparison(Resource):
    def get(self, max, num2):
        if max>=num2:
            return jsonify({"Warning": 0})
        elif max<num2:
            return jsonify({"Warning": 1})
    
api.add_resource(Info, '/')
api.add_resource(Comparison, '/compare/<int:max>/<int:num2>')

if __name__ == '__main__':
    app.run(port=5010)