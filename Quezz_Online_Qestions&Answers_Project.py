#quiz
#questions={q1:"a",q2:"b" q3:"a"}
q1='''1.what is the capatial city of ap?
      a)Amaravathi b)Vizig c)Kurnool d)None'''
q2='''2.How to learn python easly?
      a)Talking to friend b)Sleeping c)100%Attadnce
      d)Practing e)c&d'''
q3='''3.Are we are eligible for software enginner?
       a)Yes b)No'''
questions={q1:"a",q2:"e",q3:"a"}
report={}
qno=1
for q in questions:
    print(q)
    ch=input("choose one options:")
    if ch==questions[q]:
        print("correct answer")
        report[qno]="correct"
    else:
        print("wrong answer")
        report[qno]="wrong"
    qno=qno+1
        
print("*"*10,"Report","*"*10)
for qno,v in report.items():
    print("Questions",qno,"--->",v)
    
