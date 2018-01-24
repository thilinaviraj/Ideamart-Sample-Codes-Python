__author__ = 'Thilina_08838'
from flask import *

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    text1 = 'Hello World'
    return text1


@app.route('/smsReceiver', methods=["GET", "POST"])
def sms_receiver():

    if request.method == "GET":
        response = make_response("Yes, you are alive")
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response
    else:
        message_content = json.loads(request.data)

        with open("SMSMO.txt", "w") as text_file:
            print("Received message: {}".format(message_content), file=text_file) # Capture the incoming SMS


if __name__ == '__main__':
    app.run(host="localhost", port=5000)