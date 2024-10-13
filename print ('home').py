import requests
import json
from datetime import datetime
from base64 import b64encode

# Define constants
business_short_code = "YOUR_BUSINESS_SHORT_CODE"
lipa_na_mpesa_online_passkey = "YOUR_PASSKEY"
phone_number = "USER_PHONE_NUMBER"  # Should be in the format 2547XXXXXXXX
amount = 10  # Payment amount
callback_url = "https://yourdomain.com/callback"
account_reference = "Wifi Payment"
transaction_desc = "Payment for Wifi access"

# Generate timestamp
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

# Create password (base64 of business short code + passkey + timestamp)
password = b64encode(f"{business_short_code}{lipa_na_mpesa_online_passkey}{timestamp}".encode()).decode('utf-8')

# Send STK push request
def initiate_stk_push():
    access_token = get_access_token()
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    payload = {
        "BusinessShortCode": business_short_code,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,  # Customer phone number
        "PartyB": business_short_code,
        "PhoneNumber": phone_number,
        "CallBackURL": callback_url,
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc,
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Initiate the push
response = initiate_stk_push()
print(response)
import requests
import json
from datetime import datetime
from base64 import b64encode

# Define constants
business_short_code = "YOUR_BUSINESS_SHORT_CODE"
lipa_na_mpesa_online_passkey = "YOUR_PASSKEY"
phone_number = "USER_PHONE_NUMBER"  # Should be in the format 2547XXXXXXXX
amount = 10  # Payment amount
callback_url = "https://yourdomain.com/callback"
account_reference = "Wifi Payment"
transaction_desc = "Payment for Wifi access"

# Generate timestamp
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

# Create password (base64 of business short code + passkey + timestamp)
password = b64encode(f"{business_short_code}{lipa_na_mpesa_online_passkey}{timestamp}".encode()).decode('utf-8')

# Send STK push request
def initiate_stk_push():
    access_token = get_access_token()
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    payload = {
        "BusinessShortCode": business_short_code,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,  # Customer phone number
        "PartyB": business_short_code,
        "PhoneNumber": phone_number,
        "CallBackURL": callback_url,
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc,
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Initiate the push
response = initiate_stk_push()
print(response)

