
import os
import glob

#os.chdir('yourpath/projectcode')
directory1 = os.getcwd()
for i in glob.glob('*science_goal*'):     
    directory = directory1 + '/' + i
    os.chdir(directory)
    for j in glob.glob('*'):
        if j == glob.glob('*')[0]:
                directory2 = os.getcwd()
        directory = directory2 + '/' + j
        os.chdir(directory)
        os.chdir(glob.glob('*')[0])
        os.chdir('calibrated')  
        if glob.glob('*onsource*'):
            for k in glob.glob('*onsource*'):
                os.system('rm -r ' + k)
                print(k + ' deleted')

os.chdir(directory1)	
