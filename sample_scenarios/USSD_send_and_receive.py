__author__ = 'Thilina_08838'
from flask import *

import urllib.request
from urllib.request import urlopen


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
        name = message_content["message"].split(" ")[1]
        res = {'message': "Hi, " + name,
               "destinationAddress": message_content["sourceAddress"].split(" ")[0],
               "password": "password",  # This should be replaced with your ideamart app password
               "applicationId": message_content["applicationId"],
               "ussdOperation": message_content["ussdOperation"],
               "sessionId": message_content["sessionId"]
               }
        with open("USSDMT.txt", "w") as text_file:
            print("Message sent: {}".format(res), file=text_file)
        url = "http://localhost:7000/ussd/send" #Change the end point to the production when using in the live environment

        res = json.dumps(res).encode('utf8')
        req = urllib.request.Request(url, res, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response = urlopen(req)
        return response

if __name__ == '__main__':
    app.run(host="localhost", port=5000)
