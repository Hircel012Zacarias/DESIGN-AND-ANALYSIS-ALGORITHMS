# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 08:03:36 2025

@author: cirze
"""

def activiy_selection(activity,start,end):
    combined = list(zip(activity, start, end))
    combined.sort(key=lambda x: x[2])
    
    selected_activities = [combined[0][0]]
    last_end_time = combined[0][2]
    
    for i in range(1, len(combined)):
        if combined[i][1] >= last_end_time: 
            selected_activities.append(combined[i][0])
            last_end_time = combined[i][2]
    
    return selected_activities

            
activity=['0','1','2','3','4']
start=[5,6,0,4,10]
end=[8,10,5,7,12]
res=activiy_selection(activity, start, end)
print(res)