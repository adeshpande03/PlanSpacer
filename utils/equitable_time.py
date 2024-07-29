import numpy as np


def find_best_activity(travel_times):
    """
    This function takes a list of travel times for each activity and finds the top three
    activities that have the most equitable driving times.

    travel_times is a list of dictionaries, each containing:
    {
        'activity': activity,
        'driving_times': [time1, time2, ..., timeN]
    }
    """

    def calculate_variance(times):
        return np.var(times)

    def calculate_average(times):
        return np.mean(times)

    activities_with_scores = []

    for activity in travel_times:
        driving_times = activity["driving_times"]
        variance = calculate_variance(driving_times)
        average = calculate_average(driving_times)
        activities_with_scores.append(
            {
                "activity": activity["activity"],
                "variance": variance,
                "average": average,
                "driving_times": driving_times,
                "gmaps_link": activity.get("gmaps_link"),
            }
        )

    # Sort first by variance, then by average time
    sorted_activities = sorted(
        activities_with_scores, key=lambda x: (x["variance"], x["average"])
    )

    # Return the top three activities
    return sorted_activities
