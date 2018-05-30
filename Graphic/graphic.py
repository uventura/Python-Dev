import turtle
from math import sin,cos,pi,log
'''*=*=*=*=*=*=*=*=*=*=[ FUNCTIONS ]*=*=*=*=*=*=*=*=*=*='''

#Create the plan of the graphic
def constructPlan(x,y):
    #Cordenadas para o tamanho do plano cartesiano
    cordMin = lambda b: b*(-1) if b<0 else 0 #I'm using this function because just the absolute value create an error
    #If the minimum of a cordenate x is 30 for example, using the absolute value the negative part of x will have the size of 30
    plan = [abs(max(x))+5, abs(max(y))+5, cordMin(min(x))+5, cordMin(min(y))+5]
    #Loop para a criação do plano cartesiano
    for axis in plan:
        graphic.fd(axis)
        graphic.lt(180)
        graphic.fd(axis)
        graphic.rt(90)
    graphic.lt(90)

#The quadrant to create an cordenate
def quadrant(x,y):
    q = ""
    if x<0 and y>0:
        q = '1'
    elif x>0 and y>0:
        q = '2'
    elif x<0 and y<0:
        q = '3'
    else:
        q = '4'
    return q

#The draw of a cordenate
def constructCord(x,y):
    choice=["lt"]
    q = quadrant(x,y)
    if int(q)%2!=0:
        if q == "1":
            choice = ["rt"]
        graphic.lt(90)
    else:
        if q == "4":
            choice = ["rt"]
        graphic.rt(90)
    graphic.fd(abs(x))
    
    for i in range(3):
        if choice == ["rt"]:
            graphic.rt(90)
        else:
            graphic.lt(90)
        if i%2==0:
            graphic.fd(abs(y))
        else:
            graphic.fd(abs(x))
    if int(q)<3:
        graphic.lt(180)

#Goes to a point(a local based in x and y)
def findPoint(x,y):
    choice=["lt"] 
    q = quadrant(x,y)
    if int(q)%2!=0:
        if q == "1":
            choice = ["rt"]
        graphic.lt(90)
    else:
        if q == "4":
            choice = ["rt"]
        graphic.rt(90)
    graphic.fd(abs(x))
    
    for i in range(1):
        if choice == ["rt"]:
            graphic.rt(90)
        else:
            graphic.lt(90)
        if i%2==0:
            graphic.fd(abs(y))
        else:
            graphic.fd(abs(x))

#Transform angle in graus to radians
def toRad(angle):
    n = (angle*pi)/180
    return n

#Discover angle between 0° to 90° using the sin
def angle(sinx):
    tabAn = {} #Table of Angles
    aproAn = [0,0] #Approximate angles
    result = 0 #Final result
    #--------[ Table angles [0]=>Sin; [1]=>Cos. ]------------
    a = -1
    while a<45:
        a+=1
        tabAn[str(a)] = [sin(toRad(a)),cos(toRad(a))]
    #--------[ Comparation to the determine the approach angles ]------------
    for angle in tabAn:
        if sinx>=tabAn[angle][0] and sinx<=tabAn['45'][0]:
            aproAn[0]=int(angle)
            aproAn[1]=int(angle)+1
        elif sinx<=tabAn[angle][1] and sinx>tabAn['45'][0]:
            aproAn[0]=90-(int(angle)+1)
            aproAn[1]=90-int(angle)
        else:
            break
    #----------[ The Result ]----------
    '''
    The calculus for the result is:
            alpha<=angle<=beta
            
            sin(beta)-sin(alpha) ------- 1°
            sin(angle)-sin(alpha) ------- x°

            x = (sin(angle)-sin(alpha))/(sin(beta)-sin(alpha)) >>>>>>>>> This is the complementary to determinate x
        Result:
        angle = alpha+x
    '''
    findResult = lambda alpha, beta, position: (sinx-tabAn[str(alpha)][position])/(tabAn[str(beta)][position]-tabAn[str(alpha)][position])
    if aproAn[0]>44:
        result = aproAn[0]+findResult(90-aproAn[0], 90-aproAn[1], 1)
    else:
        result = aproAn[0]+findResult(aproAn[0], aproAn[1], 0)
    return  result #This is the angle

def straight(x,y):
    difx = [0,0]#Diference between the previous cordenate and the next in X
    dify = [0,0]#Diference between the previous cordenate and the next in Y
    
    counter = -1
    while counter<len(x)-2:
        counter+=1
        #First point
        difx[0] = x[counter]
        dify[0] = y[counter]
        #Second Point
        difx[1] = x[counter+1]
        dify[1] = y[counter+1]
        #Variação de uma cordenada a outra
        vx = difx[1]-difx[0]
        vy = dify[1]-dify[0]
        d = (vy**2+vx**2)**(1/2)#Distance from the prev. cord. and the next
        sinAlpha = vy/d #Sin from the angle to create the distance
        graphic.rt(90-int(angle(sinAlpha)))
        graphic.fd(d)
        graphic.lt(90-int(angle(sinAlpha)))
        
#----------------[ EXECUTION ]----------------
graphic = turtle.Turtle()
'''
#Create a straight just work for the first quadrant at moment.{DON'T FORGOT IDIOT}
#TEST 01
#Creating the cordenates
x = []
y = []
c = 0
while c<9:
    c+=1
    x.append(c*10)
    y.append(c*30)
#Construct the plan  
constructPlan(x,y)
#Draw the cordenates
c=-1
while c<len(x)-1:
    c+=1
    constructCord(x[c],y[c])
#The straight
findPoint(x[0],y[0]) #To create the straight it's necessary goes to the first cordenate
straight(x,y)
'''

#Test 02
x = [4,9,50,80,103,55,-21,-43,-7]
y = [10,14,-40,60,34,56,66,-67,9]

constructPlan(x,y)
c=-1
while c<len(x)-1:
    c+=1
    constructCord(x[c],y[c])
turtle.mainloop()
