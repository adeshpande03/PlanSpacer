import requests
from config import config

from pprint import pprint


def geocode_address(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": config.GOOGLE_MAPS_API_KEY}
    response = requests.get(url, params=params)
    geocode_result = response.json()

    if geocode_result["status"] == "OK":
        location = geocode_result["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        raise Exception(f"Geocoding failed: {geocode_result['status']}")


def get_nearby_activities(address, activity, radius=50):
    try:
        lat, lng = geocode_address(address)
    except Exception as e:
        return {"error": str(e)}

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lng}",
        "radius": radius * 1609.34,  # Convert miles to meters
        "keyword": activity,
        "key": config.GOOGLE_MAPS_API_KEY,
    }
    response = requests.get(url, params=params)
    return response.json()


def calculate_travel_times(user_address, friend_addresses, activities):
    addresses = [user_address] + friend_addresses
    travel_times = {}

    for activity in activities["results"]:
        activity_location = f"{activity['geometry']['location']['lat']},{activity['geometry']['location']['lng']}"
        url = "https://maps.googleapis.com/maps/api/distancematrix/json"
        params = {
            "origins": "|".join(addresses),
            "destinations": activity_location,
            "key": config.GOOGLE_MAPS_API_KEY,
        }
        response = requests.get(url, params=params)
        result = response.json()
        if result["status"] == "OK":
            times = [
                element["elements"][0]["duration"]["value"] // 60
                for element in result["rows"]
            ]
            travel_times[activity["vicinity"]] = times
        else:
            travel_times[activity["vicinity"]] = []

    return travel_times
