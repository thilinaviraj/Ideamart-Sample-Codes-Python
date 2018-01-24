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

@app.route('/caasSender', methods=["GET", "POST"])
def caas_request():

        res = {
               "chargeableBalance": "10",
               "password": "password",  # This should be replaced with your ideamart app password
               "applicationId": "APP_001", # Use your app ID
               "paymentInstrumentName": "MobileAccount",
               "subscriberId": "94777123456", # Use the MSISDN in the format you received
               "currency": "LKR"
               }
        with open("CAASRequest.txt", "w") as text_file:
            print("CAAS request: {}".format(res), file=text_file)
        url = "http://localhost:7000/caas/balance/query" # Use production API end point in the live system

        res = json.dumps(res).encode('utf8')
        req = urllib.request.Request(url, res, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response = urlopen(req)
        ideamart_respones = response.read()
        with open("CAASResponse.txt", "w") as text_file:
            print("CAAS response: {}".format(ideamart_respones), file=text_file)


if __name__ == '__main__':
    app.run(host="localhost", port=5000)

