
# https://neetcode.io/problems/meeting-schedule?list=neetcode150

"""
Given an array of meeting time interval objects consisting of start and end times 
    [[start_1,end_1],[start_2,end_2],...],      where       (start_i < end_i),
determine if a person could add all meetings to their schedule without any conflicts.
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

def canAttendMeetings(intervals) -> bool:
    # line below needed for Neetcode solution
    # intervals = [(i.start, i.end) for i in intervals]

    # sort by meeting start
    sorted_meetings = sorted(intervals, key = lambda x: x[0])
    i = 0
    while i < len(intervals)-1:
        # check that start of next meeting is after or at start current meeting
        if sorted_meetings[i+1][0] < sorted_meetings[i][1]:
            return False
        i += 1
    return True

intervals = [(0,30),(5,10),(15,20)]
print(canAttendMeetings(intervals))
intervals = [(5,8),(9,15)]
print(canAttendMeetings(intervals))