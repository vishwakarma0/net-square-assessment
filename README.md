# Fair Billing log parser

### Overview
This program generates a report of users, the number of sessions, and the minimum possible total duration of their sessions in seconds, based on usage data from a log file. The application provider charges for the use of its application by the duration of sessions, with a charge per second of usage.

### Usage
The program takes a single command line parameter, which should be the path to the data file to read. The data in the input should be correctly ordered chronologically, and all records in the file will be from within a single day (i.e., they will not span midnight).

To run the program, execute the following command:
```python
    python log_parser.py samplelog.txt
```

### Log File Format
The log file contains the following information for each session:

 * Time at which the session starts or stops (in the format HH:MM:SS)
 * Name of the user (a single alphanumeric string of arbitrary length)
 * Whether this is the start or end of the session (specified as either "Start" or "End")

Example:
```python
    14:02:03 ALICE99 Start
    14:02:05 CHARLIE End
    14:02:34 ALICE99 End
    14:02:58 ALICE99 Start
    14:03:02 CHARLIE Start
    14:03:33 ALICE99 Start
    14:03:35 ALICE99 End
    14:03:37 CHARLIE End
    14:04:05 ALICE99 End
    14:04:23 ALICE99 End
    14:04:41 CHARLIE Start
```

### Handling Invalid or Irrelevant Data
As with most log files, there may be other invalid or irrelevant data within the file. Therefore, any lines that do not contain a valid time-stamp, username, and a "Start" or "End" marker should be silently ignored and not included in any calculations.

### Assumptions
When there is an "End" with no possible matching start, the start time should be assumed to be the earliest time of any record in the file.
When there is a "Start" with no possible matching "End", the end time should be assumed to be the latest time of any record in the file.

### Output
The program generates a report of the users, the number of sessions, and the minimum possible total duration of their sessions in seconds, based on the data in the log file. The output is printed to the console in the following format:

```python
    name sessions duration
```

Example:
```python
    ALICE99 4 240
    CHARLIE 3 37
```
