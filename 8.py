import os

directory = 'dataset'


def creatfolder(sub):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        if not os.path.exists(sub):
            os.makedirs(directory+'/'+sub)

for i in range(10):
    creatfolder(str(i+1))