import requests

def get_geo(ip, source="Unknown", threat_type="Unknown"):
    try:
        url = f"http://ip-api.com/json/{ip}"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            if data.get("status") == "success" and data.get("lat") and data.get("lon"):
                return {
                    "ip": ip,
                    "lat": data.get("lat"),
                    "lon": data.get("lon"),
                    "org": data.get("org"),
                    "country": data.get("country"),
                    "source": source,
                    "threat_type": threat_type
                }
        print(f"Failed geo for {ip}: {r.text}")
    except Exception as e:
        print(f"[GEO ERROR] {ip} → {e}")
    return None
