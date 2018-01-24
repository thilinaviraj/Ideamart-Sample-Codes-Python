__author__ = 'Thilina_08838'
from flask import *

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    text1 = 'Hello World'
    return text1


@app.route('/ussdReceiver', methods=["GET", "POST"])
def ussd_receiver():

    if request.method == "GET":
        response = make_response("Yes, you are alive")
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response
    else:
        message_content = json.loads(request.data)
        with open("USSDMO.txt", "w") as text_file:
            print("Message Received: {}".format(message_content), file=text_file)

if __name__ == '__main__':
    app.run(host="localhost", port=5000)
