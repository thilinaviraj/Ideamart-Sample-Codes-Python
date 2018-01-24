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


@app.route('/lbsSender', methods=["GET", "POST"])
def lbs_request():

        res = {
                "applicationId": "APP_001768", # Use your app ID
                "password": "729fdf8ea178cdea9857eeb9a059fd6e", # Use your app password
                "subscriberId": "tel:94771234567", # Use the MSISDN in the format you received
                "serviceType": "IMMEDIATE",
                 "responseTime": "NO_DELAY",
                "freshness":  "HIGH",
                 "horizontalAccuracy": "1500",
                 "vesrion": "2.0"
                }

        with open("LBSRequest.txt", "w") as text_file:
            print("LBS request: {}".format(res), file=text_file)
        url = "http://localhost:7000/lbs/locate" # Use production URL in the live system

        res = json.dumps(res).encode('utf8')
        req = urllib.request.Request(url, res, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response = urlopen(req)
        ideamart_respones = response.read()
        with open("LBSResponse.txt", "w") as text_file:
            print("LBS response: {}".format(ideamart_respones), file=text_file)

if __name__ == '__main__':
    app.run(host="localhost", port=5000)

