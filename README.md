# Dubins Path Simulator
Algorithm for finding the optimal path of UAS drone given turning radius and waypoint coordinates  

## What it does
### dubins\.py:
Generates a series of GPS coordinates (latitude/longitude) that map out the Dubins path between two inputted GPS coordinates and headings (in degrees):

For example, inputting the following:
```Enter drone latitude: 49.263410
Enter drone longitude: -123.238651
Enter waypoint latitude: 49.263275
Enter waypoint longitude: -123.238456
Enter drone bearing (in degrees): -167.3
Enter waypoint bearing (in degrees): 23.1
```

Outputs the following list of GPS coordinates:
```
49.26340999999999, -123.238651
49.26340161316977, -123.23867810471107
49.26338646973052, -123.23869716975376
49.263367454224436, -123.23870456360221
49.26334818874659, -123.23869887788112
49.26333234300304, -123.23868119562559
49.263322935302654, -123.23865488497394
49.26327500000001, -123.238456
49.263261159225195, -123.23848337857115
49.26324034065914, -123.23849697786683
49.26321782433831, -123.23849334883079
49.26319932087951, -123.23847341188457
49.26318952314724, -123.23844222346918
49.26319091604964, -123.2384076936174
49.26320314631782, -123.23837857981358
49.26322311210169, -123.23836226592925
49.26324574965922, -123.23836288952451
49.26326531762369, -123.23838029246348
49.26327685313685, -123.23841006100086
```

<div align="center" markdown="1">
  
  <br>
  <img src="https://github.com/nuggetbucket54/dubins-path-sim/assets/55860775/cc1e555f-7f63-4135-9a10-b3d42fd3e779" width="400"/> <br>
  The above GPS coordinates plotted on a map

</div>

### dubins_graph\.py:
Randomly generates a theoretical drone/waypoint position/orientation and calculates the optimal Dubins path. New waypoints can be generated by the user, in which the drone will be updated to the previous waypoint's position & orientation. Slider exists to play around with minimum turning radius

<div align="center" markdown="1">

![dubin](https://github.com/nuggetbucket54/dubins-path-sim/assets/55860775/b1d658a1-8c49-439b-abb9-1a17e45e979b)

</div>

## About Dubins paths
- [Dubins paths](https://en.wikipedia.org/wiki/Dubins_path) are the shortest path from one orientation & position to another orientation & position for a vehicle that can only move forward and also has a minimum turning radius
- Here's a good visualization: https://www.youtube.com/watch?v=fEImNJQ3hUM 
- Two types of Dubin's paths: CSC (curve + straight line + curve) and CCC (curve + curve + curve)

  <div align="center" width="500">
    <img src="https://github.com/nuggetbucket54/dubins-path-sim/assets/55860775/8a815619-61e1-4907-a719-fdaa727f8dc8" width="500"/>
  </div>

<!--
## The math involved (only look at it if you really want to)
![math](https://github.com/nuggetbucket54/dubins-path-sim/assets/55860775/4179f301-8559-4ab7-ad4d-7a613d1ff790)
--->
