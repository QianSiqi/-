import os
import sys
dir = os.getcwd()
class Comand():
    def __init__(self,v,n):
        self.v = v
        self.n = n
    def write(self):
        file = open(self.n,'a+',encoding = 'utf-8')
        file.write(self.v)
while True:
    try:
        ipt = input('>>')
        spl = ipt.split(' ')
        if spl[0] == 'cd':
            os.chdir(spl[1])
        elif '+' in ipt or '-' in ipt or '*' in ipt or '/' in ipt :
            print(str(eval(ipt)))
        elif ipt == 'quit':
            break
        elif spl[0] == 'write':
            os.system(dir + '\\bin\\vim\\vim90\\vim.exe ' + spl[1])
        elif spl[0] == 'read':
            comand = Comand('',spl[1])
            rd = open(comand.n,'r',encoding = 'utf-8')
            rd2 = rd.read()
            print(rd2)
        elif spl[0] == 'remove':
            os.system('powershell rm ' + spl[1])
        elif spl[0] == 'dir':
            os.system('dir')
        elif spl[0] == 'mkdir':
            os.mkdir(spl[1])
        else:
            print('没有这个命令！')
    except SyntaxError:
        print('语法错误！')