# rootkit
Purpose
8505’s final project purpose is to create a rootkit with a C&C (command and control) system. This system will be capable of:
-Starting/Stopping a keylogger
-File transfer from victim to attacker
-Start/Stop watching a file for changes
-Start/Stop watching a directory for changes

Installing

Command Modules
pip install cryptography
pip install scapy

Rkit Modules
pip install watchdog
pip install keyboard
pip install setproctitle
pip install cryptography
pip install scapy

Running
python3 command.py
python3 receiver.py
python3 rkit.py

Limitations
-To receive any output from the rootkit, receiver must be running
-The rootkit will function regardless if the receiver is running or not
-Only one instance of file watch or directory watch can exist at once
-The current watch must be stopped before a new one is started



