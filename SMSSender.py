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


@app.route('/smsSender', methods=["GET", "POST"])
def sms_sender():
        res = {
               "message": "Hello World",
               "destinationAddresses": "tel:94771122336", # Use the number, in format received from ideamart
               "password": "password",  # Use your app password
               "applicationId": "APP_001" # Use your app ID
               }
        with open("SMSMT.txt", "w") as text_file:
            print("send message: {}".format(res), file=text_file)
        url = "http://localhost:7000/sms/send" # Use production API in the live environment

        res = json.dumps(res).encode('utf8') #Send the encoded value to the API call
        req = urllib.request.Request(url, res, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response = urlopen(req)

        if response.getcode() == 200:
            logging.info('Message delivered Successfully!')
            response = make_response("Message delivered Successfully!")
            response.headers['Content-Type'] = 'application/json'
            response.headers['Accept'] = 'application/json'
            with open("DeliveryNotify.txt", "w") as text_file:
                print("send message: {}".format(response), file=text_file)
            return response
        else:
            logging.error('Message not delivered Successfully ERROR-CODE: ' + str(response.getcode()) + '')
            response = make_response("Message was not delivered Successfully!")
            response.headers['Content-Type'] = 'application/json'
            response.headers['Accept'] = 'application/json'
            with open("DeliveryNotify.txt", "w") as text_file:
                print("send message: {}".format(response), file=text_file)
            return response


if __name__ == '__main__':
    app.run(host="localhost", port=5000)