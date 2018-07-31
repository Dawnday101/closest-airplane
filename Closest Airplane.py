//The program finds the closest airborne airplane to any
 position in North America or Europe using an API that gives 
 us all the date on currentlly airborne commercial planes in the region.//
 
import urllib.request, json
from math import acos, sin, cos, radians
with urllib.request.urlopen(https://opensky-network.org/api/states/all")
as url:
    data = json.loads(url.read().decode())
['states']

EARTH_RAD = 6371
def point_dist(x, y):
    xrad = [radians(d) for d in x]
	yrad = [radians(d) for d in y]
	return
EARTH_RAD*acos(sin(xrad[0])*sin(yrad[0])+ 
cos(xrad[0])*cos(yrad[0])*cos(abs(xrad[1]-
yrad[1])))

def get_closest(longitude, latitude):
    closest = data[0], 10000000
	for plane in data:
		if None in plane[5:7]: continue
		dist = point_dist(plane[5:7],
[longitude, latitude])
		if dist<closest[1]:
			closest = plane, dist
	print("closest plane to "longitude, "E", 'latitude, "N",)
	print("Geodesic distance:',
closest[1])
	print(Callsign:", closest[0][1])
	print("Longitude and Latitude:",
closest[0][5], "E", closest[0][6], "N")
	print("Geometric Altitude:", closest[0][7])
	print("Country of Origin:", closest[0][2])
	print("ICA024 ID:", closest