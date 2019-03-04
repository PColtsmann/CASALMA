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
        if glob.glob('*concat.ms'):
            for k in glob.glob('*concat.ms'):
                direct = '/storage/astro2/phrpfc/BPic/2017.1.01583.S/Averaged/' + vishead(vis=k,mode = 'get',hdkey='field')[0][0]
                if not os.path.exists(direct):
                    os.mkdir(direct)
                    os.rename(os.getcwd()+'/'+k, direct+'/'+k)
                    print(k + ' moved to '+direct)
        elif glob.glob('*.2chan.ms'):
            for k in glob.glob('*2chan.ms'):
                direct = '/storage/astro2/phrpfc/BPic/2017.1.01583.S/Averaged/' + vishead(vis=k,mode = 'get',hdkey='field')[0][0]
                if not os.path.exists(direct):
                    os.mkdir(direct)
                    os.rename(os.getcwd()+'/'+k, direct+'/'+k)
                    print(k + ' moved to '+direct)
        if glob.glob('*.cube*'):####
            for k in glob.glob('*.cube.ms'):
                direct = '/storage/astro2/phrpfc/BPic/2017.1.01583.S/COLines/' + vishead(vis=k,mode = 'get',hdkey='field')[0][0]
                if not os.path.exists(direct):
                    os.mkdir(direct)
                    os.rename(os.getcwd()+'/'+k, direct+'/'+k)
                    print(k + ' moved to '+direct)
            for k in glob.glob('*fits'):
                os.rename(os.getcwd()+'/'+k, '/storage/astro2/phrpfc/BPic/2017.1.01583.S/Averaged/'  + vishead(vis=k,mode = 'get',hdkey='field')[0][0]+'/'+k)
            for k in glob.glob('*png'):
                os.rename(os.getcwd()+'/'+k, '/storage/astro2/phrpfc/BPic/2017.1.01583.S/Averaged/'  + vishead(vis=k,mode = 'get',hdkey='field')[0][0]+'/'+k)
os.chdir(directory1)	












