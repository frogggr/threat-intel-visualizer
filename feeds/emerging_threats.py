import requests
import re

def get_ips_from_emerging_threats():
    url = "https://rules.emergingthreats.net/blockrules/compromised-ips.txt"
    response = requests.get(url)
    return [line.strip() for line in response.text.splitlines() if re.match(r"\d+\.\d+\.\d+\.\d+", line)]
