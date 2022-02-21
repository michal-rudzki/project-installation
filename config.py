import os, json
from subprocess import Popen, PIPE

def folderCreation(folders):
    for x in folders:
        if os.path.isdir(x) != True:
            print(f"Folder creation... {x}")
            os.mkdir(x)
            print("Created...")

def frameworkInst(cmdInst):
    proc = Popen(cmdInst, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    print(f'AppName: {cmdInst[-1]} created.')
    
def main():
    with open('config.json', 'r') as f:
        jsonData = json.load(f)

    for x in jsonData:
        if x == 'folders':
            folderCreation(jsonData[x])
        
        """ Installation depends on "service" : True """
        if x == 'installation':
            cmdInst = []
            
            for y in jsonData[x]:
                cmdInst = []
                for list in jsonData[x][y][2]:
                    cmdInst.append(list)
                cmdInst.append(jsonData[x][y][1])

                if bool(jsonData[x][y][0]) == True:
                    frameworkInst(cmdInst)

                #print(y)
                #print(jsonData[x][y][0])

    # leci pokoleji jak w pliku json, najpierw django and true (instllationDjango), react and true (installationReact)
    # print(jsonData["installation"]["django"])
    # print(jsonData["installation"]["react"])

if __name__ == '__main__':
    main()


#folderCreation(jsonData["folders"]) 
#djangoInstallation('Testowski')
#reactInstallation('dupowski')

#print(json.dumps(jsonData["folders"], indent=4))
#print(json.dumps(jsonData["installation"], indent=4))
#print(json.dumps(jsonData, indent=4))
