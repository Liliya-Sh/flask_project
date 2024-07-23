from flask import Flask, jsonify, request

from model.twit import Twit

app = Flask(__name__)

twits = []


@app.route('/twit', methods=['POST'])
def create_twit():
    """{"id": 1, "body": "Hello, my name user1", "author": "@user1"}"""
    twit_json = request.get_json()
    twit_id = twit_json.get('id')
    twit_body = twit_json.get('body')
    twit_author = twit_json.get('author')

    if twit_id is None or twit_body is None or twit_author is None:
        return jsonify({'status': 'error', 'message': 'Missing required fields'})

    twit = Twit(twit_id, twit_body, twit_author)
    twits.append(twit)

    return jsonify({'status': 'success', 'twit': twit.to_json()})


@app.route('/twit', methods=['GET'])
def read_twits():
    twits_data = [twit.to_json() for twit in twits]
    return jsonify({'twits': twits_data})


@app.route('/twit/<int:id>', methods=['PUT'])
def update_twit(id):
    """{"id": 1, "body": "Hello, my name Alex", "author": "@user1"}"""
    twit_json = request.get_json()
    for twit in twits:
        if twit.id == id:
            twit.body = twit_json.get('body', twit.body)
            twit.author = twit_json.get('author', twit.author)
            return jsonify({'status': 'success'})
    return jsonify({'message': 'Twit not found'})


@app.route('/twit/<int:id>', methods=['DELETE'])
def delete_twit(id):
    twit_found = False
    for twit in twits:
        if twit.id == id:
            twits.remove(twit)
            twit_found = True
            break
    if twit_found:
        return jsonify({'status': 'success', 'message': f'Twit with id {id} has been deleted'})
    else:
        return jsonify({'message': 'Twit not found'})


if __name__ == '__main__':
    app.run(debug=True)
