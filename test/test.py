import glob2
import os.path as path
import matplotlib.pyplot as plt
import os


source_directory = 'source'
destination='dataset'

working_num=str(1)

def creatfolder(sub):
    if not os.path.exists(sub):
        os.makedirs(destination+'/'+sub)



creatfolder(working_num)




