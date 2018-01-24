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


@app.route('/ussdSender', methods=["GET", "POST"])
def ussd_sender():

        res = {
               "message": "1. Press One 2. Press two 3. Press three, 4. Exit",
               "destinationAddress": "tel:94777123456", # Use the MSISDN in the same format you received
               "password": "password",  # This should be replaced with your ideamart app password
               "applicationId": "APP_OO1", # Replace this with your APP ID
               "ussdOperation": "mt-cont",
               "sessionId": "1330929317043"
               }
        with open("USSDMT.txt", "w") as text_file:
            print("Message sent: {}".format(res), file=text_file)
        url = "http://localhost:7000/ussd/send" # Change the end point to the production when using in the live environment

        res = json.dumps(res).encode('utf8')
        req = urllib.request.Request(url, res, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response = urlopen(req)
        return response

if __name__ == '__main__':
    app.run(host="localhost", port=5000)
