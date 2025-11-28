
import pandas as pd
from datetime import datetime, time
import time as t


data = [

    ("SUN", "06:30", "08:00", "Python for AI/ML", "Manaslu Lecture Hall", "Practical"),
    ("SUN", "09:00", "10:00", "Machine Learning Fundamentals", "T05 - Phewa", "Practical"),
    ("SUN", "10:00", "11:00", "Programming for Data Analysis", "Sagarmatha Hall", "Lecture"),
    ("SUN", "11:00", "12:30", "Systems Development Methods", "Makalu Hall", "Practical"),

    ("MON", "06:30", "07:30", "Systems Development Methods", "Sagarmatha Hall", "Lecture"),
    ("MON", "07:30", "08:30", "Object Oriented Development with Java", "T08 - Rupa", "Tutorial"),
    ("MON", "08:30", "10:00", "Technical Communication", "Sagarmatha Hall", "Lecture"),
    ("MON", "11:00", "12:00", "Programming for Data Analysis", "T02 - IPSpace", "Tutorial"),

    ("TUE", "06:30", "08:00", "System and Network Administration", "T08 - Rupa", "Tutorial"),
    ("TUE", "08:00", "09:00", "Systems Development Methods", "T05 - Phewa", "Tutorial"),
    ("TUE", "09:00", "10:30", "Programming for Data Analysis", "T01 - AlgoSpace", "Practical"),
    ("TUE", "11:30", "13:30", "Machine Learning Fundamentals", "T02 - IPSpace", "Practical"),

    ("WED", "06:30", "07:30", "System & Network Administration", "Saipal Hall", "Lecture"),
    ("WED", "07:30", "08:30", "Object Oriented Development with Java", "Saipal Hall", "Lecture"),
    ("WED", "09:00", "10:30", "Integrated Business Process with SAP", "T09 - Lhotse", "Practical"),
    ("WED", "11:00", "12:00", "Innovation Process", "Manaslu Hall", "Lecture"),

    ("THU", "06:30", "08:00", "OOP with Java", "T02 - IPSpace", "Practical"),
    ("THU", "08:00", "09:30", "Technical Communication", "Manaslu Hall", "Lecture"),
    ("THU", "10:30", "11:30", "ERP SAP System", "T09 - Lhotse", "Tutorial"),

    ("FRI", "06:30", "08:00", "System & Network Administration", "Makalu Hall", "Practical"),
    ("FRI", "08:00", "09:00", "Innovation Process", "Manaslu Hall", "Lecture"),
    ("FRI", "09:30", "10:30", "ERP SAP System", "Sagarmatha Hall", "Lecture"),
    ("FRI", "11:00", "12:30", "Python for AI/ML", "T04 - Rara", "Practical"),
]

df = pd.DataFrame(data, columns=["Day", "Start", "End", "Subject", "Room", "Type"])

df["Start"] = pd.to_datetime(df["Start"], format="%H:%M").dt.time
df["End"] = pd.to_datetime(df["End"], format="%H:%M").dt.time


day_map = {
    6: "SUN",
    0: "MON",
    1: "TUE",
    2: "WED",
    3: "THU",
    4: "FRI",
}





