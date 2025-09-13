class students:
    institute="jspiders"
    std_fees=[]
    def __init__(self,name,age,m1,m2,f):
        self.name=name
        self.age=age
        self.english_marks=m1
        self.maths_marks=m2
        students.std_fees.append(f)
    def info(self):
        print(self.name,self.age)
    def getavg(self):
        return (self.english_marks+self.maths_marks)//2
    def getgrade(self):
        avg=self.getavg()
        if avg>70:
            grade="A+"
        elif avg>60:
            grade="A"
        elif avg>50:
            grade="B"
        else:
            grade="C"
        msg="{} has secured {} grade".format(self.name,grade)
        return msg
    
    @classmethod
    def getrevenue(cls):
        rev=sum(cls.std_fees)
        msg="{} has generated revenue of {} ruppes".format(cls.institute,rev)
        return msg
s1=students("raju",22,45,54,45000)
s2=students("shiva",21,67,54,5000)
s1.info()
s1.getavg()
s1.getgrade()
rev=students.getrevenue()
print(rev)

        
        
