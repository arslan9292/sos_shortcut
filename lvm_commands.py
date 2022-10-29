#!/usr/bin/python3

"""

@author    : Arslan Ahmad
VERSION_NUMBER = 1

"""

import re
import sys
import os

def main():
    for root, dirs, files in os.walk("./sos_commands/"):
        for i in files:
            if re.search('vgs_-v_-o*', i):
                vgs_file = os.path.join(root, i)
            elif re.search('lvs_-a_-o*', i):
                lvs_file = os.path.join(root, i)
            elif re.search('pvs_-a_-v*', i):
                pvs_file = os.path.join(root, i)
            elif re.search('multipath_-v4_-ll', i):
                mpath_file = os.path.join(root, i)

    try:
        firstarg = sys.argv[1]

        if firstarg == 'vgs':
            if os.path.exists(vgs_file):
                file = open(vgs_file)
                vgs = file.read()
                file.close()
                print(vgs)
            else:
                print("%s file is not captured in sosreport."%firstarg)

        elif firstarg == 'lvs':
            if os.path.exists(lvs_file):
                file = open(lvs_file)
                lvs = file.read()
                file.close()
                print(lvs)
            else:
                print("%s file is not captured in sosreport."%firstarg)

        elif firstarg == 'pvs':
            if os.path.exists(pvs_file):
                file = open(pvs_file)
                pvs = file.read()
                file.close()
                print(pvs)
            else:
                print("%s file is not captured in sosreport."%firstarg)

        elif firstarg == 'mpath':
            if os.path.exists(mpath_file):
                file = open(mpath_file)
                mpath = file.read()
                file.close()
                print(mpath)
            else:
                print("%s file is not captured in sosreport."%firstarg)

        elif firstarg == 'conf':
            if os.path.exists('./etc/lvm/lvm.conf'):
                with open("./etc/lvm/lvm.conf", "r") as ifile:
                    for line in ifile:
                        if re.search("locking_type|use_lvmetad|volume_list|filter|global_filter|system_id_source|auto_activation_volume_list", line):
                            param = line.lstrip()
                            if (param.startswith("locking_type")):
                                param = param.strip()
                                print("\t" + param)
                            if (param.startswith("use_lvmetad")):
                                param = param.strip()
                                print("\t" + param)
                            if (param.startswith("volume_list")):
                                param = param.strip()
                                print("\t" + param)
                            if (param.startswith("filter")):
                                param = param.strip()
                                print("\t" + param)
                            if (param.startswith("global_filter")):
                                param = param.strip()
                                print("\t" + param)
                            if (param.startswith("system_id_source")):
                                param = param.strip()
                                print("\t" + param)
                            if (param.startswith("auto_activation_volume_list")):
                                param = param.strip()
                                print("\t" + param)
            else:
                print("%s file is not captured in sosreport."%firstarg)
        else:
            print("Invalid input. Available options: vgs, lvs, pvs, mpath and conf.")

    except IndexError:
        print("Missing the input to display. Available options: vgs, lvs, pvs, mpath and conf (display entries in lvm.conf file.")

if __name__ == "__main__":
    main()
