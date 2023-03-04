import sys
from datetime import datetime, timedelta

# dictionary to store each user's session start and end times
sessions = {}
sessionsTime = {}

# variables to store the earliest and latest timestamps in the log file
earliest_time = datetime.max
latest_time = datetime.min

# parse the log file and update the sessions dictionary
with open(sys.argv[1], 'r') as f:
    for line in f:
        # extract the timestamp, username, and start/end marker from the line
        try:
            time_str, username, marker = line.strip().split()
        except ValueError:
            continue  # ignore invalid lines
        
        # parse the timestamp
        try:
                time = datetime.strptime(time_str, '%H:%M:%S')
        except ValueError:
            # Ignore irrelevants timestamp
            continue
        
        
        # update the earliest and latest timestamps
        if time < earliest_time:
            earliest_time = time
        if time > latest_time:
            latest_time = time
        
        sessions.setdefault(username, [])
        sessionsTime.setdefault(username, [])

        # update the sessions dictionary
        if marker == 'Start':
            sessions.setdefault(username, []).append(time)
        elif marker == 'End':
            if len(sessions[username]) == 0:
                duration = (time-earliest_time).total_seconds()
                if duration >= 0:
                    sessionsTime[username].append(duration)
            elif username in sessions:
                start_time = sessions[username].pop(0)
                duration = (time-start_time).total_seconds()
                if duration >= 0:
                    sessionsTime[username].append(duration)


for username, times in sessions.items():
    if len(sessions[username]):
        start_time = sessions[username].pop(0)
        duration = (latest_time-time).total_seconds()
        if duration >= 0:
            sessionsTime[username].append(duration)

# calculate the total duration and number of sessions for each user
for username, times in sessionsTime.items():
    total_duration = sum(times)
    num_sessions = len(times)
    print(f'{username} {num_sessions} {int(total_duration)}')