course={"DAI":(60,300),"DUASP":(40,350),"DAC":(240,400)}
def addnewcourse():
    cname=input("enetr course name")
    capacity=int(input("enetr capacity"))
    duration=int(input("enter duration"))
    v=course.get(cname,-1)
    #if key is not there add it
    if v==-1:
        course[cname]=capacity,duration
        return True
    else:
        return False
    
#delete by name
def deletebyname(cname):
    if cname in course:
        ans=input(f"{cname}, {course[cname]} do you want to delete(y/n)?")
        if ans=="y":
            course.pop(cname)
            return 1
        else:
            return 2
    else:
        return 3
                  
#to update details of a course
def updatecourse(cname,capacity,duration):
    if cname in course:
        ans=input(f"{cname}, {course[cname]} do you want to update(y/n)?")
        if ans=="y":
            course[cname]=capacity,duration
            return 1
        else:
            return 2
    else:
        return 3

#find all courses with capacity >= given capacity
def findByCapacity(c):
    lst=[]
    for k,v in course.items():
        if v[0]>=c:
            lst.append((k,v))
    if len(lst)>0:
        return lst
    else:
        return None
     
def displaybycname(cname):
    if cname in course:
        return course[cname]
    else:
        return None
#display all the values from the given dictionary
def displayall():
    for k,v in course.items():
        print(f"{k}---->{v}")

#display data in sorted order of keys
def displayinsortedorder():
    for k in sorted(course.keys()):
        print(f"{k} ---> {course[k]}")

#to display course by duration
def displaybyduration(duration):
    for k,v in course.items():
        if v[1]==duration:
            print((k,v))





















        
