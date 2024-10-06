import http.client
import json
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from django.conf import settings

DEFAULT_FILTER_BACKENDS = (filters.DjangoFilterBackend, SearchFilter, )

def send_otp(otp, mobile_number):
    message = f"Your One Time Verification Code (OTP) is {otp} valid for 2 minutes. Please, donot share with anyone"
    send_sms(mobile_number,message)

def send_sms(to, message):

    conn = http.client.HTTPSConnection(settings.SMS_BASE_URL)
    payload = json.dumps({
        "messages": [
            {
                "destinations": [{"to":str(to)}],
                "from": "447491163443",
                "text": message
            }
        ]
    })
    headers = {
        'Authorization': f'App {settings.SMS_API_KEY}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", "/sms/2/text/advanced", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

