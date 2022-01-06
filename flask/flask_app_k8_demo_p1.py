from flask import Flask
import socket

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    import socket
    my_ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1],
                       [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
                         [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    print('I am in index')
    return {f"name": f"Hello World! my ip: {my_ip}"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=8080)