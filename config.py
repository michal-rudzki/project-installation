import os, json
from subprocess import Popen, PIPE

def folderCreation(folders):
    for x in folders:
        if os.path.isdir(x) != True:
            print(f"Folder creation... {x}")
            os.mkdir(x)
            print("Created...")

def djangoInstallation(appName=None):
    proc = Popen(['django-admin.exe', 'startapp', (appName).lower()], stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    print(f'Django app: {appName} created.')
    
def reactInstallation(appName=None):
    proc = Popen(['npx.cmd', '-y', 'create-react-app', (appName).lower()], stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    print(f'React app: {appName} created.')


with open('config.json', 'r') as f:
    jsonData = json.load(f)

print(jsonData["installation"]["django"])
print(jsonData["installation"]["react"])

#folderCreation(jsonData["folders"]) 
#djangoInstallation('Testowski')
#reactInstallation('dupowski')

#print(json.dumps(jsonData["folders"], indent=4))
#print(json.dumps(jsonData["installation"], indent=4))
#print(json.dumps(jsonData, indent=4))
