import os

directory = 'dataset'


def creatfolder(sub):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        if not os.path.exists(sub):
            os.makedirs(directory+'/'+sub)
i=0

for i in range(12):
   creatfolder(str(i+1))
