import os
from os.path import isfile, join

mypath = os.getcwd()
allfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
oldNamesList = input('please enter some part of your files name: ')
name = input('What is your files main name? ')
illigalChar = input('Is there another number besides episode,season and quality(like 1080 and 720) in your files? If yes write it.\n')
specificAllFiles = [ x for x in allfiles if oldNamesList in x ]
for i in specificAllFiles:
    seperatedListWithDot = i.split('.')
    suffix = seperatedListWithDot[-1]
    if suffix == 'srt' or suffix == 'ass' or suffix == 'sub' or suffix == 'idx' or suffix == 'mkv' or suffix == 'mp4':
        justName = '.'.join(seperatedListWithDot[:-1])
        nameByChars = [char for char in justName]
        tempNum = []
        num = ''
        season = 0
        episode = 0
        for j in range(len(nameByChars)):
            if nameByChars[j].isdigit():
                tempNum.append(nameByChars[j])
            elif len(tempNum)>0:
                num = ''.join(tempNum)
                tempNum = []
                if illigalChar!='':
                    illigalCharList = illigalChar.split(' ')
                    cond = "if num != '1080' and num != '720' and num != '480'"
                    for k in range(len(illigalCharList)):
                        cond += f" and num != '{illigalCharList[k]}'"
                    cond += ':\n'
                    cond += '''
                        if nameByChars[j-len(num)-1] == 'S':
                            season = num
                        else:
                            episode = num
                    '''
                    exec(cond)
                else:
                    if num != '1080' and num != '720' and num != '480':
                        if nameByChars[j-len(num)-1] == 'S':
                            season = num
                        else:
                            episode = num
        if len(tempNum)>0 and episode == 0:
            num = ''.join(tempNum)
            episode = num
        oldName = mypath + '\\' + i
        newName = f'{mypath}\{name} S{season}x{episode}.{suffix}'
        os.rename(oldName, newName)
        print(f'Changed {i} to {name} S{season}x{episode}.{suffix}')
