import requests

def get_ips_from_alienvault():
    url = "https://otx.alienvault.com/api/v1/indicators/export?type=IPv4"
    response = requests.get(url)
    return [line.strip() for line in response.text.splitlines() if line and not line.startswith("#")]
