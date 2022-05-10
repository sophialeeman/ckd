#Read the csv file
import csv
file = open('ckd_clean.csv')
filereader = csv.reader(file)

#Headings
header = []
header = next(filereader)

#Create separate lists of records for each heading
#Assigning variables
#Age in Years
age = []
#Diastolic Blood Pressure in mm/Hg
bp = []
#Specific Gravity of Urine (one of 1.005,1.010,1.015,1.020,1.025)
sg = []
#Albumin in Urine (on a 5-point scale)
al = []
#Sugar in Urine (on a 5-point scale)
sug = []
#Red Blood Cells in Urine (normal or abnormal)
rbcu = []
#Pus Cell in Urine (normal or abnormal)
pus = []
#Pus Cell Clumps in Urine (present or not present)
pcc = []
#Bacteria in Urine (present or not present)
bac = []
#Blood Glucose Random (mgs/dl)
bgr = []
#Blood Urea (mgs/dl)
bu = []
#Serum Creatinine (mgs/dl)
sc = []
#Sodium (mEq/L)
na = []
#Potassium (mEq/L)
k = []
#Hemoglobin (gms)
hem = []
#Packed Cell Volume (%)
pcv = []
#White Blood Cell Count (cells/cumm)
wbc = []
#Red Blood Cell Count (millions/cmm)
rbc = []
#Hypertension (yes or no)
hyp = []
#Diabetes Mellitus (yes or no)
dia = []
#Coronary Artery Disease (yes or no)
cad = []
#Appetite (good or bad)
app = []
#Pedal Edema (yes or no)
ed = []
#Anemia (yes or no)
an = []
#Chronic Kidney Disease (1 for yes, 0 for no)
ckd = []
#Assigning data
for row in filereader:
    age.append(float(row[0]))
    bp.append(float(row[1]))
    sg.append(float(row[2]))
    al.append(float(row[3]))
    sug.append(row[4])
    rbcu.append(row[5])
    pus.append(row[6])
    pcc.append(row[7])
    bac.append(row[8])
    bgr.append(row[9])
    bu.append(row[10])
    sc.append(row[11])
    na.append(row[12])
    k.append(row[13])
    hem.append(row[14])
    pcv.append(row[15])
    wbc.append(row[16])
    rbc.append(row[17])
    hyp.append(row[18])
    dia.append(row[19])
    cad.append(row[20])
    app.append(row[21])
    ed.append(row[22])
    an.append(row[23])
    ckd.append(row[24])
      
file.close()

#Calculating Averages for Each Header Across the Whole Data Set and for CKD Patients Only
#Average Age Across Data Set
avage = sum(age)/len(age)
print("The average age is:") 
print(avage)
#Average Age of CKD Patients
ckdage = sum(age[0:43])/len(age[0:43]) #The first 43 subjects are ckd patients
print("The average age for CKD patients is:")
print(ckdage)
#Blood Pressure
avbp = sum(bp)/len(bp)
print("The average bp is:")
print(avbp)
ckdbp = sum(bp[0:43])/len(bp[0:43])
print("The average bp for CKD patients is:")
print(ckdbp)
#Specific Gravity
avsg = sum(sg)/len(sg)
print("The average sg is:")
print(avsg)
ckdsg = sum(sg[0:43])/len(sg[0:43])
print("The average sg for CKD patients is:")
print(ckdsg)
#Albumin
aval = sum(al)/len(al)
print("The average al is:")
print(aval)
ckdal = sum(al[0:43])/len(al[0:43])
print("The average al for CKD patients is:")
print(ckdal) 
#This shows the first striking difference, which is expected since Albuminuria is one of the main symptoms of CKD
