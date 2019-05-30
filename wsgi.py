from flask import Flask, request, Response, jsonify
import mock_data

application = Flask(__name__)


@application.route('/data/<int:aircraft_id>', methods=['GET'])
def get(aircraft_id):
    resp = jsonify(mock_data.get_data())
    resp.status_code = 200

    return resp


@application.route('/test', methods=['POST'])
def post():
    print(request.is_json)
    content = request.get_json()
    # print(content)
    print(content['id'])
    print(content['name'])
    return 'JSON posted'


@application.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8086)
