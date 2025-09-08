# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:05:31 2025

@author: cirze
"""

#Job Scheduling
def max_element(deadline):
    if len(deadline)==0:
        return 0
    return max(deadline)

def job_scheduling(jobs,deadline,profit):
    combined=list(zip(jobs,deadline,profit))
    combined.sort(key=lambda x:x[2],reverse=True)
    
    max_deadline=max_element(deadline)
    slots=[-1]*max_deadline
    selected_jobs=[]
    
    for job, dl, pr in combined:
        for i in range(min(dl,max_deadline)-1,-1,-1):
            if slots[i]==-1:
                slots[i]=job
                selected_jobs.append(job)
                break
    return selected_jobs
                
    
jobs=['A','B','C','D','E','F']
deadline=[2,1,3,1,2,1]
profit=[100,20,35,27,30,28]
res=job_scheduling(jobs, deadline, profit)
print(res)