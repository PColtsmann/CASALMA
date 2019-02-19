import os 
import glob

"""
Executing this file from within 'casa --pipeline' will execute all 'scriptForPI.py's that are contained within your ALMA
project, automatically calibrating all of your .asdm's into .ms's. The form of the script can be easily modified to only
calibrate certain asdms or to operate over multiple projects/only over certain Scheduling Blocks etc.
"""

os.chdir('yourpath/projectcode')
"""
This should be absolute path to your ALMA project code directory that contains the science_goal folders.
"""

for i in glob.glob('*'):
    if i == glob.glob('*')[0]:
        directory1 = os.getcwd()
    directory = directory1 + '/' + i
    os.chdir(directory)
    for j in glob.glob('*'):
        if j == glob.glob('*')[0]:
                directory2 = os.getcwd()
        directory = directory2 + '/' + j
        os.chdir(directory)
        os.chdir(glob.glob('*')[0])
        if not glob.glob('calibrated'):
            os.chdir('script')
            execfile(glob.glob('*.scriptForPI.py')[0])
