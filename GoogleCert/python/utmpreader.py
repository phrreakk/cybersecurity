# Read in a utmp file for hackthebox
import utmp

with open("..\..\..\..\htb\wtmp", 'rb') as file:
    buf = file.read()
    for entry in utmp.read(buf):
        print(entry.time, entry.type, entry)
