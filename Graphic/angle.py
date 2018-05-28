from math import pi, sin, cos
#Degrees to Radians
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

print(angle(sin(pi/2)))
