from flask import Flask, jsonify
from info_rede import get_status_hosts

app = Flask(__name__)
resp_host = get_status_hosts()

@app.route("/status-rede", methods=['GET'])
def get_status_rede():
    return jsonify(resp_host)
