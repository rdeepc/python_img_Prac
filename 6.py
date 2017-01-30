import matplotlib.pyplot as plt
import os

directory='c'
sub='fol1'
if not os.path.exists(directory):
    os.makedirs(directory)
else:
    if not os.path.exists(sub):
        os.makedirs(directory+'/'+sub)
