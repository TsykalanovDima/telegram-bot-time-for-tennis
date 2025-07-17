import requests
from datetime import datetime, timedelta

def merge_intervals(data: list[dict]) -> list[list[dict]]:
    if not data:
        return []
    intervals = []
    current = [data[0]]

    for i in range(1, len(data)):
        prev_dt = current[-1]["datetime"]
        curr_dt = data[i]["datetime"]
        if (curr_dt - prev_dt) == timedelta(hours=1):
            current.append(data[i])
        else:
            intervals.append(current)
            current = [data[i]]
    intervals.append(current)
    return intervals


def get_tennis_windows(lat: float, lon: float) -> str:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation,windspeed_10m",
        "timezone": "auto",
    }
    response = requests.get(url, params=params)
    data = response.json()

    times = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]
    precs = data["hourly"]["precipitation"]
    winds = data["hourly"]["windspeed_10m"]

    good = []
    acceptable = []

    for i in range(len(times)):
        dt = datetime.fromisoformat(times[i])
        if 6 <= dt.hour <= 21:
            temp = temps[i]
            rain = precs[i]
            wind = winds[i]

            info = {
                "datetime": dt,
                "temp": temp,
                "rain": rain,
                "wind": wind
            }

            if 15 <= temp <= 30 and rain < 0.4 and wind < 6:
                good.append(info)
            elif 13 <= temp <= 32 and rain < 1.0 and wind < 7:
                acceptable.append(info)

    message = ""

    def format_blocks(title, slots):
        if not slots:
            return ""
        result = f"{title}\n\n"
        intervals = merge_intervals(slots)
        for group in intervals:
            start_dt = group[0]["datetime"]
            end_dt = group[-1]["datetime"] + timedelta(hours=1)

            temp = group[0]["temp"]
            rain = group[0]["rain"]
            wind = group[0]["wind"]

            result += f"📅 {start_dt.strftime('%a %d.%m')}\n"
            result += f"🕒 {start_dt.strftime('%H:%M')}–{end_dt.strftime('%H:%M')}\n"
            result += f"🌡 {temp:.0f}°C   💧 {rain:.1f}mm   🌬 {wind:.1f} m/s\n\n"
        return result

    if good:
        message += format_blocks("🎾 Best time slots for tennis:", good)

    if acceptable:
        message += format_blocks("🟡 Acceptable but not ideal:", acceptable)

    if not message:
        return "❌ No suitable windows to play tennis in the coming days."

    return message.strip()
