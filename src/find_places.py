# Libs
import googlemaps
from flask import jsonify
from credentials import google_maps_key

# Codes for types of places
CODES = {
  "HALAL_RESTAURANTS": 1,
  "HALAL_GROCERY": 2,
  "MOSQUES": 3,
  "GENERAL_CLOTHING": 4,
  "BUS_STATIONS": 5,
  "BANKS": 6,
  "GOVERNMENT_OFFICES": 7,
  "HOUSING_ASSISTANCE": 8,
  "PARKS": 9,
  "ISLAMIC_CLOTHING": 10,
  "MEDICAL": 11,
}

QUERIES = {
  CODES["HALAL_RESTAURANTS"]: "islamic restaurants",
  CODES["HALAL_GROCERY"]: "halal grocery",
  CODES["MOSQUES"]: "mosque",
  CODES["GENERAL_CLOTHING"]: "clothing",
  CODES["BUS_STATIONS"]: "bus station",
  CODES["BANKS"]: "banks",
  CODES["GOVERNMENT_OFFICES"]: "government offices",
  CODES["HOUSING_ASSISTANCE"]: "housing assistance",
  CODES["PARKS"]: "parks",
  CODES["ISLAMIC_CLOTHING"]: "islamic clothing",
  CODES["MEDICAL"]: "urgent care",
}

# Google maps stuff
client = googlemaps.Client(key=google_maps_key())

def _find_places_path(request):
  try:
    # Get the data from the request
    code = request.json["code"]
    location = request.json["location"]

    # Choose a query for the api based on the code sent
    if code not in QUERIES:
      raise "Not yet implemented"
    query = QUERIES[code]

    # Get the results
    results = client.places(
      query,
      location=location,
    )["results"]

    # Return the results
    return jsonify(results)
  except:
    # If there is any errors return 400
    return "", 400