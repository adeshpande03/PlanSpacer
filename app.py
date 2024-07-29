from flask import Flask, render_template, request
from utils import get_nearby_activities, calculate_travel_times, find_best_activity
from config import config
from pprint import pprint

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", google_maps_api_key=config.GOOGLE_MAPS_API_KEY)


@app.route("/results", methods=["POST"])
def results():
    activity = request.form["activity"]
    user_address = request.form["user_address"]
    friend_addresses = request.form.getlist("friend_addresses")

    activities = get_nearby_activities(user_address, activity)

    if "error" in activities:
        return render_template(
            "index.html",
            error=activities["error"],
            google_maps_api_key=config.GOOGLE_MAPS_API_KEY,
        )

    travel_times = calculate_travel_times(user_address, friend_addresses, activities)

    formatted_travel_times = []
    for activity in activities["results"]:
        activity_location = activity["geometry"]["location"]
        activity_name = activity["name"]
        activity_address = activity["vicinity"]
        times = travel_times.get(activity_address, [])

        formatted_travel_times.append(
            {
                "activity": {
                    "name": activity_name,
                    "vicinity": activity_address,
                    "location": activity_location,
                },
                "driving_times": times,
                "gmaps_link": f"https://www.google.com/maps/dir/?api=1&destination={activity_location['lat']},{activity_location['lng']}",
            }
        )
    best_activities = find_best_activity(formatted_travel_times)

    return render_template(
        "results.html",
        best_activities=best_activities,
        google_maps_api_key=config.GOOGLE_MAPS_API_KEY,
        friend_addresses=friend_addresses,
        user_address=user_address,
        zip=zip,
    )


if __name__ == "__main__":
    app.run(debug=True)
