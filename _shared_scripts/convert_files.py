import os
from pathlib import Path
# import shutil

# # directory = "_inputfiles\D3_H_IncFiles"
# # files = Path(directory).glob('*')
# # for filename in files:
# #     og_path = str(filename)
# #     # new_path = ""
# #     print(directory)
# #     print(og_path)
# #     idx = og_path.find("D3_H_IncFiles")
# #     print(idx)
# #     idx = idx + 14
# #     print(idx)
# #     fileName = og_path[idx::] 
# #     print("filename:", fileName)
# #     print (og_path[0:idx:])
# #     if(".h" in og_path.lower()):
# #         h_txt_name = og_path[idx:-2:] + "_h.SEQ"
# #         print(h_txt_name)
# #         new_path = os.path.join("_inputfiles\h_files", h_txt_name)
# #         print("newH", new_path)
# #         shutil.move(og_path, new_path)
# #     elif(".inc" in og_path.lower()):
# #         txtName = fileName[0:-4] + "_inc.txt"
# #         print("txtName", txtName)
# #         new_path = os.path.join("_inputfiles\incFile", txtName)
# #         print("new", new_path)
# #         shutil.move(og_path, new_path)
# #         # new_path = og_path[0:idx:] + "h_files\\" + fileName[0:-4] + "_inc.txt"
# #     else:
# #         print("backup")

# #     # print ("done:",new_path)

import pandas as pd

# student = {"PROGRAM NAME:": "sadsajkdhkjahsdjkha","info" :[{"Name": "Vishvajit Rao", "age": 23, "Occupation": "Developer","Language": "Python"}], "hello": "world"}

# # convert into dataframe
# df = pd.DataFrame(data=student, index=[1])

# #convert into excel
# df.to_csv("students.csv", index=False)
# print("Dictionary converted into excel...")

dct = {1: [0, 120, 115, 100, 91, 131, 74, 14, 8, 105, 122, 47, 103, 0], 
       2: [0, 107, 25, 26, 121, 118]}

# define the second column name as "values"
df = pd.DataFrame({'values': dct}).reset_index() 
# rename the first colum, here "keys"
df.rename(columns={"index": "keys"}, inplace = True)
# save dataframe to excel file
df.to_csv("output.csv")  

# directory = "_inputfiles\D3SeqFiles\ALDOXSC.SEQ"
# # files = Path(directory).glob('*')
# og_path = str(directory)
# # new_path = ""
# print(directory)
# print(og_path)
# idx = og_path.find("h_files")
# print(idx)
# idx = idx+8
# print(idx)
# fileName = og_path[idx::] 
# print("filename:", fileName)
# print (og_path[0:idx:])
# if("_h" in og_path.lower()):
#     h_txt_name = og_path[idx:-2:] + "_h.SEQ"
#     print(h_txt_name)
#     new_path = os.path.join("_inputfiles\h_files", h_txt_name)
#     print("newH", new_path)
#     shutil.move(og_path, new_path)
# elif(".inc" in og_path.lower()):
#     txtName = fileName[0:-4] + "_inc.txt"
#     print("txtName", txtName)
#     new_path = os.path.join("_inputfiles\incFile", txtName)
#     print("new", new_path)
#     shutil.move(og_path, new_path)
#     # new_path = og_path[0:idx:] + "h_files\\" + fileName[0:-4] + "_inc.txt"
# else:
#     print("backup")

# # print ("done:",new_path)