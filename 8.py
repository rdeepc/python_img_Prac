import os

directory = 'dataset'


def creatfolder(sub):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        if not os.path.exists(sub):
            os.makedirs(directory+'/'+sub)
i=1

for y in range(4):
    for x in range(3):
        print(i)
        i=i+1
