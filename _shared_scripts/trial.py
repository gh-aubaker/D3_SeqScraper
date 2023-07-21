import re
from pathlib import Path
import time
import json
import samplePaths
global unit_boo 
unit_boo = False
global common_boo
common_boo = False
global runit_boo
runit_boo = False
global final
final = []
global count
count = 0
global file_l
file_l = []
global p_name
p_name = ""
global p_bool
p_bool = False
global include
include = []
global fileName
fileName = ""
global newFile_bool
newFile_bool = False
global inc_file
inc_file = ""
global overall
overall = []

def get_p_name(line):
    global p_name
    p_pat = samplePaths.grab_regex()[0]
    p_match = re.findall(p_pat, line, re.IGNORECASE)
    if p_match != []:
        p_name = p_match[0]

def getFile(str):
    global file_l
    global count
    global newFile_bool
    newFile_bool = True
    count += 1
    if(".h" in str.lower()):
        fileCopy = samplePaths.grab_new_path(str)[0]
    if(".inc" in str.lower()):
        fileCopy = samplePaths.grab_new_path(str)[1]
    file_l.append(fileCopy)
    return fileCopy

def checkContent(line):
    global unit_boo
    holder = []
    u_pat = samplePaths.grab_regex()[1]
    u_match = re.findall(u_pat, line, re.IGNORECASE)
    c_pat = samplePaths.grab_regex()[2]
    c_match = re.findall(c_pat, line, re.IGNORECASE)
    r_pat = samplePaths.grab_regex()[3]
    r_match = re.findall(r_pat, line, re.IGNORECASE)
    
    for i in u_match:
        holder.append(i)
    for i in c_match:
        holder.append(i)
    for i in r_match:
        holder.append(i)
    return holder
def getContent(line):
    global unit_boo
    global common_boo
    global runit_boo
    global final
    holder = checkContent(line)
    l = []
    if holder != []:
        for i in holder:
            if "unit" in i.lower() and "runit" not in i.lower():
                l.append(i)
                unit_boo = True
            if ("common" in i.lower()):
                l.append(i)
                common_boo = True
            if "runit" in i.lower():
                l.append(i)
                runit_boo = True
    if(l != []):
        if l not in final:
            final.append(l)
    return l
def include_check(line):
    if ("#include" in line and unit_boo == False):
        inc_pat = samplePaths.grab_regex()[4]
        inc_match = re.findall(inc_pat, line, re.IGNORECASE)
        new_file = getFile(inc_match[0])
        return new_file
    else:
        return ""
def test(file):
    global unit_boo
    global common_boo
    global runit_boo
    global final
    global count
    global inc_file
    inc_file = file
    try:
        openFile = open(file, "r")
        lines = openFile.readlines()
    except OSError:
        return "link didnt work"
    
    num = 0
    check = []
    include = ""
    for line in lines:
        get_p_name(line)
        inlclude_add(line)
        if "/*" in line:
            num += 1
        if "*/" in line:
            num += 1
            slash_mat = re.findall(samplePaths.grab_regex()[5], line)
            if slash_mat != []:
                check = slash_mat
            
        if num%2 == 0:
            if check != []:
                if "#include" in check[0] and unit_boo == False:
                    include = include_check(check[0])
                    test(include)
                    return
                else:
                    getContent(check[0])
            
            getContent(line)
            include = include_check(line)
            if(include != ""):
                test(include)
                return
           

def cleanup(list, bool):
    global p_name
    temp_list = []
    for i in list:
        if i not in temp_list:
            temp_list.append(i[0])
    if bool == False:
        temp_list.append(p_name)
    for i in range (len(temp_list)):
        if ";" in temp_list[i]:
            semi = temp_list[i].find(";")
            temp_list[i] = " ".join(temp_list[i][0:semi].split())
        if "*" in temp_list[i]:
            star = temp_list[i].find("*")
            temp_list[i] = " ".join(temp_list[i][0:star].split())
        if "program name:" in temp_list[i].lower():
            if "/*" in temp_list[i]:
                slash_star = temp_list[i].find("/*")
                temp_list[i] = " ".join(temp_list[i][0:slash_star].split())
                p_name = temp_list[i]
        elif "/" in temp_list[i]:
            slash = temp_list[i].find("/")
            temp_list[i] = " ".join(temp_list[i][0:slash].split())
    return temp_list

def inlclude_add(line):
    global include
    if "#include" in line:
        inc_pat = samplePaths.grab_regex()[6]   
        inc_mat = re.findall(inc_pat, line, re.IGNORECASE)
        if inc_mat != []:
            include.append(inc_mat[0])

global h_boo
h_boo = False
global inc_boo
inc_boo = False

def get_file_name(str):
    slash_count = 0
    for i in range (len(str)):
        if ("\\" in str[i:i+1]):
            slash_count = i
    return str[slash_count+1::]

def dict_convert(list):
    global common_boo
    global runit_boo
    global fileName
    global newFile_bool
    name = get_file_name(str(fileName))
    dict = {}
    p = False
    dict[name] = {'PROGRAM NAME:': [],
                  'UNIT:' : [],
                  'COMMOM:' : [],
                  'RUNIT:' : [],
                  'INC:' :[],
                  'H:' : [],
                'newFile_bool:': False}
    
    dict[name]["newFile_bool:"] = newFile_bool
    if list == []:
        return dict
    for i in list:
        if("program name:" in i.lower()):
            dict[name]["PROGRAM NAME:"].append(i[13::])
            p = True
        if("unit" in i.lower() and "include" not in i.lower() and "runit" not in i.lower()):
            dict[name]['UNIT:'].append(i[4::])
        if("common" in i.lower() and p == False):
            dict[name]["COMMOM:"].append(i[6::])
        if("runit" in i.lower()):
            dict[name]["RUNIT:"].append(i[5::])
        if("include" in i.lower() and ".inc" in i.lower()):
            dict[name]["INC:"].append(i[9::])
        if("include" in i.lower() and ".h" in i.lower()):
            dict[name]["H:"].append(i[9::])
    return dict

if __name__ == '__main__':
    start = time.time()
    print("start timer")
    dict_list = [samplePaths.grab_dict_path()[0], samplePaths.grab_dict_path()[1], samplePaths.grab_dict_path()[2]]
    overallCount = 0
    for directory in dict_list:
        files = Path(directory).glob('*')
        print(files)
        for fileName_in in files:
            overallCount += 1
            unit_boo = False
            runit_boo = False
            common_boo = False
            p_bool = False
            newFile_bool = False
            include = []
            p_name = ""
            count = 0
            final = []
            file_l = []
            newFile = ""
            escaped = str(fileName_in)
            for j in range (len(escaped)):
                if escaped[j]  == "\\":
                    newFile += "\\\\"
                else:
                    newFile += escaped[j]
            test(Path(escaped))
            final = cleanup(final, False)
            overallCount += count
            if newFile_bool == True:
                fileName = inc_file
                newFile_bool = False
                final.append(p_name)
                add_dict = dict_convert(final)
                if add_dict not in overall:
                    overall.append(add_dict)
                    newFile_bool = True
                fileName = fileName_in
                add_dict = dict_convert(include)
                if add_dict not in overall:
                    overall.append(add_dict)
            else:
                final = final + include
                fileName = fileName_in
                dict_holder = dict_convert(final)
                if dict_holder not in overall:
                    overall.append(dict_holder)
    with open("overall.json", "w") as fp:
        json.dump(overall, fp, indent=6)
    print("DONE; TIME TAKEN:", time.time()-start, "SECS TO RUN;", overallCount, "NUM OF FILES ACESSED")