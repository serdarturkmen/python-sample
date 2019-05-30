from flask import Flask, request, Response, jsonify
import mock_data

app = Flask(__name__)


@app.route('/data/<int:aircraft_id>', methods=['GET'])
def get(aircraft_id):
    resp = jsonify(mock_data.get_data())
    resp.status_code = 200

    return resp


@app.route('/test', methods=['POST'])
def post():
    print(request.is_json)
    content = request.get_json()
    # print(content)
    print(content['id'])
    print(content['name'])
    return 'JSON posted'


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run()
