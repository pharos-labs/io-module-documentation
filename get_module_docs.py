# Extract the README file from all available IOMs
#

import requests
import tempfile
import tarfile
import os
import shutil

BASE_URL = 'https://dl.pharoscontrols.com/resources/io_modules/'
LIBRARY_DESCRIPTION = 'module_library_v2.json'
IOM_EXTENSION = '.iom'
DOCS_DIR = 'sphinx-src'


# Version key function used for sorting modules by version
# Format major.minor.patch[.BETAbeta]
def sortVersionKey(item):
    item = str(item['version'])
    parts = item.split('.')
    major = 0
    minor = 0
    patch = 0
    beta = 0
    for i in range(len(parts)):
        match i:
            case 0:
                major = int(parts[0])
            case 1:
                minor = int(parts[1])
            case 2:
                patch = int(parts[2])
            case 3:
                beta = int(parts[3][4])

    return major * 300 + minor * 200 + patch * 100 + beta

# Get the highest version from an array of modules,
# using 'version' as key
def getHighestVersion(moduleArray):
    if len(moduleArray) == 1:
        return moduleArray[0]
    moduleArray.sort(key=sortVersionKey, reverse=True)
    return moduleArray[0]

print('Downloading IO module library')
resp = requests.get(url=BASE_URL + LIBRARY_DESCRIPTION)
data = resp.json()

# Table of modules
moduleTable = open(os.path.join(DOCS_DIR, 'module_table.rst'), 'w')
moduleTable.write('''.. list-table:: Modules
   :widths: 25 25 10 40 10
   :header-rows: 1

   * - Category
     - Module
     - Module Version
     - Description
     - IOM API Version\n''')

# Table of contents
tocFile = open(os.path.join(DOCS_DIR, 'toc.rst'), 'w')

with tempfile.TemporaryDirectory() as tempDir:
    for group in data:

        groupName = group['groupName']

        tocFile.write(f'''.. toctree::
   :caption: {groupName}
   :hidden:\n\n''')

        # Make an output directory for the group
        groupDirPath = os.path.join(DOCS_DIR, 'iom',groupName)
        if not os.path.exists(groupDirPath):
            try:
                os.mkdir(groupDirPath)
            except:
                print(f'Error making directory {groupDirPath}')

        for module in group['modules']:
            print('Extracting ' + module['name'])
            version = getHighestVersion(module['versions'])
            print(f'Highest version {version['version']}')

            # Sanitized module name for making the path/URL
            # Some module names contain a forward slash, replace with a space
            sanitizedModuleName = module['name'].replace("/", " ")

            outputFilename = os.path.join(groupDirPath, f'{sanitizedModuleName}.md')

            moduleTable.write(f'   * - {groupName}\n')
            moduleTable.write(f'     - :doc:`{module['name']}<iom/{groupName}/{sanitizedModuleName}>`\n')
            moduleTable.write(f'     - {version['version']}\n')
            moduleTable.write(f'     - {module['description']}\n')
            moduleTable.write(f'     - {version['apiVersion']}\n')

            tocFile.write(f'   {module['name']} <iom/{groupName}/{sanitizedModuleName}>\n')

            moduleData = requests.get(BASE_URL + version['path'] + IOM_EXTENSION)

            bytesToSkip = 23
            if moduleData.content[5] == 0:
                bytesToSkip = 22

            # Skip the bytes for the header
            # TODO - will only handle v0/v1 header, size may change for others
            filename = os.path.join(tempDir, f'{version['path']}.tgz')
            with open(filename, 'wb') as file:
                file.write(moduleData.content[bytesToSkip:])

            # Delete if updating
            if os.path.exists(outputFilename): os.remove(outputFilename)
            # Extract the module docs
            try:
                tar = tarfile.open(filename)
                inFileData = tar.extractfile('readme.md')
                with open(outputFilename, 'wb') as outFile:
                    outFile.write(f'# {module['name']} - Version {version['version']}\n\n'.encode())
                    outFile.write(inFileData.read())
                tar.close()
            except:
                print(f'Invalid IOM? {filename}')
