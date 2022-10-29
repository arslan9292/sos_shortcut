#!/usr/bin/python3

"""

@author    : Arslan Ahmad
VERSION_NUMBER = 1

"""

import re
import sys
import os
import glob

def main():
    try:
        firstarg = sys.argv[1]

        if firstarg == 'config':
            if os.path.exists("./sos_commands/pacemaker/pcs_config"):
                file = open("./sos_commands/pacemaker/pcs_config")
                pcs_config = file.read()
                file.close()
                print(pcs_config)
            elif os.path.exists("./sos_commands/cluster/pcs_config"):
                file = open("./sos_commands/cluster/pcs_config")
                pcs_config = file.read()
                file.close()
                print(pcs_config)
            elif os.path.exists("./etc/cluster/cluster.conf"):
                print("\n\tNOTE: This is a RHEL6 cman/rgmanager cluster.\n")
                file = open("./etc/cluster/cluster.conf")
                pcs_config = file.read()
                file.close()
                print(pcs_config)
            else:
                print("Cluster configuration is not captured.")

        elif firstarg == 'status':
            if os.path.exists("./sos_commands/pacemaker/pcs_status"):
                file = open("./sos_commands/pacemaker/pcs_status")
                pcs_status = file.read()
                file.close()
                print(pcs_status)
            elif os.path.exists("./sos_commands/pacemaker/pcs_status_--full"):
                file = open("./sos_commands/pacemaker/pcs_status_--full")
                pcs_status = file.read()
                file.close()
                print(pcs_status)
            elif os.path.exists("./sos_commands/cluster/pcs_status"):
                file = open("./sos_commands/cluster/pcs_status")
                pcs_status = file.read()
                file.close()
                print(pcs_status)            
            elif os.path.exists("./sos_commands/cluster/clustat"):
                print("\n\tNOTE: This is a RHEL6 cman/rgmanager cluster.\n")
                file = open("./sos_commands/cluster/clustat")
                pcs_status = file.read()
                file.close()
                print(pcs_status)
            else:    
                print("Cluster status is not captured.")

        elif firstarg == 'cib':
            crm_report = False
            for cibexists in glob.iglob("./sos_commands/pacemaker/crm_report/*/"):
                crm_report = True
                break
            if crm_report == True:
                for root, dirs, files in os.walk(cibexists):
                    if 'cib.xml' in files:
                        cib = os.path.join(root, 'cib.xml')
                    break
                if os.path.exists(cib):
                    file = open(cib)
                    pcs_cib = file.read()
                    file.close()
                    print(pcs_cib)
                else:
                    print("Cluster CIB is not captured.")
            elif crm_report == False:
                if os.path.exists("./var/lib/pacemaker/cib/cib.xml"):
                    file = open("./var/lib/pacemaker/cib/cib.xml")
                    pcs_cib = file.read()
                    file.close()
                    print(pcs_cib)
                else:
                    print("Cluster CIB is not captured.")

        elif firstarg == 'prop':
            if os.path.exists("./sos_commands/pacemaker/pcs_property_list_--all"):
                file = open("./sos_commands/pacemaker/pcs_property_list_--all")
                pcs_property = file.read()
                file.close()
                print(pcs_property)
            else:    
                print("Cluster property is not captured.")
        
        else:
            print("Invalid input. Available options: config, status, cib and prop.")
            
    except IndexError:
        print("Missing the input to display. Available options: config, status, cib and prop.")

if __name__ == "__main__":
    main()
