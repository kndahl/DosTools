import time
import random
import socket
import sys

def process(ip, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    msg = bytes(random.getrandbits(10))
    timeout = time.time() + int(duration)
    sent_packets = 0

    while time.time() < duration:
        port = random.randint(1025, 65356)
        sock.sendto(msg, (ip, port))
        sent_packets += 1

def main(args):
    ip = args[1]
    duration = args[2]
    process(ip, duration)

main(sys.argv)