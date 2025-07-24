# Auto Shutdown Scheduler

Auto Shutdown Scheduler is a simple desktop application built with Python and Tkinter that allows users to schedule automatic shutdowns of their computer. You can set a timer (in seconds) or specify an exact time (HH:MM) for the shutdown. The app also provides an option to cancel a scheduled shutdown.

## Features
- Schedule shutdown after a specified number of seconds
- Schedule shutdown at an exact time (HH:MM)
- Cancel a scheduled shutdown
- User-friendly graphical interface

## Requirements
- Python 3.x
- Tkinter (usually included with Python)

## How to Use
1. Run the script `Os project auto shutdown .py` using Python:
   ```bash
   python "Os project auto shutdown .py"
   ```
2. To schedule a shutdown after a certain number of seconds, enter the seconds and click "Schedule Timer".
3. To schedule a shutdown at a specific time, enter the hour and minute, then click "Schedule Exact Time".
4. To cancel a scheduled shutdown, click "Cancel Shutdown".

## Supported Platforms
- Windows
- Linux (shutdown commands may require root privileges)

## Note
- On Linux, you may need to run the application with appropriate permissions to execute shutdown commands.
- On Windows, the shutdown command works out of the box for most users. 