#Threat Intelligence Visualizer

Real-time cyber threat map that pulls malicious IPs from public feeds, geolocates them, and plots them on a dark-mode world map using Folium + Flask.

#Features
Pulls IPs from:
 - AlienVault OTX
 - AbuseIPDB
 - CyberCrime Tracker
 - Emerging Threats
 - Spamhaus DROP 
Geolocates IPs via `ip-api.com`
Dark-mode map with Leaflet
Shows 30 random public IP markers on each refresh
Manual “Refresh” button (no auto-refresh)
IP Lookup tool to view geolocation of any public IP

#Project Structure
threat-intel-visualizer/
├── app.py
├── core/
│ ├── geolocation.py
│ └── map_plot.py
├── feeds/
│ ├── alienvault.py
│ ├── abuseipdb.py
│ ├── cybercrime.py
│ ├── emerging_threats.py
│ └── spamhaus.py
├── static/
│ └── threat_map.html
├── templates/
│ ├── index.html
│ └── lookup.html
├── requirements.txt
└── README.md

#INSRUCTIONS
1. **Clone the repo:**
git clone https://github.com/frogggr/threat-intel-visualizer.git
cd threat-intel-visualiser

2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the App
python3 app.py

5. Open in your browser
http://127.0.0.1:5000/


#License
MIT License

Copyright (c) 2025 Liam Dupere

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


#Author
built by LiamDupere (Frogggr)


