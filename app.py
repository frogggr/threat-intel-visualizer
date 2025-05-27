from flask import Flask, render_template, request
from core.geolocation import get_geo
from core.map_plot import generate_map
from feeds.alienvault import get_ips_from_alienvault
from feeds.abuseipdb import get_ips_from_abuseipdb
from feeds.cybercrime import get_ips_from_cybercrime
from feeds.emerging_threats import get_ips_from_emerging_threats
from feeds.spamhaus import get_ips_from_spamhaus
from datetime import datetime
import ipaddress

def is_public_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_global
    except ValueError:
        return False


app = Flask(__name__)

def collect_threats():
    import random
    all_ips = []

    for ip in get_ips_from_alienvault()[:25]:
        if not is_public_ip(ip): continue
        geo = get_geo(ip, "AlienVault", "Scanning")
        print("AlienVault:", ip, geo)
        if geo: all_ips.append(geo)

    for ip in get_ips_from_abuseipdb()[:25]:
        if not is_public_ip(ip): continue
        geo = get_geo(ip, "AbuseIPDB", "Botnet")
        print("AbuseIPDB:", ip, geo)
        if geo: all_ips.append(geo)

    for ip in get_ips_from_cybercrime()[:25]:
        if not is_public_ip(ip): continue
        geo = get_geo(ip, "CyberCrime", "Malware")
        print("CyberCrime:", ip, geo)
        if geo: all_ips.append(geo)

    for ip in get_ips_from_emerging_threats()[:25]:
        if not is_public_ip(ip): continue
        geo = get_geo(ip, "EmergingThreats", "Compromised")
        print("Emerging:", ip, geo)
        if geo: all_ips.append(geo)

    for ip in get_ips_from_spamhaus()[:25]:
        ip_clean = ip.split("/")[0]
        if not is_public_ip(ip_clean): continue
        geo = get_geo(ip_clean, "Spamhaus", "Spam")
        print("Spamhaus:", ip_clean, geo)
        if geo: all_ips.append(geo)

    random.shuffle(all_ips)
    selected = all_ips[:15]  # just 15
    print(f"Collected {len(selected)} markers")
    return selected

from datetime import datetime

@app.route("/")
def index():
    filter_type = request.args.get("filter")
    ip_data = collect_threats()
    generate_map(ip_data, filter_type)

    # Pass timestamp to avoid browser caching
    return render_template("index.html", timestamp=datetime.utcnow().timestamp())

@app.route("/lookup", methods=["GET", "POST"])
def lookup():
    if request.method == "POST":
        ip = request.form["ip"]
        geo = get_geo(ip, "User", "Lookup")
        generate_map([geo] if geo else [], None)
        return render_template("index.html")
    return render_template("lookup.html")

if __name__ == "__main__":
    app.run(debug=True)
