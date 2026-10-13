# Simple Transfer Server

A simple single-file executable for launching a SMB 1.0 server for air-gapped file transfers between old and new computers.

Simply download the appropriate server binary from the releases page and run as administrator to begin. The shared folder is located on the user's desktop by default.

# Basic Configuration

Start by connect the two computers together via ethernet. Take note of which NIC (network interface card) is used on both systems. The IP address configurations must happen on the corresponding NIC to work.

Configure the Host PC (the new one running the server) to have a static IPv4 address of `192.168.77.1`. Similarly, configure the Client PC (the old one to transfer files off of) to have a static IPv4 address of `192.168.77.2`.

If these address conflict with any existing networks, this can be changed in `server.py` but will require re-compilation (or running the script directly).

## Host PC

Check what is already running on port:
- Unix: `sudo lsof -nP -i :445`
- Windows: `netstat -ano | findstr :445`

Disable native use of port 445:
- MacOS: `sudo launchctl disable system/com.apple.smbd`
- Windows: `sc config lanmanserver start= disabled`

## Client PC

Map shared drive:
- Windows XP: `net use Z: \\192.168.99.1\DATA`

Delete shared drive:
- Windows XP: `net use Z: /delete`


## Special notes:
It may be required on Windows to disable `Disable NetBIOS over TCP/IP` (since it will try to connect over port 139).