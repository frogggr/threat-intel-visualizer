import requests

def get_ips_from_cybercrime():
    url = "https://cybercrime-tracker.net/all.php"
    response = requests.get(url)
    return list(set(line.strip().split(",")[0] for line in response.text.splitlines() if line))
