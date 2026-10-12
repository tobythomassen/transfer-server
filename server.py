import sys
import errno
import logging
import pathlib
from impacket.smbserver import SimpleSMBServer

IP = "192.168.99.1"
PORT = 445
SHARE = "DATA"
FOLDER = pathlib.Path.home() / "Desktop" / "Shared Data"
FOLDER.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s  %(levelname)-7s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(FOLDER / "LOG.txt", encoding="utf-8"),
    ],
)
logging.getLogger("impacket.smbserver").setLevel(logging.DEBUG)

# Attempt to create server
try:
    server = SimpleSMBServer(listenAddress=IP, listenPort=PORT)
except OSError as e:
    if e.errno == errno.EACCES:
        sys.exit(f"Port {PORT} is unavailable without elevated permissions.")
    if e.errno == errno.EADDRINUSE:
        sys.exit(f"Port {PORT} is already in use.")
    if e.errno == errno.EADDRNOTAVAIL:
        sys.exit(f"IP address {IP} is not available.")
    raise

# Share data folder
server.addShare(SHARE, str(FOLDER), "")
server.setSMB2Support(False)

# Start server
logging.info(
    "Serving %s as \\\\%s\\%s on port %s",
    FOLDER,
    IP,
    SHARE,
    PORT,
)
server.start()
