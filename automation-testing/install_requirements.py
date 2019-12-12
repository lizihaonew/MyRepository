import subprocess

with open('requirements/common.txt') as requirements:
    for package in requirements:
        subprocess.call(['pip', 'install', package])
