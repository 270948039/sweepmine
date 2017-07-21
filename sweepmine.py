#coding:utf-8
from prettytable import PrettyTable
import random
class minesweep():
    #类属性初始化
    matrix=[]
    two_matrix=[] #用于存放随机布雷的矩阵
    define_matrix=[]
    print_matrix=[]
    def __init__(self,nandu,minenum):
        self.nandu=int(nandu)
        self.matrix={1:'10*10',2:'15*15',3:'20*20',4:'exit'}
        self.mine=int(minenum)
        self.hardstring=''
        self.row=0
        self.col=0
        self.maxmine=0
        self.score=0
        #self.print_matrix=[['*' for row in range(self.row)] for col in range(self.col)]

    #判断用户选择的难度,以及计算最大雷数
    def define_hard(self):
        if self.nandu==4:
            exit(0)
        else :
            self.hardstring=self.matrix.get(self.nandu)
            self.hardstring=self.hardstring.split('*')
            self.row=int(self.hardstring[0])
            self.col=int(self.hardstring[1])
            self.maxmine=self.row*self.col*0.75
    # print self.maxmine

    #这一方法编写的是随机布雷模块
    def init_matrix(self):
        minesweep.print_matrix=[['*' for r in range(self.row)] for c in range(self.col)]
        num=0
        #该循环是随机添加0，1插入到列表中
        while(num<self.mine):
            a=random.randint(-1,0)
            #print a
            minesweep.matrix.append(a)
            if a==-1:
                num+=1
        #因为长度肯定没有符合对应个数，所以要加上0，然后再打乱列表的顺序
        while(len(minesweep.matrix)<(self.col*self.row)):
            minesweep.matrix.append(0)
        random.shuffle(minesweep.matrix)
        #print minesweep.matrix
        #这个python自带的列表生成式太厉害了，很难想
        #从matrix列表中按行列存放到扫雷矩阵中
        for i in range(self.row):
            minesweep.two_matrix.append([minesweep.matrix[ii] for ii in [i*self.col+ii for ii in range(self.col)]])
            # print minesweep.two_matrix[0][5]
    #计算每个位置周围的地雷的个数

    #计算地雷区的雷数
    def calc_mine(self):
        minesweep.define_matrix=[[0 for row in range(self.row)] for col in range(self.col)]
        num=0
        for i in range(self.row):
            for ii in range(self.col):
                if(minesweep.two_matrix[i][ii]!=-1): #如果不是雷则计算该位置九宫格内的雷数
                    #左上角
                    if (i-1>=0 and ii-1>=0):
                        if minesweep.two_matrix[i-1][ii-1]==-1:
                            num+=1
                    #正上方
                    if i-1>=0:
                        if minesweep.two_matrix[i-1][ii]==-1:
                            num+=1
                    #右上角
                    if i-1>=0 and ii+1<=self.col-1:
                        if minesweep.two_matrix[i-1][ii+1]==-1:
                            num+=1
                    #左方
                    if ii-1>=0:
                        if minesweep.two_matrix[i][ii-1]==-1:
                            num+=1
                    #右方
                    if ii+1<=self.col-1:
                        if minesweep.two_matrix[i][ii+1]==-1:
                            num+=1
                    #左下角
                    if i+1<=self.row-1 and ii-1>=0:
                        if minesweep.two_matrix[i+1][ii-1]==-1:
                            num+=1
                    #正下方
                    if i+1<=self.row-1:
                        if minesweep.two_matrix[i+1][ii]==-1:
                            num+=1
                    #右下角
                    if i+1<=self.row-1 and ii+1<=self.col-1:
                        if minesweep.two_matrix[i+1][ii+1]==-1:
                            num+=1
                    minesweep.define_matrix[i][ii]=num
                    num=0
                else :minesweep.define_matrix[i][ii]=-1



    #画出扫雷棋盘方法
    def print_minefile(self):
        #minesweep.print_matrix=[['*' for row in range(self.row)] for col in range(self.col)]
        tb=PrettyTable([i+1 for i in range(self.col)])
        tb1=PrettyTable([i+1 for i in range(self.col)])
        '''
        for i in range(self.row):
            tb.add_row([minesweep.matrix[ii] for ii in [i*self.col+ii for ii in range(self.col)]])

        print tb
     '''

        for i in range(self.row):
            tb.add_row(minesweep.define_matrix[i])
        print tb

        for i in range(self.row):
            tb1.add_row(self.print_matrix[i])
        print tb1

    # print self.print_matrix
    #玩家点击方法
    def player(self,x,y):
        if minesweep.define_matrix[x][y]==-1:
            print 'Game over!'
            print 'would you play again?'
            a=raw_input('Y or N?\n')
            if a=='Y' or a=='y':
                self.main()
            else :
                exit(0)
        else :
            if minesweep.define_matrix[x][y]==0:
                self.print_matrix[x][y]=minesweep.define_matrix[x][y]
                #minesweep.define_matrix[x][y]+=10
                self.recursion(x,y)


            else:
                if minesweep.define_matrix[x][y]/10==0: #玩家没选择过的空格
                    self.print_matrix[x][y]=minesweep.define_matrix[x][y] #
                    minesweep.define_matrix[x][y]+=10

                else:
                    print 'you have select this block,please select again!'    #玩家选择过该空格
        self.print_minefile()
    #递归缺少结束条件
    def recursion(self,x,y):
        ############
        if self.had_select(x, y)==0: #已经被选择的直接返回
            return
        minesweep.define_matrix[x][y]+=10

        if (x-1>=0 and y-1>=0):
            if minesweep.define_matrix[x-1][y-1]==0:
                self.print_matrix[x-1][y-1]=minesweep.define_matrix[x-1][y-1]  #这一个赋值是无雷时赋值
                self.recursion(x-1,y-1)
            elif self.had_select(x-1, y-1)==1:
                minesweep.print_matrix[x-1][y-1]=minesweep.define_matrix[x-1][y-1]
                minesweep.define_matrix[x-1][y-1]+=10
        if x-1>=0:
            if minesweep.define_matrix[x-1][y]==0:
                self.print_matrix[x-1][y]=minesweep.define_matrix[x-1][y]
                self.recursion(x-1,y)
            elif self.had_select(x-1, y)==1:
                minesweep.print_matrix[x-1][y]=minesweep.define_matrix[x-1][y]
                minesweep.define_matrix[x-1][y]+=10
        #右上角
        if x-1>=0 and y+1<=self.col-1:
            if minesweep.define_matrix[x-1][y+1]==0:
                self.print_matrix[x-1][y+1]=minesweep.define_matrix[x-1][y+1]
                self.recursion(x-1,y+1)
            elif self.had_select(x-1, y+1)==1:
                minesweep.print_matrix[x-1][y+1]=minesweep.define_matrix[x-1][y+1]
                minesweep.define_matrix[x-1][y+1]+=10
        #左方
        if y-1>=0:
            if minesweep.define_matrix[x][y-1]==0:
                self.print_matrix[x][y-1]=minesweep.define_matrix[x][y-1]
                self.recursion(x,y-1)
            elif self.had_select(x, y-1)==1:
                minesweep.print_matrix[x][y-1]=minesweep.define_matrix[x][y-1]
                minesweep.define_matrix[x][y-1]+=10
        #右方
        if y+1<=self.col-1:
            if minesweep.define_matrix[x][y+1]==0:
                self.print_matrix[x][y+1]=minesweep.define_matrix[x][y+1]
                self.recursion(x,y+1)
            elif self.had_select(x, y+1)==1:
                minesweep.print_matrix[x][y+1]=minesweep.define_matrix[x][y+1]
                minesweep.define_matrix[x][y+1]+=10
        #左下角
        if x+1<=self.row-1 and y-1>=0:
            if minesweep.define_matrix[x+1][y-1]==0:
                self.print_matrix[x+1][y-1]=minesweep.define_matrix[x+1][y-1]
                self.recursion(x+1,y-1)
            elif self.had_select(x+1, y-1)==1:
                minesweep.print_matrix[x+1][y-1]=minesweep.define_matrix[x+1][y-1]
                minesweep.define_matrix[x+1][y-1]+=10
        #正下方
        if x+1<=self.row-1:
            if minesweep.define_matrix[x+1][y]==0:
                self.print_matrix[x+1][y]=minesweep.define_matrix[x+1][y]
                self.recursion(x+1,y)
            elif self.had_select(x+1, y)==1:
                minesweep.print_matrix[x+1][y]=minesweep.define_matrix[x+1][y]
                minesweep.define_matrix[x+1][y]+=10
        #右下角
        if x+1<=self.row-1 and y+1<=self.col-1:
            if minesweep.define_matrix[x+1][y+1]==0:
                self.print_matrix[x+1][y+1]=minesweep.define_matrix[x+1][y+1]
                self.recursion(x+1,y+1)
            elif self.had_select(x+1, y+1)==1:
                minesweep.print_matrix[x+1][y+1]=minesweep.define_matrix[x+1][y+1]
                minesweep.define_matrix[x+1][y+1]+=10
    #判断是否被选择函数
    def had_select(self,x,y):
        if minesweep.define_matrix[x][y]/10==0: #未选择
            return 1
        else :return 0  #已选择
    '''
    def define_start(self,content):
        if content.isdigit()==True:
            return 1
        elif content=='q':
            return -1
        else :
            return 0
    '''




    def main(self):
        self.define_hard()
        self.init_matrix()
        self.calc_mine()
        self.print_minefile()
        while(1):
            print 'please select the block: x:(1-%d) y:(1-%d)'%(self.row,self.col)
            print 'if you want to quit the game,press \'q\''
            print 'mark place,press \'m\''
            a=raw_input('x:')
            b=raw_input('y:')
            if a.isdigit() and b.isdigit():
                if int(a)>self.row or int(b)>self.col or int(a)<1 or int(b)<1:
                    print '输入的坐标不在范围内,请重新输入！'.decode('utf-8')
                else:
                    self.player(int(a)-1,int(b)-1)
            elif a=='q' or b=='q':
                exit(0)
                '''
            elif a=='m' or b=='m':
                print 'mark place is:'
                ma=int(raw_input('x:'))
                mb=int(raw_input('y:'))
                '''
            else :print '请输入数字！'.decode('utf-8')
        #print 'define matrix is ',minesweep.define_matrix
        #print 'two_matrix is',minesweep.two_matrix
        #print 'matrix is',minesweep.matrix

nandu=raw_input(
                'please choose the size:\n1.10*10\n'
                '2.15*15\n'
                '3.20*20\n'
                '4.exit\n'

                 )
minenum=raw_input('请输入地雷数目(不超过总格数的75%):'.decode('utf-8').encode('gbk'))
#.decode('utf-8').encode('gbk')


if nandu.isdigit() and minenum.isdigit():
    mine=minesweep(nandu,minenum)
    mine.main()
else :print ('输入的不全是数字，请重新输入！！'.decode('utf-8'))
