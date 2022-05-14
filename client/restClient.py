# application/order_api/api/UserClient.py
import requests
import os
import sys
sys.stdout.flush()

# Get environment variables
SERVICE_2 = os.getenv('SERVICE_2')

class ServiceTwoClient:
    @staticmethod
    def get_user():
        
        response = requests.request(method="GET", url=SERVICE_2+"/service-2", headers={})
        print(response, flush=True)
        if response.status_code == 401:
            return "401 found"
        return str(response.text)

