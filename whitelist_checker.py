from os import walk, path
import os.path
import time
from typing import List, Optional
NAMEOFUSER = "random"
whitelist_list = 'whitelist.txt'
toolbox_folder = "C:\\Users\\" + NAMEOFUSER +\
                 r"\AppData\Local\Programs\TeraToolbox\mods"
whitelist_file = open(whitelist_list, "r")
whitelisted_hooks = []


def checker(check_path: str, hooks: List[str]) -> Optional[bool]:
    if not path.exists(check_path):
        return
    for root, dirs, files in walk(check_path):
        if root != check_path:
            for item in files:
                if item[item.find("."):] == ".js":
                    check = open(root + "\\" + item, "r", encoding="utf8")
                    for line in check:
                        finder = line.find(".hook")
                        if finder > 1:
                            line = line[finder+7:]
                            if line[0:2] == "S_" or line[0:2] == "C_":
                                finder = line.find("'")
                                if finder > 0:
                                    line = line[:line.find("'")]
                                else:
                                    line = line[:line.find('"')]
                                print("Checking " + line, end="\r")
                                time.sleep(0.02) # runs fast anyways just
                                # let it look cool delete this if you care
                                if line not in hooks:
                                    print(root, line)
                                    return False
    print("\n")
    return True


for whitelist_item in whitelist_file:
    whitelist_item = whitelist_item.strip()
    whitelisted_hooks.append(whitelist_item)

if checker(toolbox_folder, whitelisted_hooks):
    print("All hooks are on whitelist.")
elif checker(toolbox_folder, whitelisted_hooks) is None:
    print("Invalid file name!"
          " Make sure you've changed NAMEOFUSER in python file.")
else:
    print("Blacklisted hook has been printed, fix before using.")
