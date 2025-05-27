import requests

def get_ips_from_spamhaus():
    url = "https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt"
    response = requests.get(url, timeout=5)
    return [line.strip() for line in response.text.splitlines() if line and not line.startswith("#")]
