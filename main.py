from fastapi import FastAPI
from pydantic import BaseModel
from dubins import dubin

app = FastAPI()

# waypoint object
class Waypoint(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    altitude: float

# object received from GCOM
class Item(BaseModel):
    current_waypoint: Waypoint
    desired_waypoint: Waypoint
    current_heading: float
    desired_heading: float

# converts calculated latitude/longitude into JSON format to match object
def create_item(lat, long, alt, count):
    return {
        "id": str(count),
        "name": "wp" + str(count),
        "latitude": str(lat),
        "longitude": str(long),
        "altitude": str(alt),
    }

@app.post("/")
async def root(item: Item):
    # get drone and waypoint positions
    print(item)
    drone = item.current_waypoint
    destination = item.desired_waypoint
    alt = drone.altitude
    waypoints = []

    drone_lat = drone.latitude
    drone_long = drone.longitude
    drone_angle = item.current_heading

    point_lat = destination.latitude
    point_long = destination.longitude
    point_angle = item.desired_heading

    # grab points of Dubins path
    points = dubin(drone_lat, drone_long, drone_angle, point_lat, point_long, point_angle)

    # turn all points into JSON objects
    count = 1
    for p in points:
        waypoints.append(create_item(p[0], p[1], alt, count))
        count += 1
    print(waypoints, flush=True)
    return waypoints