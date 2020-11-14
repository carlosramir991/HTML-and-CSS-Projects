import shutil
import os
from datetime import datetime
source = '/Users/slims/Documents/python_projects/folder_A/'

destination = '/Users/slims/Documents/python_projects/folder_B/'
time_1 = os.path.getmtime(destination)
print(datetime.fromtimestamp(time_1).strftime('%Y-%m-%d %H:%M:%S'))
#files = os.listdir(source)

#for i in files:

    #shutil.move(source+i, destination)
