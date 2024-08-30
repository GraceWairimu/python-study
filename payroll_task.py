# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 

def get_gross(basicsalary,benefit):
    gross_salary=basicsalary+benefit
    return gross_salary

basic_salary=float(input("Enter the basic salary: "))
benefits=float(input("Enter the benefits: "))
gross=get_gross(basic_salary,benefits)
print(gross)

def get_nhif(gross_salary):

    if gross_salary>=100000:
        nhif=1700
    elif gross_salary>=90000:
        nhif=1600
    elif gross_salary>=80000:
        nhif=1500
    elif gross_salary>=70000:
        nhif=1400
    elif gross_salary>=60000:
        nhif=1300
    elif gross_salary>=50000:
        nhif=1200
    elif gross_salary>=45000:
        nhif=1100
    elif gross_salary>=40000:
        nhif=1000
    elif gross_salary>=35000:
        nhif=950
    elif gross_salary>=30000:
        nhif=900
    elif gross_salary>=25000:
        nhif=850
    elif gross_salary>=20000:
        nhif=750
    elif gross_salary>=15000:
        nhif=600
    elif gross_salary>=12000:
        nhif=500
    elif gross_salary>=8000:
        nhif=400
    elif gross_salary>=6000:
        nhif=300
    else:
        nhif=150

    return nhif

NHIF=get_nhif(gross)
print(f"NHIF is {NHIF}")

# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 

def get_nssf(gross_salary):
    if gross_salary<=6000:
        nssf=0.06*6000
    elif gross_salary>=18000:
        nssf=0.06*18000
    else:
        nssf=0.06*gross_salary

    return nssf

NSSF=get_nssf(gross)
print(f"NSSF is {NSSF}")

# Task 17: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015

# def get_nhdf(gross_salary):
#     nhdf=gross_salary*0.015

#     return nhdf

    # OR
def get_nhdf(gross_salary,rate=0.015): #Using default parameter rate
    nhdf=gross_salary*rate

    return nhdf

NHDF=get_nhdf(gross)
print(f"NHDF is {NHDF}")


# Task 18: Using Python or PHP or Java or Ruby or JavaScript
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 

def get_taxableincome(gross_salary,nssf,nhdf,nhif):
    taxableincome=gross_salary-(nssf+nhdf+nhif)

    return taxableincome

taxable_income=get_taxableincome(gross,NSSF,NHDF,NHIF)
print(f"Taxable income is {taxable_income}")

# TASK 19: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK

# def get_payee(taxable_income):
#     remainder=0
#     payee=0
#     if taxable_income<=24000:
#         payee=0
#     else:
#         payee=0.10*24000
#         remainder=taxable_income-24000
#     if remainder>0:
#         if remainder>8333:
#             payee=payee+(0.25*8333)
#             remainder=remainder-8333
#         else:
#             payee=payee+(0.25*remainder)
#             remainder=0
#     if remainder>0:
#         if remainder>467667:
#             payee=payee+(0.25*467667)
#             remainder=remainder-467667
#         else:
#             payee=payee+(0.3*remainder)
#             remainder=0
#     if remainder>0:
#         if remainder>300000:
#             payee=payee+(0.325*300000)
#             remainder=remainder-300000
#         else:
#             payee=payee+(0.325*remainder)
#             remainder=0

#     if remainder>0:
#         payee=0.35*remainder

#     return payee
       
    #    OR

def get_payee(taxable_income,relief=2400):
    if taxable_income<=24000:
        payee=0
    elif taxable_income>24000 and taxable_income<=32333:
        payee=(24000*0.1)+((taxable_income-24000)*0.25)-relief
    elif taxable_income>32333 and taxable_income<=500000:
        payee=(24000*0.1)+(8333*0.25)+((taxable_income-32333)*0.3)-relief
    elif taxable_income>500000 and taxable_income<=800000:
        payee=(24000*0.1)+(8333*0.25)+(467667*0.3)+((taxable_income-500000)*0.325)-relief
    else:
        payee=(24000*0.1)+(8333*0.25)+(467667*0.3)+(300000*0.325)+((taxable_income-800000)*0.35)-relief
        
    return payee

PAYEE=get_payee(taxable_income)
PAYEE=round(PAYEE,2)
print(f"PAYEE is {PAYEE}")
# Task 20: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee-relief)

# relief=2400
def get_netsalary(gross_salary,nhif,nhdf,nssf,payee):

    netsalary=gross_salary-(nhif+nhdf+nssf+payee)
    return netsalary

net_salary=get_netsalary(gross,NHIF,NHDF,NSSF,PAYEE)
print(f"The NET SALARY is {net_salary}")