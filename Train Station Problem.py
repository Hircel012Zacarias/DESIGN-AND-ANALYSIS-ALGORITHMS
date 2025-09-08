# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 21:20:17 2025

@author: cirze
"""

#Train Station Problem
def max_trains_stop(trains, n):
    # trains: list of tuples (arrival, departure, platform)
    from collections import defaultdict

    platforms = defaultdict(list)
    
    # Group trains by platform
    for arr, dep, plat in trains:
        platforms[plat].append((arr, dep))
    
    total = 0
    for plat in platforms:
        # Sort by departure time
        platforms[plat].sort(key=lambda x: x[1])
        
        count = 0
        last_dep = -1
        for arr, dep in platforms[plat]:
            if arr >= last_dep:
                count += 1
                last_dep = dep
        total += count
    
    return total


# Example input (converted to minutes for simplicity)
def to_minutes(t):  # "HH:MM" -> minutes
    h, m = map(int, t.split(":"))
    return h*60 + m

trains = [
    (to_minutes("10:00"), to_minutes("10:30"), 1),
    (to_minutes("10:10"), to_minutes("10:30"), 1),
    (to_minutes("10:00"), to_minutes("10:20"), 2),
    (to_minutes("10:30"), to_minutes("12:30"), 2),
    (to_minutes("12:00"), to_minutes("12:30"), 3),
    (to_minutes("09:00"), to_minutes("10:05"), 1)
]

print("Maximum stopped trains:", max_trains_stop(trains, 3))
