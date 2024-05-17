import requests
import credentials

def do_test():

    
    config = credentials.get_ui_api_call_credentials("0")
    #custom1697428800000to1697463886191
    url = f"https://guu84124.live.dynatrace.com/rest/serviceanalysis/servicebacktrace?serviceId=SERVICE-19DC7FDCA52D14F8&sci=SERVICE-19DC7FDCA52D14F8&timeframe={config['timeframe']}"

    payload = None

    response = requests.request("GET", url, headers=config["headers"], data=payload)

    print(response.text)
    print(url)
