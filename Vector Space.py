import numpy as np
import random,re,pygal
from flask import Flask,render_template,request
app = Flask(__name__)
###################################################
#Sort
def sortSecond(val): 
    return val[1]
#Extract the query array weights
def query(x):
    #Check Query Syntax before calculations
    pattern = r'^([a-eA-E ]+)$'
    result = re.match(pattern ,x)
    if not result:
        return 2
    #End of check and start of calculations
    z=''
    print(x,type(x),sep="/")
    for i in range (len(x)):
        z=z+x[i]
    z=z.upper()
    z=z.strip()
    y=z[0]
    j=1
    for i in range (len(z)):
        y=y+" "+z[j]
        j=j+1
        if j>len(z)-1:
            break
    return y
#Calculate the simillarty
def Cal(s1,s2,s3,s4,s5,q):
    c1=np.array([0,0,0,0,0])
    c2=np.array([0,0,0,0,0])
    c3=np.array([0,0,0,0,0])
    c4=np.array([0,0,0,0,0])
    c5=np.array([0,0,0,0,0])
    cq=np.array([0,0,0,0,0])
    tfd1=[0,0,0,0,0]
    tfd2=[0,0,0,0,0]
    tfd3=[0,0,0,0,0]
    tfd4=[0,0,0,0,0]
    tfd5=[0,0,0,0,0]
    tfdq=[0,0,0,0,0]
    idf=[0,0,0,0,0]
    #Calcualte count of each letter in file
    ###################
    c1[0]=s1.count('A')
    c1[1]=s1.count('B')
    c1[2]=s1.count('C')
    c1[3]=s1.count('D')
    c1[4]=s1.count('E')
    ###################
    c2[0]=s2.count('A')
    c2[1]=s2.count('B')
    c2[2]=s2.count('C')
    c2[3]=s2.count('D')
    c2[4]=s2.count('E')
    ###################
    c3[0]=s3.count('A')
    c3[1]=s3.count('B')
    c3[2]=s3.count('C')
    c3[3]=s3.count('D')
    c3[4]=s3.count('E')
    ###################
    c4[0]=s4.count('A')
    c4[1]=s4.count('B')
    c4[2]=s4.count('C')
    c4[3]=s4.count('D')
    c4[4]=s4.count('E')
    ###################
    c5[0]=s5.count('A')
    c5[1]=s5.count('B')
    c5[2]=s5.count('C')
    c5[3]=s5.count('D')
    c5[4]=s5.count('E')
    ###################
    cq[0]=q.count('A')
    cq[1]=q.count('B')
    cq[2]=q.count('C')
    cq[3]=q.count('D')
    cq[4]=q.count('E')
    ###################
    #Calculate the tf for each file
    for i in range (len(c1)):
        tfd1[i]=c1[i]/(c1.max())
    for i in range (len(c2)):
        tfd2[i]=c2[i]/(c2.max())
    for i in range (len(c3)):
        tfd3[i]=c3[i]/(c3.max())
    for i in range (len(c4)):
        tfd4[i]=c4[i]/(c4.max())
    for i in range (len(c5)):
        tfd5[i]=c5[i]/(c5.max())
    for i in range (len(cq)):
        tfdq[i]=cq[i]/(cq.max())
    ###################
    #Calculate the count of each letter in all number of files 
    a=b=c=d=e=0
    if (s1.__contains__('A')):
        a=a+1
    if (s2.__contains__('A')):
        a=a+1
    if (s3.__contains__('A')):
        a=a+1
    if (s4.__contains__('A')):
        a=a+1
    if (s5.__contains__('A')):
        a=a+1
    if (q.__contains__('A')):
        a=a+1
    ############################
    if (s1.__contains__('B')):
        b=b+1
    if (s2.__contains__('B')):
        b=b+1
    if (s3.__contains__('B')):
        b=b+1
    if (s4.__contains__('B')):
        b=b+1
    if (s5.__contains__('B')):
        b=b+1
    if (q.__contains__('B')):
        b=b+1
    #############################
    if (s1.__contains__('C')):
        c=c+1
    if (s2.__contains__('C')):
        c=c+1
    if (s3.__contains__('C')):
        c=c+1
    if (s4.__contains__('C')):
        c=c+1
    if (s5.__contains__('C')):
        c=c+1
    if (q.__contains__('C')):
        c=c+1
    #############################
    if (s1.__contains__('D')):
        d=d+1
    if (s2.__contains__('D')):
        d=d+1
    if (s3.__contains__('D')):
        d=d+1
    if (s4.__contains__('D')):
        d=d+1
    if (s5.__contains__('D')):
        d=d+1
    if (q.__contains__('D')):
        d=d+1
    #############################
    if (s1.__contains__('E')):
        e=e+1
    if (s2.__contains__('E')):
        e=e+1
    if (s3.__contains__('E')):
        e=e+1
    if (s4.__contains__('E')):
        e=e+1
    if (s5.__contains__('E')):
        e=e+1
    if (q.__contains__('E')):
        e=e+1
    #############################
    #Calculate idf for each letter
    idf[0]=np.log2(6/a)
    idf[1]=np.log2(6/b)
    idf[2]=np.log2(6/c)
    idf[3]=np.log2(6/d)
    idf[4]=np.log2(6/e)
    ##############################
    #Calcualte td-idf for each file
    tfidf1=np.multiply(tfd1,idf)
    tfidf2=np.multiply(tfd2,idf)
    tfidf3=np.multiply(tfd3,idf)
    tfidf4=np.multiply(tfd4,idf)
    tfidf5=np.multiply(tfd5,idf)
    tfidfq=np.multiply(tfdq,idf)
    ###############################
    #Calculate Sim
    d1sim=(np.sum(np.multiply(tfidf1,tfidfq)))/np.sqrt(np.sum(np.power(tfidf1,2))*np.sum(np.power(tfidfq,2)))
    d2sim=(np.sum(np.multiply(tfidf2,tfidfq)))/np.sqrt(np.sum(np.power(tfidf2,2))*np.sum(np.power(tfidfq,2)))
    d3sim=(np.sum(np.multiply(tfidf3,tfidfq)))/np.sqrt(np.sum(np.power(tfidf3,2))*np.sum(np.power(tfidfq,2)))
    d4sim=(np.sum(np.multiply(tfidf4,tfidfq)))/np.sqrt(np.sum(np.power(tfidf4,2))*np.sum(np.power(tfidfq,2)))
    d5sim=(np.sum(np.multiply(tfidf5,tfidfq)))/np.sqrt(np.sum(np.power(tfidf5,2))*np.sum(np.power(tfidfq,2)))
    res=[round(d1sim,3),round(d2sim,3),round(d3sim,3),round(d4sim,3),round(d5sim,3)]
    return res
#Calculate the Matrix/Vector
def Cal2(s1,s2,s3,s4,s5):
    x1=[0]*5
    x2=[0]*5
    x3=[0]*5
    x4=[0]*5
    x5=[0]*5
    #Calculate the count of numbers(links)
    x1[0]=s1.count('1')
    x1[1]=s1.count('2')
    x1[2]=s1.count('3')
    x1[3]=s1.count('4')
    x1[4]=s1.count('5')
    #################################
    x2[0]=s2.count('1')
    x2[1]=s2.count('2')
    x2[2]=s2.count('3')
    x2[3]=s2.count('4')
    x2[4]=s2.count('5')
    #################################
    x3[0]=s3.count('1')
    x3[1]=s3.count('2')
    x3[2]=s3.count('3')
    x3[3]=s3.count('4')
    x3[4]=s3.count('5')
    #################################
    x4[0]=s4.count('1')
    x4[1]=s4.count('2')
    x4[2]=s4.count('3')
    x4[3]=s4.count('4')
    x4[4]=s4.count('5')
    #################################
    x5[0]=s5.count('1')
    x5[1]=s5.count('2')
    x5[2]=s5.count('3')
    x5[3]=s5.count('4')
    x5[4]=s5.count('5')
    #Remove multi-links
    for i in range (len(x1)):
        while x1[i]>1:
            x1[i]=x1[i]-1
    for i in range (len(x2)):
        while x2[i]>1:
            x2[i]=x2[i]-1
    for i in range (len(x3)):
        while x3[i]>1:
            x3[i]=x3[i]-1
    for i in range (len(x4)):
        while x4[i]>1:
            x4[i]=x4[i]-1
    for i in range (len(x5)):
        while x5[i]>1:
            x5[i]=x5[i]-1
    #Remove Loops
    if s1.__contains__('1'):
        x1[0]=0
    if s2.__contains__('2'):
        x2[1]=0
    if s3.__contains__('3'):
        x3[2]=0
    if s4.__contains__('4'):
        x4[3]=0
    if s5.__contains__('5'):
        x5[4]=0
    #Construct Adjancy Matrix and calculate a & h
    ares=[0]*5
    hres=[0]*5
    finalres=[0,0]
    A = np.array([x1,x2,x3,x4,x5])
    AT = A.T
    h=np.array([1,1,1,1,1])
    a=np.array([1,1,1,1,1])
    for i in range(20):
        a=np.dot(AT,h)
        a=a/np.sqrt(np.sum(np.power(a,2)))
        h=np.dot(A,a)
        h=h/np.sqrt(np.sum(np.power(h,2)))
    ares=[['D1',round(a[0],2)],['D2',round(a[1],2)],['D3',round(a[2],2)],['D4',round(a[3],2)],['D5',round(a[4],2)]]
    hres=[['D1',round(h[0],2)],['D2',round(h[1],2)],['D3',round(h[2],2)],['D4',round(h[3],2)],['D5',round(h[4],2)]]
    # ares.sort(key=sortSecond,reverse=True)
    # hres.sort(key=sortSecond,reverse=True)
    finalres=[ares,hres]
    return finalres
#read file and extarct wanted array
def read(p):
    f = open(p, "r+")
    line = f.readline()
    s=line.split()
    return s
#Display Result
def show(d1sum,d2sum,d3sum,d4sum,d5sum):
    res=[['D1',d1sum],['D2',d2sum],['D3',d3sum],['D4',d4sum],['D5',d5sum]]
    res.sort(key=sortSecond,reverse=True)
    return res
    # if (d1sum>=d2sum and d1sum>=d3sum):
    #     if (d2sum>=d3sum):
    #         res = 'Sim to Query is : \n(1) D1 with ratio = '+str(d1sum)+'\n(2) D2 with ratio = '+str(d2sum)+'\n(3) D3 with ratio = '+str(d3sum)+'\n'
    #         return res
    #     else:
    #         res = 'Sim to Query is : \n(1) D1 with ratio = '+str(d1sum)+'\n(2) D3 with ratio = '+str(d3sum)+'\n(3) D2 with ratio = '+str(d2sum)+'\n'
    #         return res
    # elif (d2sum>=d1sum and d2sum>=d3sum):
    #     if (d1sum>=d3sum):
    #         res = 'Sim to Query is : \n(1) D2 with ratio = '+str(d2sum)+'\n(2) D1 with ratio = '+str(d1sum)+'\n(3) D3 with ratio = '+str(d3sum)+'\n'
    #         return res
    #     else:
    #         res = 'Sim to Query is : \n(1) D2 with ratio = '+str(d2sum)+'\n(2) D3 with ratio = '+str(d3sum)+'\n(3) D1 with ratio = '+str(d1sum)+'\n'
    #         return res
    # else:
    #     if (d3sum>=d1sum and d3sum>=d2sum):
    #         if (d1sum>=d2sum):
    #             res = 'Sim to Query is : \n(1) D3 with ratio = '+str(d3sum)+'\n(2) D1 with ratio = '+str(d1sum)+'\n(3) D2 with ratio = '+str(d2sum)+'\n'
    #             return res
    #         else:
    #             res = 'Sim to Query is : \n(1) D3 with ratio = '+str(d3sum)+'\n(2) D2 with ratio = '+str(d2sum)+'\n(3) D1 with ratio = '+str(d1sum)+'\n'
    #             return res
#Random String
def randString(length=10):
    letters='ABCDE12345'
    return ''.join((random.choice(letters) for i in range(length)))
#Write Generated Strings in files
def wrrd(p):
    s=randString()
    ss=s[0]
    for i in range(len(s)-1):
        ss=ss+" "+s[i+1]
    f = open(p,"w")
    f.write(ss)
    f.close()
#Graph
def grp(ahres):
    a=ahres[0]
    h=ahres[1]
    a.sort()
    h.sort()
    line_chart = pygal.Bar()
    line_chart.title = 'Authority and Hubness Weights'
    line_chart.x_labels = ['D1','D2','D3','D4','D5']
    line_chart.add('Authority', [a[0][1],a[1][1],a[2][1],a[3][1],a[4][1]])
    line_chart.add('Hubness', [h[0][1],h[1][1],h[2][1],h[3][1],h[4][1]])
    graph_data = line_chart.render_data_uri()
    return graph_data
###################################################
@app.route('/')
def index():
	return render_template('home.html')
###################################################
@app.route('/form', methods=['GET','POST'])
def form():
    #If ShowSim button clicked
    if 's' in request.form:
        s1=read("D:\My Projects\IR\Project 2\D1.txt")
        s2=read("D:\My Projects\IR\Project 2\D2.txt")
        s3=read("D:\My Projects\IR\Project 2\D3.txt")
        s4=read("D:\My Projects\IR\Project 2\D4.txt")
        s5=read("D:\My Projects\IR\Project 2\D5.txt")
        if request.method=='POST':
            x=request.form['x']
            y=query(x)
            if y==2:
                return 'Please, Insert a Valid Query!'
            res=Cal(s1,s2,s3,s4,s5,y)
            fres=show(res[0],res[1],res[2],res[3],res[4])
            ahres=Cal2(s1,s2,s3,s4,s5)
            gph=grp(ahres)
            a=ahres[0]
            h=ahres[1]
            a.sort(key=sortSecond,reverse=True)
            h.sort(key=sortSecond,reverse=True)
            return render_template('home.html',x=fres[0],y=fres[1],z=fres[2],c=fres[3],b=fres[4],a=a,h=h,graph_data=gph)
        else:
            return render_template('home.html')
    #If Random Generate button clicked
    else:
        wrrd("D:\My Projects\IR\Project 2\D1.txt")
        wrrd("D:\My Projects\IR\Project 2\D2.txt")
        wrrd("D:\My Projects\IR\Project 2\D3.txt")
        wrrd("D:\My Projects\IR\Project 2\D4.txt")
        wrrd("D:\My Projects\IR\Project 2\D5.txt")
        s1=read("D:\My Projects\IR\Project 2\D1.txt")
        s2=read("D:\My Projects\IR\Project 2\D2.txt")
        s3=read("D:\My Projects\IR\Project 2\D3.txt")
        s4=read("D:\My Projects\IR\Project 2\D4.txt")
        s5=read("D:\My Projects\IR\Project 2\D5.txt")
        if request.method=='POST':
            x=request.form['x']
            y=query(x)
            if y==2:
                return 'Please, Insert a Valid Query!'
            res=Cal(s1,s2,s3,s4,s5,y)
            fres=show(res[0],res[1],res[2],res[3],res[4])
            ahres=Cal2(s1,s2,s3,s4,s5)
            gph=grp(ahres)
            a=ahres[0]
            h=ahres[1]
            a.sort(key=sortSecond,reverse=True)
            h.sort(key=sortSecond,reverse=True)
            return render_template('home.html',x=fres[0],y=fres[1],z=fres[2],c=fres[3],b=fres[4],a=a,h=h,graph_data=gph)
        else:
            return render_template('home.html')
###################################################
if __name__ == '__main__':
	app.run(debug = True)
