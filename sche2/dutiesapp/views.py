from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse
from .models import teacher
from .models import exam
from random import shuffle
import random
teachdict1={}
teachdict2={}
teachdict3={}
invidict={}
reldict={}
acsdict={}
dsdict={}
examdict={}
nsessions=0




def home(request):
    return render(request,'dutiesapp/home.html')

def validate(request):
    insert=request.POST.get("insert")
    delete = request.POST.get("delete")
    display = request.POST.get("display")
    calculate=request.POST.get("calculate")
    schedule=request.POST.get("schedule")
    query=request.POST.get("query")
    dates=request.POST.get("dates")
    update=request.POST.get("update")
    context={}
    d={}
    j=0
    if insert:
        return render(request,"dutiesapp/create.html")
    if delete:
        return render(request,"dutiesapp/delete.html")
    if display:
        #template = loader.get_template('dutiesapp/display.html')
        o = teacher.objects.all()
        tdict={}
        for i in o:
            l=[]
            l.append(i.initials)

            l.append(i.department)
            l.append(i.designation)
            tdict[i.id]=l

        context['tdict']=tdict



        return render(request, "dutiesapp/display.html", context)
    if calculate:
        return  render(request,"dutiesapp/calculate.html")
    if schedule:
        return render(request,"dutiesapp/schedule.html")

    if query:
        return render(request,"dutiesapp/query.html")
    if dates:
        return render(request,"dutiesapp/dates.html")
    if update:
        return render(request,"dutiesapp/update.html")
def add(request):
    a=teacher()
    a.initials=request.POST.get('initials')
    a.department=request.POST.get('department')
    a.designation=request.POST.get('designation')



    a.save()
    return render(request,"dutiesapp/create.html")

def dele(request):
    name=request.POST.get('initials')
    teacher.objects.filter(initials=name).delete()
    return render(request,"dutiesapp/delete.html")



def cal(request):
    exam.objects.all().delete()
    ndays=int(request.POST.get('ndays'))
    nsessions=int(request.POST.get('nsessions'))

    total=0
    totalds=0
    totalacs=0
    for i in range(nsessions):
        b=exam()
        date1=request.POST.get("d"+str(i+1))
        ap1=request.POST.get("ap"+str(i+1))
        datetime=date1+ap1
        b.date=datetime
        b.n_students=request.POST.get("s"+str(i+1))
        b.n_rooms=request.POST.get("r"+str(i+1))
        r1="r"+str(i+1)
        n_rs=int(request.POST.get("r"+str(i+1)))
        b.n_rs=n_rs;
        rel=(n_rs)/5;
        rel1=int(n_rs/5);

        if rel-rel1>=0.2:
            if n_rs!=2:
                relfinal=rel1+1
            else:
                relfinal=rel1
        else:
            relfinal=rel1
        b.n_relief=relfinal
        total=total+relfinal
        total=total+n_rs

        ds=n_rs/10
        ds1=int(n_rs/10)
        if ds-ds1>0:
            dsfinal=ds1+1
        else:
            dsfinal=ds1;
        b.n_ds=dsfinal
        totalds=totalds+dsfinal

        acs=1
        if n_rs>4:
            acs=1
        else:
            acs=0
        b.n_acs=acs;
        totalacs=totalacs+acs
        b.save()
    o1=teacher.objects.filter(designation='Associate').filter(Flag=0)
    o2=teacher.objects.filter(designation="Assistant").filter(Flag=0)
    o3=teacher.objects.filter(designation="Associate(prob)").filter(Flag=0)

    o5=teacher.objects.filter(designation="Probitionary").filter(Flag=0)
    o6=teacher.objects.filter(designation="H.O.D").filter(Flag=0)
    o7=teacher.objects.filter(designation="Professor").filter(Flag=0)
    o8=teacher.objects.filter(designation="Professor(prob)").filter(Flag=0)
    
    n_assoc=4
    n_assocprob=4
    rem=total-len(o1)*n_assoc-len(o3)*n_assocprob
    n_assis1=rem/len(o2);
    n_assisabs=int(rem/len(o2))
    if n_assisabs>=5:
        n_assis=5
    elif n_assis1-n_assisabs>0:
        n_assis=n_assisabs+1
    else:
        n_assis=n_assisabs
    remprob=total-len(o1)*n_assoc-len(o3)*n_assocprob-len(o2)*n_assis
    n_prob=0
    if remprob>0:
        n_prob1=remprob/len(o5);
        n_probabs=int(remprob/len(o5))
        if n_probabs>=6:
            n_prob=6
        elif n_prob1-n_probabs>0:
            n_prob=n_probabs+1
        else:
            n_prob=n_probabs

    n_prof=6
    remprofd=totalds-n_prof*len(o7);

    z=remprofd/len(o8)
    
    z1=int(z)
    n_profprob=6
    # if z-z1>0:
    #     n_profprob=int(remprofd/len(o8))+1

    for i in o1:
        i.n_duties=n_assoc;
        i.save()
    for i in o2:
        i.n_duties=n_assis;
        i.save()
    for i in o3:
        i.n_duties=n_assocprob;
        i.save()
    for i in o5:
        i.n_duties=n_prob;
        i.save()
    for i in o6:
        i.n_duties=2;
        i.save()
    for i in o7:
        i.n_duties=n_prof;
        i.save()
    for i in o8:
        i.n_duties=n_profprob;
        i.save()


    return render(request,"dutiesapp/calculate.html")

def sche(request):
    totaltea=teacher.objects.all()
    for i in totaltea:
        i.n_am=0
        i.n_pm=0
        i.n_dutiesassigned=0
        i.n_relief=0
        i.save()
    context={}
    random.seed(4)
    o1=list(teacher.objects.filter(designation="Associate").filter(Flag=0))
    shuffle(o1)
    o2=list(teacher.objects.filter(designation="Associate(prob)").filter(Flag=0))
    shuffle(o2)
    o3=list(teacher.objects.filter(designation="Assistant").filter(Flag=0))
    shuffle(o3)
    o4=list(teacher.objects.filter(designation="Probitionary").filter(Flag=0))
    shuffle(o4)
    o5=list(teacher.objects.filter(designation="H.O.D").filter(Flag=0))
    shuffle(o5)
    o6=list(teacher.objects.filter(designation="Professor").filter(Flag=0))
    shuffle(o6)
    o7=list(teacher.objects.filter(designation="Professor(prob)").filter(Flag=0))
    shuffle(o7)

    b1=1
    for i in o1:
        l=[]
        l.append(i.initials)
        l.append(i.department)
        l.append(i.designation)
        l.append(i.n_duties)
        l.append(i.n_dutiesassigned)
        l.append(i.n_am)
        l.append(i.n_pm)
        l.append(i.n_relief)
        l.append(i.n_dates)
        l.append(i.leaves)
        l.append(int(i.id))
        teachdict1[b1]=l;
        b1+=1
    for i in o2:
        l=[]
        l.append(i.initials)
        l.append(i.department)
        l.append(i.designation)
        l.append(i.n_duties)
        l.append(i.n_dutiesassigned)
        l.append(i.n_am)
        l.append(i.n_pm)
        l.append(i.n_relief)
        l.append(i.n_dates)
        l.append(i.leaves)
        l.append(int(i.id))
        teachdict1[b1]=l;
        b1+=1
    for i in o3:
        l=[]
        l.append(i.initials)
        l.append(i.department)
        l.append(i.designation)
        l.append(i.n_duties)
        l.append(i.n_dutiesassigned)
        l.append(i.n_am)
        l.append(i.n_pm)
        l.append(i.n_relief)
        l.append(i.n_dates)
        l.append(i.leaves)
        l.append(int(i.id))
        teachdict1[b1]=l;
        b1+=1
    for i in o4:
        l=[]
        l.append(i.initials)
        l.append(i.department)
        l.append(i.designation)
        l.append(i.n_duties)
        l.append(i.n_dutiesassigned)
        l.append(i.n_am)
        l.append(i.n_pm)
        l.append(i.n_relief)
        l.append(i.n_dates)
        l.append(i.leaves)
        l.append(int(i.id))
        teachdict1[b1]=l;
        b1+=1
    b2=1
    for i in o5:
        l=[]
        l.append(i.initials)
        l.append(i.department)
        l.append(i.designation)
        l.append(i.n_duties)
        l.append(i.n_dutiesassigned)
        l.append(i.n_am)
        l.append(i.n_pm)
        l.append(i.n_relief)
        l.append(i.n_dates)
        l.append(i.leaves)
        l.append(int(i.id))
        teachdict2[b2]=l;
        b2+=1
    b3=1
    for i in o6:
        l=[]
        l.append(i.initials)
        l.append(i.department)
        l.append(i.designation)
        l.append(i.n_duties)
        l.append(i.n_dutiesassigned)
        l.append(i.n_am)
        l.append(i.n_pm)
        l.append(i.n_relief)
        l.append(i.n_dates)
        l.append(i.leaves)
        l.append(int(i.id))
        teachdict3[b3]=l;
        b3+=1
    for i in o7:
        l=[]
        l.append(i.initials)
        l.append(i.department)
        l.append(i.designation)
        l.append(i.n_duties)
        l.append(i.n_dutiesassigned)
        l.append(i.n_am)
        l.append(i.n_pm)
        l.append(i.n_relief)
        l.append(i.n_dates)
        l.append(i.leaves)
        l.append(int(i.id))
        teachdict3[b3]=l;
        b3+=1
    e=exam.objects.all()
    e1=1
    for i in e:
        l=[]

        l.append(i.n_students)
        l.append(i.n_rooms)
        l.append(i.n_acs)
        l.append(i.n_ds)
        l.append(i.n_rs)
        l.append(i.n_relief)

        examdict[i.date]=l

    a1=1
    for i,j in examdict.items():
        rellist=[]
        for k in range(j[5]):
            while a1 in rellist or teachdict1[a1][7]==1 or teachdict1[a1][4]>=teachdict1[a1][3] or i[:-2] in teachdict1[a1][8] or i in teachdict1[a1][9] or teachdict1[a1][2]=="Probitionary":
                if a1<len(teachdict1):
                    a1=a1+1
                else:
                    a1=1
            teachdict1[a1][7]=1
            teachdict1[a1][4]+=1
            if i[-2:]=='pm':
                teachdict1[a1][6]+=1
            if i[-2:]=='am':
                teachdict1[a1][5]+=1
            rellist.append(a1)
            if a1<len(teachdict1):
                a1=a1+1
            else:
                a1=1
        reldict[i]=rellist

    a1=1
    invilist=[]
    for i,j in examdict.items():
        if i[-2:]=='am':
            invilist=[]
        dateam=i[:-2]+"am"
        datepm=i[:-2]+"pm"
        l1=[]
        l2=[]
        if dateam in reldict.keys():
            l1=reldict[dateam]
        if datepm in reldict.keys():
            l2=reldict[datepm]


        for k in range(j[4]):
            while a1 in invilist or a1 in l1 or a1 in l2 or teachdict1[a1][4]>=teachdict1[a1][3]or i[:-2] in teachdict1[a1][8]or i in teachdict1[a1][9]:
                if a1<len(teachdict1):
                    a1=a1+1
                else:
                    a1=1

            teachdict1[a1][4]+=1
            if i[-2:]=='pm':
                teachdict1[a1][6]+=1
            if i[-2:]=='am':
                teachdict1[a1][5]+=1
            invilist.append(a1)
            if a1<len(teachdict1):
                a1=a1+1
            else:
                a1=1

        if i[-2:]=="am":
            nrsam=j[4]
            invidict[i]=invilist[:j[4]]
        elif i[-2:]=="pm":
            invidict[i]=invilist[nrsam:]

            invilist=[]

    # for ds
    a1=1
    dslist=[]
    for i,j in examdict.items():
        date1=i
        if i[-2:]=='am':
            dslist=[]
        for k in range(j[3]):
            while a1 in dslist or teachdict3[a1][4]>=teachdict3[a1][3]or i in teachdict3[a1][9]or i[:-2] in teachdict3[a1][8]:
                if a1<len(teachdict3):
                    a1=a1+1
                else:
                    a1=1

            teachdict3[a1][4]+=1
            if i[-2:]=='pm':
                teachdict3[a1][6]+=1
            if i[-2:]=='am':
                teachdict3[a1][5]+=1
            dslist.append(a1)
            if a1<len(teachdict3):
                a1=a1+1
            else:
                a1=1
        if i[-2:]=="am":
            ndsam=j[3]
            dsdict[i]=dslist[:j[3]]
        elif i[-2:]=="pm":
            dsdict[i]=dslist[ndsam:]

            dslist=[]
    a1=1
    acslist=[]
    for i,j in examdict.items():
        if i[-2:]=='am':
            acslist=[]
        for k in range(j[2]):
            while a1 in acslist or teachdict2[a1][4]>=teachdict2[a1][3]or i[:-2] in teachdict2[a1][8]or i in teachdict2[a1][9]:
                if a1<len(teachdict2):
                    a1=a1+1
                else:
                    a1=1

            teachdict2[a1][4]+=1
            if i[-2:]=='pm':
                teachdict2[a1][6]+=1
            if i[-2:]=='am':
                teachdict2[a1][5]+=1
            acslist.append(a1)
            if a1<len(teachdict2):
                    a1=a1+1
            else:
                a1=1
        if i[-2:]=="am":
            nacsam=j[2]
            acsdict[i]=acslist[:j[2]]
        elif i[-2:]=="pm":
            acsdict[i]=acslist[nacsam:]

            acslist=[]
    datedict={}
    for i,j in examdict.items():
        if i[:-2] not  in datedict.keys():
            datedict[i[:-2]]=1
        else:
            datedict[i[:-2]]+=1

    context['a']=teachdict1;
    context['b']=teachdict2;
    context['c']=teachdict3;
    context['d']=examdict;
    context['e']=reldict;
    context['f']=invidict;
    context['g']=dsdict;
    context['l1']=acsdict;
    context['datedict']=datedict;
    context['h']=len(invidict[date1])
    context['nsessions']=len(examdict.keys());
    totalteac=teacher.objects.all().filter(Flag=0)

    for i,j in teachdict1.items():
        k2=teacher.objects.filter(id=j[10]).filter(Flag=0)
        for k1 in k2:
            k1.n_am=teachdict1[i][5]
            k1.n_pm=teachdict1[i][6]
            k1.n_dutiesassigned=teachdict1[i][4]
            k1.n_relief=teachdict1[i][7]
            k1.save()
    for i,j in teachdict2.items():
        k2=teacher.objects.filter(id=j[10]).filter(Flag=0)
        for k1 in k2:
            k1.n_am=teachdict2[i][5]
            k1.n_pm=teachdict2[i][6]
            k1.n_dutiesassigned=teachdict2[i][4]
            k1.n_relief=teachdict2[i][7]
            k1.save()
    for i,j in teachdict3.items():
        k2=teacher.objects.filter(id=j[10]).filter(Flag=0)
        for k1 in k2:
            k1.n_am=teachdict3[i][5]
            k1.n_pm=teachdict3[i][6]
            k1.n_dutiesassigned=teachdict3[i][4]
            k1.n_relief=teachdict3[i][7]
            k1.save()

    return render(request,"dutiesapp/sche2.html",context);



def que(request):

    name=request.POST.get("name")
    dept=request.POST.get("department")
    o10=teacher.objects.filter(initials=name, department=dept)
    for i in o10:
        designation=i.designation

    dict={"RS duties":[],"DS duties":[],"Relief duties":[],"ACS duties":[]}
    count=0
    for i,j in invidict.items():
        for k,l in teachdict1.items():
            if k in j:
                if l[0]==name and l[1]==dept:
                    count=count+1
                    dict["RS duties"].append(i)


    for i,j in reldict.items():
        for k,l in teachdict1.items():
            if k in j:
                if l[0]==name and l[1]==dept:
                    count=count+1
                    dict["Relief duties"].append(i)


    for i,j in dsdict.items():
        for k,l in teachdict3.items():
            if k in j:
                if l[0]==name and l[1]==dept:
                    count=count+1
                    dict["DS duties"].append(i)


    for i,j in acsdict.items():
        for k,l in teachdict2.items():
            if k in j:
                if l[0]==name and l[1]==dept:
                    count=count+1
                    dict["ACS duties"].append(i)
    l=[len(dict['ACS duties']),len(dict['DS duties']),len(dict['RS duties']),len(dict['Relief duties'])]

    return render(request,"dutiesapp/query2.html",{"dict":dict,"name":name,"dept":dept,"l":l,"designation":designation})






from datetime import timedelta, date
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def dates(request):
    name=request.POST.get("initials")
    department=request.POST.get("department")
    print(name)
    print(department)

    total_dates=int(request.POST.get("total_dates"))
    # print("Total dates--------------"+str(total_dates))
    total_ranges=int(request.POST.get("total_ranges"))
    l=[]
    for i in range(total_dates):

        a=request.POST.get("date"+str(i+1))
        # print(a)
        l.append(a)
    print(l)
    for i in range(total_ranges):

        a11=request.POST.get("range"+str(i+1)+"1")
        a21=request.POST.get("range"+str(i+1)+"2")
        a1=date(int(a11[:4]),int(a11[5:7]),int(a11[8:]))
        a2=date(int(a21[:4]),int(a21[5:7]),int(a21[8:]))


        for dt in daterange(a1,a2):
              l.append(dt.strftime("%Y-%m-%d"))


    a=teacher.objects.filter(initials=name).filter(department=department).filter(Flag=0)
    for i in a:
        print(i)
        print("Heloooo")
        i.n_dates=l
        i.save();
    return render(request,"dutiesapp/dates.html",{'a':a});


def datesconfidential(request):
    name=request.POST.get("initials1")
    department=request.POST.get("department1")

    total_dates=int(request.POST.get("total_dates1"))
    total_ranges=int(request.POST.get("total_ranges1"))
    l=[]
    for i in range(total_dates):

        a=request.POST.get("date"+str(i+1))
        ap=request.POST.get("ap"+str(i+1))
        a=a+ap
        l.append(a)
    for i in range(total_ranges):

        a11=request.POST.get("range"+str(i+1)+"1")
        a21=request.POST.get("range"+str(i+1)+"2")
        a1=date(int(a11[:4]),int(a11[5:7]),int(a11[8:]))
        a2=date(int(a21[:4]),int(a21[5:7]),int(a21[8:]))

        rap=request.POST.get("rap"+str(i+1))
        print(rap)
        for dt in daterange(a1,a2):
            l.append(dt.strftime("%Y-%m-%d")+str(rap))


    a=teacher.objects.filter(initials=name,department=department).filter(Flag=0);
    for i in a:
        i.leaves=l
        i.save();
    return render(request,"dutiesapp/dates.html",{'a':a});

def update(request):

    name=request.POST.get("initials")
    department=request.POST.get("department")

    fieldname=request.POST.get("fieldname")

    if fieldname=="initials":
        newinitials=request.POST.get("newinitials")
        a=teacher.objects.filter(initials=name,department=department);
        for i in a:
            i.initials=newinitials
            i.save()

    if fieldname=="designation":
        newdesignation=request.POST.get("newdesignation")
        a=teacher.objects.filter(initials=name,department=department);
        for i in a:
            i.designation=newdesignation
            i.save()


    if fieldname=="department":
        newdepartment=request.POST.get("newdepartment")
        a=teacher.objects.filter(initials=name,department=department);
        for i in a:
            i.department=newdepartment
            i.save()
    return render(request,"dutiesapp/update.html")


# Create your views here.
