import folium

def generate_map(ip_data_list, filter_type=None):
    m = folium.Map(location=[0, 0], zoom_start=2, tiles="CartoDB dark_matter")

    for entry in ip_data_list:
        if not entry["lat"] or not entry["lon"]:
            continue
        if filter_type and entry["threat_type"].lower() != filter_type.lower():
            continue
        folium.Marker(
            location=[entry["lat"], entry["lon"]],
            popup=f"{entry['ip']} ({entry['org']})<br>Type: {entry['threat_type']}<br>Source: {entry['source']}",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    with open("static/threat_map.html", "w", encoding="utf-8") as f:
        f.write(m.get_root().render())
