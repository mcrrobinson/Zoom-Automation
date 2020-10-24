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
    1: "Database Systems",
    2: "Programming",
    3: "Core Computing",
    4: "Architecture and Operating Systems",
    5: "Networks"
}

ENTRIES = {
    "Monday": {
        1: {
            "class_name": CLASS_MAP[1], 
            "meeting_time": [9,10], 
            "meeting_link": "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
        },
        2: {
            "class_name": CLASS_MAP[2],
            "meeting_time": [10,12],
            "meeting_link": ""
        },
        3: {
            "class_name": CLASS_MAP[3],
            "meeting_time": [12,13],
            "meeting_link": ""
        },
        4: {
            "class_name": CLASS_MAP[3],
            "meeting_time": [13,14],
            "meeting_link": ""
        },
        5: {
            "class_name": CLASS_MAP[4],
            "meeting_time": [16,17],
            "meeting_link": ""
        }
    },
    "Tuesday": {
        1: {
            "class_name": CLASS_MAP[4],
            "meeting_time": [11,12],
            "meeting_link": ""
        },
        2: {
            "class_name": CLASS_MAP[5],
            "meeting_time": [12,13],
            "meeting_link": ""
        },
        3: {
            "class_name": CLASS_MAP[1],
            "meeting_time": [15,16],
            "meeting_link": ""
        }
    },
    "Wednesday": {
        1: {
            "class_name": CLASS_MAP[5],
            "meeting_time": [12,13],
            "meeting_link": ""
        }
    },
    "Thursday": {
        1: {
            "class_name": CLASS_MAP[3],
            "meeting_time": [14,15],
            "meeting_link": ""
        },
        2: {
            "class_name": CLASS_MAP[2],
            "meeting_time": [17,18],
            "meeting_link": ""
        }
    },
    "Friday": {},
    "Saturday": {
        1: {
            "class_name": CLASS_MAP[1], 
            "meeting_time": [23,24], 
            "meeting_link": "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
        }
    }
}