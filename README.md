# rootkit
## Purpose

8505’s final project purpose is to create a rootkit with a C&C (command and control) system. This system will be capable of:

- Starting/Stopping a keylogger
- File transfer from victim to attacker
- Start/Stop watching a file for changes
- Start/Stop watching a directory for changes


## Installing

### Command Modules
```
pip install cryptography
pip install scapy
```

### Rkit Modules
```
pip install watchdog
pip install keyboard
pip install setproctitle
pip install cryptography
pip install scapy
```

## Running
```
python3 command.py
python3 receiver.py
python3 rkit.py
```

## Limitations

- To receive any output from the rootkit, receiver must be running
- The rootkit will function regardless if the receiver is running or not
- Only one instance of file watch or directory watch can exist at once
- The current watch must be stopped before a new one is started

## Documentation
- [Report](https://docs.google.com/document/d/17NWaDPMvG8lsnzjp-fAs6lRr7EwbuBFzMtBFpkY0mb0/edit?usp=sharing)
- [Design](https://docs.google.com/document/d/1mzj84zZmFBkI-RDPmchlk96TIwZ1pGOF92H6OW_JssY/edit?usp=sharing)
- [Testing](https://docs.google.com/document/d/1St9zNfmGDppEs5FzQaNFFPESn9hlpM7H7eMsbBwq6uQ/edit?usp=sharing)
- [User Guide](https://docs.google.com/document/d/1ZajTX9TB9Q7dEOJuAROxDHCnbdgvEkQXgs8tyEogouQ/edit?usp=sharing)

