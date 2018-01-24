__author__ = 'Thilina_08838'
from flask import *

import logging
import urllib.request
from urllib.request import urlopen

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    text1 = 'Hello World'
    return text1


@app.route('/smsOperation', methods=["GET", "POST"])
def sms_ops():

    if request.method == "GET":
        response = make_response("Yes, you are alive")
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response
    else:
        message_content = json.loads(request.data)

        with open("SMSMO.txt", "w") as text_file:
            print("Received message: {}".format(message_content), file=text_file) # Capture the incoming SMS

        message = message_content["message"].split(" ")[1]
        res = {'message': " " + message,
               "destinationAddresses": message_content["sourceAddress"].split(" ")[0],
               "password": "password",  # Use your app password
               "applicationId": message_content["applicationId"]
               }
        with open("SMSMT.txt", "w") as text_file:
            print("send message: {}".format(res), file=text_file)
        url = "http://localhost:7000/sms/send" # Don't use localhost in the live API

        res = json.dumps(res).encode('utf8') #Send the encoded value to the API call
        req = urllib.request.Request(url, res, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response = urlopen(req)

        if response.getcode() == 200:
            logging.info('Message delivered Successfully!')
            response = make_response("Message delivered Successfully!")
            response.headers['Content-Type'] = 'application/json'
            response.headers['Accept'] = 'application/json'
            with open("DeliveryNotif.txt", "w") as text_file:
                print("send message: {}".format(response), file=text_file)
            return response
        else:
            logging.error(
                '*** Message not delivered Successfully ERROR-CODE: ' + str(response.getcode()) + ' ****')
            response = make_response("Message was not delivered Successfully!")
            response.headers['Content-Type'] = 'application/json'
            response.headers['Accept'] = 'application/json'
            with open("DeliveryNotif.txt", "w") as text_file:
                print("send message: {}".format(response), file=text_file)
            return response


if __name__ == '__main__':
    app.run(host="localhost", port=5000)