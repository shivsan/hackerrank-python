import googlemaps
import requests

api_key = "AIzaSyDkkXIG7RPsrmEnU0_oppecx7XvFKcmyPY"
gmaps = googlemaps.Client(key=api_key)

def getPlace(placeName: str) -> str:
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key=" + api_key

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.candidates[0].name

# Declarativeness
def getShortestDistance(destinationInput: str, sourceText: str) -> str:
    destinationCanonicalName = getPlace(destinationInput)
    sourceCanonicalName = getPlace(sourceText)

    shortestDistance = gmaps.distance_matrix(destinationCanonicalName, sourceCanonicalName)['rows'][0]['elements'][0]

    return shortestDistance

