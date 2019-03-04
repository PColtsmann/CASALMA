
import os
import glob

#os.chdir('yourpath/projectcode')
z=0
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
        changed = 1
        unchanged = 0
        while changed != unchanged:
            changed,unchanged = 0,0
            for l in glob.glob('*.ms*'):
                if 'split.cal' in l and 'onsource' not in l and not glob.glob(l[:-12]+'split'):
                    print('Splitting ' + l)
                    os.mknod(l[:-12]+'split')#this will leave a permanent record of this ms having been split before, could be easily circumvented by keeping the name of l and appending field name
                    for k in vishead(vis=l,mode = 'get',hdkey='field')[0]:#assumes multiple fields
                        if k[0] != 'J':#gets rid of calibrators
                            if glob.glob(k+'.split.cal.onsource.ms'):
                                mstransform(vis=l, outputvis=str(len(glob.glob(k+'.split.cal.onsource.ms'))) + k +'.split.cal.onsource.ms',intent='OBSERVE_TARGET#ON_SOURCE',spw='19,21,23,25', datacolumn='DATA',field=k) 
                            else:
                                mstransform(vis=l, outputvis=k+'.split.cal.onsource.ms',intent='OBSERVE_TARGET#ON_SOURCE',spw='19,21,23,25',field=k, datacolumn='DATA') 
                        changed+=1
                elif 'split.cal' not in l and 'onsource' not in l and not glob.glob(l[:-2]+'split'):
                    os.mknod(l[:-2]+'split')
                    print('Splitting ' + l)
                    for k in vishead(vis=l,mode = 'get',hdkey='field')[0]:
                        if k[0] != 'J':
                            if glob.glob(k+'.onsource.ms'):#multiple observations of same field
                                mstransform(vis=l, outputvis=str(len(glob.glob(k+'.onsource.ms'))) + k +'.onsource.ms',intent='OBSERVE_TARGET#ON_SOURCE',spw='19,21,23,25',field=k) 
                            else:
                                mstransform(vis=l, outputvis=k+'.onsource.ms',intent='OBSERVE_TARGET#ON_SOURCE',spw='19,21,23,25',field=k) 
                    changed+=1
                if 'onsource.ms' in l and not glob.glob(l[:-2]+'30time*') and not glob.glob(l[:-2]+'*2chan*'):
                    print('Time Averaging ' + l)
                    mstransform(vis=l, outputvis=l[:-2]+'30time.ms', timeaverage=True, timebin='30s', datacolumn='DATA')
                    changed+=1
                if '30time.ms' in l and not glob.glob(l[:-2]+'*2chan*'): 
                    print('Channel Averaging ' + l)
                    mstransform(vis=l, outputvis=l[:-2]+'2chan.ms', chanaverage=True, chanbin=[64,64,64,1920], datacolumn='DATA')
                    changed+=1
            if len(glob.glob('*2chan*')) > 1:
                for m in glob.glob('*2chan*'):
                    for n in glob.glob('*2chan*'):
                        if m != n and vishead(vis=m,mode = 'get',hdkey='field')[0] == vishead(vis=n,mode = 'get',hdkey='field')[0]:
                            if 'split.cal' in m and not glob.glob(vishead(vis=n,mode = 'get',hdkey='field')[0][0]+'.split.cal.onsource.30time.2chan.concat.ms'):
                                print('concatenating '+m+', '+n)
                                concat(vis = [m,n], concatvis = vishead(vis=n,mode = 'get',hdkey='field')[0][0]+'.split.cal.onsource.30time.2chan.concat.ms', freqtol = '1MHz', dirtol='2arcsec')
                                print(m+', '+n+' concatenated')
                                changed+=1
                            elif not glob.glob(vishead(vis=n,mode = 'get',hdkey='field')[0][0]+'.onsource.30time.2chan.concat.ms'):#[0][0]
                                print('concatenating '+m+', '+n)
                                concat(vis = [m,n], concatvis = vishead(vis=n,mode = 'get',hdkey='field')[0][0]+'.onsource.30time.2chan.concat.ms', freqtol = '1MHz', dirtol='2arcsec')
                                print(m+', '+n+' concatenated')
                                changed+=1
        print(str(glob.glob('*onsource.30time.2chan.ms*'))+' averaged')

os.chdir(directory1)	
