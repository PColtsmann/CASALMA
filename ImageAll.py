
import os
import glob

#os.chdir('yourpath/projectcode')
"""
for i in glob.glob('*science_goal*'):
    if i == glob.glob('*science_goal*')[0]:
        directory1 = os.getcwd()
    directory = directory1 + '/' + i
    os.chdir(directory)
    for j in glob.glob('*'):
        if j == glob.glob('*')[0]:
                directory2 = os.getcwd()
        directory = directory2 + '/' + j
        os.chdir(directory)
        os.chdir(glob.glob('*')[0])
        os.chdir('calibrated')  
		for k in glob.glob('*ms*'):
			if glob.glob('*concat.ms'):
				for k in glob.glob('*concat.ms'):
					clean(vis=k,
					imagename='k', 
					imsize=[180,180],
					cell=['0.16arcsec'],
					interactive=True)					
					print(k + ' imaged')
						
			elif glob.glob('*.2chan.ms'):
				for k in glob.glob('*2chan.ms'):
					tclean(vis=k,
					imagename='k', 
					imsize=[180,180],
					cell=['0.16arcsec'],
					interactive=True)	
					print(k + ' imaged')

os.chdir(directory1)	
"""
#intented for after MoveAll
directory1 = os.getcwd()
os.chdir(directory1+'/Averaged')
for i in glob.glob('*'):
    os.chdir(directory1+'/Averaged/'+i)  
    for k in glob.glob('*.ms'):
        tclean(vis=k, imagename=k, imsize=[180,180], cell=['0.16arcsec'], interactive=True)					
        print(k + ' imaged')

os.chdir(directory1)	
