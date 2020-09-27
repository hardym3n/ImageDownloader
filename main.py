from  flask import Flask, request, json, make_response, jsonify
from flask_cors import CORS, cross_origin
import logic
import re
import requests.exceptions as req_execption


DEBUG = True
app = Flask(__name__)
CORS(app)


@app.route("/api/images/get", methods=['POST'])
def get_list():
    if request.method == 'POST':
        url = request.json['url']
        if url != None and re.search(r"(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$", url):
            try:
                a = logic.Worker(url)
                return jsonify(a.get_list())
            except req_execption.ConnectionError as E:
                return jsonify({"error": "Failed to establish a new connection"})
        else:
            return jsonify({'error': "incorrect url"})


if __name__ == "__main__":
    app.run(debug=DEBUG)