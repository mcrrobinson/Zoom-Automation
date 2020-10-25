# THIS IS STATIC
WEEKDAYS = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}
CLASS_MAP = {
    1: "Art",
    2: "Geography",
    3: "Science"
}

ENTRIES = {
    "Monday": {
        1: {
            "class_name": CLASS_MAP[1], 
            "meeting_time": [9,10], 
            "meeting_link": "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=5453452341&pwd=c8j88912u391n8m2d98sumd98u1"
        },
        2: {
            "class_name": CLASS_MAP[2],
            "meeting_time": [10,12],
            "meeting_link": "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=5453452341&pwd=c8j88912u391n8m2d98sumd98u1"
        },
        3: {
            "class_name": CLASS_MAP[3],
            "meeting_time": [12,13],
            "meeting_link": "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=5453452341&pwd=c8j88912u391n8m2d98sumd98u1"
        }
    },
    "Tuesday": {
        1: {
            "class_name": CLASS_MAP[2],
            "meeting_time": [11,12],
            "meeting_link": "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=5453452341&pwd=c8j88912u391n8m2d98sumd98u1"
        },
    },
    "Wednesday": {
        1: {
            "class_name": CLASS_MAP[3],
            "meeting_time": [12,13],
            "meeting_link": "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=5453452341&pwd=c8j88912u391n8m2d98sumd98u1"
        }
    },
    "Thursday": {
        1: {
            "class_name": CLASS_MAP[1],
            "meeting_time": [14,15],
            "meeting_link": "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=5453452341&pwd=c8j88912u391n8m2d98sumd98u1"
        },
        2: {
            "class_name": CLASS_MAP[2],
            "meeting_time": [17,18],
            "meeting_link": "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=5453452341&pwd=c8j88912u391n8m2d98sumd98u1"
        }
    },
    "Friday": {},
}