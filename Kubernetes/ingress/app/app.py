from flask import Flask 
from flask import jsonify 
from flask import Response
import socket, os 

app = Flask(__name__)

@app.route('/db')
def print_the_ip():
    hostname = socket.gethostname()
    get_local_ip = socket.gethostbyname(hostname)
    output = f"""
      <h1> This is the <b>Backend - Database</b> </h1>
      <h4> <b>POD_IP:</b> {get_local_ip} </h4> 
    """
    return output

@app.route('/health')
def print_health():
    return Response("{'health':'ok'}", status=201, mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


