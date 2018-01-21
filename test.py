__author__ = 'Thilina_08838'

from flask import *

import json
data = {}

app = Flask(__name__)
app.debug = True

@app.route('/smsReceiver1', methods=["GET", "POST"])
def sms_receiver():
    with open('data.txt', 'w') as f:
      json.dump(data, f, ensure_ascii=False)

if __name__ == '__main__':

    app.run(host="localhost", port=5000)