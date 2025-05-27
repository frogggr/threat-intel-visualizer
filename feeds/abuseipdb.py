import requests

def get_ips_from_abuseipdb():
    url = "https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt"
    response = requests.get(url)
    return [line.strip() for line in response.text.splitlines() if line and not line.startswith("#")]
