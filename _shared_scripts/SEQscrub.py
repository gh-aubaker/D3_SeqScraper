from pathlib import Path
import re

directory = "_inputfiles/D3Files"
files = Path(directory).glob('*')
filesFound = []

for filename in files:
    openFile = open(filename, "r")
    lines = openFile.readlines()
    for line in lines:
        result = re.findall("RUNIT", line)
        if result != []:
            filesFound.append(filename)









# REGEX CODE
# PROGRAM NAME: (?<=PROGRAM NAME:	).*$
# UUNIT: (?<=UNIT ).*$
