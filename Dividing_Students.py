#Dividing Students for sections program
no_students=int(input("Enter no of students:"))
no_sections=int(input("Enter no of students:"))
each_section=no_students//no_sections
extra=no_students%no_sections
i=1
while i<=no_sections:
    if i==no_sections:
        print("Sections",i,"---",each_section+extra)
    else:
        print("Section",i,"---",each_section)
    i=i+1
        
