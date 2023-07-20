# from pathlib import Path
# import re

# def get_info ():
#     directory = "_inputfiles/D3SeqFiles"
#     find_units_algo("agehdr_unit.h")
#     files = Path(directory).glob('*')
#     for filename in files:
#         print(filename)
#         ##the code below captures the part of the file that includes runit, unit, and common
#         openFile = open(filename, "r")
#         lines = openFile.readlines()
#         for line in lines:
#             pName = re.findall("(?<=PROGRAM NAME:).*$", line)
#         if pName != []:
#             print("PROGRAM NAME:",pName[0])
#         val = find_units_algo(str(filename))
#         print("og:", val)
#         if("." in val):
#             print("going into the include:")
#             find_units_algo(val)







#mini save because I am making changes

from pathlib import Path
import re

directory = "_inputfiles/D3SeqFiles"
files = Path(directory).glob('*')
filesFound = []
found = []
count = 0
for filename in files:
    print(filename)
    ##the code below captures the part of the file that includes runit, unit, and common
    file_path = filename
    openFile = open(filename, "r")
    lines = openFile.readlines()
    with open(file_path, "r") as file:
        text = file.read()
    for line in lines:
        pName = re.findall("(?<=PROGRAM NAME:).*$", line)
        if pName != []:
            print("PROGRAM NAME:",pName[0])
    pattern = r'DEFINE UNITS(.*?);=+'
    matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
    if matches == []:
        pattern = r'define units(.*?);=+'
        matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
    if matches == []:
        pattern = r'Define Units(.*?);=+'
        matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
    if matches == []:
        pattern = r'DEFINE(.*?);=+'
        matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
    if matches != []:
        iHolder = 0
        #print(matches)
        for i in range(len(matches[0][0::])):
            if(matches[0][(i):i+1] == "*" or matches[0][(i):i+1] == "="):
                iHolder = i
                break
        newStr = matches[0][0:iHolder]
        #print(newStr)

        ##the code below now captures every line that is not a comment
        newStr = iter(newStr.splitlines())
        holder = []
        for line in newStr:
            commonPat = r'^(?![ ]*;)([^;]*)' #when there is a line with no semi colon at the start capture it
            comm = re.findall(commonPat, line)
            # print("comm:",comm)
            for match in comm:
                #print(match.strip())
                holder.append(match.strip())

        holder = [x for x in holder if x != '']#remove empty strings
        print("holder", holder)

        ##the code below sorts everything that is taken and prints it and output area
        unit = holder
        runit = []
        common = []
        
        for i in holder:
            if("UNIT" in i and "RUNIT" not in i):
                unit.append(i[10::])
            if("RUNIT" in i):
                runit.append(i[6::])
            if("COMMON" in i):
                common.append(i[7::])
        if unit != []:
            print("Unit:", unit[0])
        if runit != []:
            print("RUNIT:", runit[0])
        if common != []:
            print("COMMON:", common[0])
        count += 1
        print(count)
    
        
# def find_units_algo(file):
#     fileName = ""
    
#     if (file[0:10:1] == "_inputfile"):
#         fileName = Path(file)
#         # openFile = open(fileName, "r")
#         # lines = openFile.readlines()
#         with open(fileName, "r") as file:
#             text = file.read()
#         #print("in here")
#         pattern = r'DEFINE UNITS(.*?);=+'
#         matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
        
#         if matches == []:
#             pattern = r'define units(.*?);=+'
#             matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
#         elif matches == []:
#             pattern = r'Define Units(.*?);=+'
#             matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
#         elif matches == []:
#             pattern = r'DEFINE(.*?);=+'
#             matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
#         elif matches == []:
#             pattern = r';\s*define units\n([\s\S]+?);\*\*'
#             matches = re.search(pattern, text)
#         # print("match", matches)
#     else:
#         # print("or here")
#         fileName = Path("_inputfiles/D3_H_IncFiles/"+ file)
#         with open(fileName, "r") as file:
#             text = file.read()
#         pattern = r'UNIT [\s\S]*?;\*'
#         matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
#         print(fileName)
    
    

#     print(matches)
#     if matches != []:
#         iHolder = 0
#         #print(matches)
#         for i in range(len(matches[0][0::])):
#             if(matches[0][(i):i+2] == ";*" or matches[0][(i):i+2] == ";="):
#                 iHolder = i
#                 break
#         newStr = matches[0][0:iHolder]
#         #print(newStr)

#         ##the code below now captures every line that is not a comment
#         newStr = iter(newStr.splitlines())
#         holder = []
#         for line in newStr:
#             commonPat = r'^(?![ ]*;)([^;]*)'
#             comm = re.findall(commonPat, line)
#             #print(comm)
#             for match in comm:
#                 #print(match.strip())
#                 holder.append(match.strip())

#         holder = [x for x in holder if x != '']#remove empty strings
#         print("holder", holder)

#         ##the code below sorts everything that is taken and prints it and output area
#         unit = holder
#         runit = []
#         common = []
        
#         for i in holder:
#             if("UNIT" in i and "RUNIT" not in i):
#                 unit.append(i[10::])
#             if("RUNIT" in i):
#                 runit.append(i[6::])
#             if("COMMON" in i):
#                 common.append(i[7::])
#             if("#include" in i):
#                 include = re.findall("(?<=#include <)(.*?)(?=>)", i)

#                 print("include:", include)

#         if unit != []:
#             print("Unit:", unit[0])
#         if runit != []:
#             print("RUNIT:", runit[0])
#         if common != []:
#             print("COMMON:", common[0])
#         # count += 1
#         # print(count)
#         return unit[0]
# # include_units("agehdr_unit.h")
# get_info()
#########################################trial#########################################
# from pathlib import Path
# import re

# directory = "some_input_files"
# files = Path(directory).glob('*')
# filesFound = []
# found = []
# for filename in files:
#     openFile = open(filename, "r")
#     lines = openFile.readlines()
#     commCount = 0
#     #unitCount = 0
#     unitArr = []
#     for line in lines:
#         pName = re.findall("(?<=PROGRAM NAME:   ).*$", line)
#         include = re.findall("(?<=#include).*", line)
#         unit = re.findall("(?<=UNIT ).*$", line)
#         comm = re.findall("(?<=COMMON ).*$", line)
#         runit = re.findall("(?<=RUNIT ).*$", line)
#         H = re.findall("(?<=#include <)(.*?)(?=.h>)", line)
#         if pName != []:
#             print("PROGRAM NAME:",pName)
#             found.append(True)
#         else:
#             found.append(False)
#         if comm != [] and commCount == 0:
#             print("COMM OG:", comm)
#             commCount +=1
#             found.append(True)
#         else:
#             found.append(False)
#         if (runit != []):
#             print("runit:", runit)
#             found.append(True)
#         else:
#             found.append(False)
#         if (unit != []):
#             #print("Program Name:", pName)
#             # print()
#             # unitArr.append(unit)
#             found.append(True)
#             #unitCount += 1
#         else:
#             found.append(False)
#         # if unit != [] and runit != []:
#         #     print("Unit:",unitArr)
#         #     found.append(True)
#         #     #print("filename:", filename)
#         # else:
#         #     found.append(False)
#         if H != []:
#             print("H:", H)
#             found.append(True)
#         else:
#             found.append(False)
#         if include != []:
#             print("Include:", include)
#             found.append(True)
#             # filesFound.append(filename)
#         else:
#             found.append(False)
#     if(False not in found):
#         filesFound.append(filename)
#         print("file:", filename)
            
#     print("filename:", filename)
#     commCount = 0
#     #unitCount = 0

# print(filesFound)
