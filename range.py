import requests


def find_tennis_courts_nearby(lat: float, lon: float) -> str:
    query = f"""
    [out:json][timeout:25];
    (
      node["sport"="tennis"](around:12000,{lat},{lon});
      way["sport"="tennis"](around:12000,{lat},{lon});
      node["name"~"tennis|Tennis"](around:12000,{lat},{lon});
      way["name"~"tennis|Tennis"](around:12000,{lat},{lon});
    );
    out center;
    """

    try:
        response = requests.post("https://overpass-api.de/api/interpreter", data=query, timeout=30)
        data = response.json()
        elements = data.get("elements", [])

        if not elements:
            return show_google_search(lat, lon)

        courts = []

        for element in elements:
            tags = element.get("tags", {})
            name = tags.get("name", "Tennis Court")

            if name not in courts:
                courts.append(name)

        if not courts:
            return show_google_search(lat, lon)

        message = "🎾 Tennis courts near you:\n\n"

        for name in courts[:8]:
            search_name = name.replace(" ", "+")
            google_link = f"https://www.google.com/maps/search/{search_name}"
            message += f"• {name}\n  🔗 {google_link}\n\n"

        return message.strip()

    except:
        return show_google_search(lat, lon)


def show_google_search(lat: float, lon: float) -> str:
    google_link = f"https://www.google.com/maps/search/tennis+court/@{lat},{lon},14z"

    return f"""🎾 Search tennis courts:

🔍 Google Maps search:
{google_link}

"""