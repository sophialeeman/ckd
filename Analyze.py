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
    sug.append(float(row[4]))
    if row[5] == "normal":
        rbcu.append(0)
    if row[5] == "abnormal":
        rbcu.append(1)
    if row[6] == "normal":
        pus.append(0)
    if row[6] == "abnormal":
        pus.append(1)
    if row[7] == "notpresent":
        pcc.append(0)
    if row[7] == "present":
        pcc.append(1)
    if row[8] == "notpresent":
        bac.append(0)
    if row[8] == "present":
        bac.append(1)
    bgr.append(float(row[9]))
    bu.append(float(row[10]))
    sc.append(float(row[11]))
    na.append(float(row[12]))
    k.append(float(row[13]))
    hem.append(float(row[14]))
    pcv.append(float(row[15]))
    wbc.append(float(row[16]))
    rbc.append(float(row[17]))
    if row[18] == "no":
        hyp.append(0)
    if row[18] == "yes":
        hyp.append(1)
    if row[19] == "no":
        dia.append(0)
    if row[19] == "yes":
        dia.append(1)
    if row[20] == "no":
        cad.append(0)
    if row[20] == "yes":
        cad.append(1)
    if row[21] == "good":
        app.append(0)
    if row[21] == "poor":
        app.append(1)
    if row[22] == "no":
        ed.append(0)
    if row[22] == "yes":
        ed.append(1)
    if row[23] == "no":
        an.append(0)
    if row[23] == "yes":
        an.append(1)
    ckd.append(float(row[24]))
      
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
print("The percent change is")
print((ckdage - avage)/avage * 100)
#Blood Pressure
avbp = sum(bp)/len(bp)
print("The average bp is:")
print(avbp)
ckdbp = sum(bp[0:43])/len(bp[0:43])
print("The average bp for CKD patients is:")
print(ckdbp)
print("The percent change is")
print((ckdbp - avbp)/avbp * 100)
#Specific Gravity
avsg = sum(sg)/len(sg)
print("The average sg is:")
print(avsg)
ckdsg = sum(sg[0:43])/len(sg[0:43])
print("The average sg for CKD patients is:")
print(ckdsg)
print("The percent change is")
print((ckdsg - avsg)/avsg * 100)
#Albumin
aval = sum(al)/len(al)
print("The average al is:")
print(aval)
ckdal = sum(al[0:43])/len(al[0:43])
print("The average al for CKD patients is:")
print(ckdal) 
print("The percent change is")
print((ckdal - aval)/aval * 100)
#This shows the first striking difference, which is expected since Albuminuria is one of the main symptoms of CKD
#Sugar
avsug = sum(sug)/len(sug)
print("The average sug is:")
print(avsug)
ckdsug = sum(sug[0:43])/len(sug[0:43])
print("The average sug for CKD patients is:")
print(ckdsug)
print("The percent change is")
print((ckdsug - avsug)/avsug * 100)
#The same percent change as Albumin.
#Red Blood Cells in Urine
avrbcu = sum(rbcu)/len(rbcu)
print("The average rbcu is:")
print(avrbcu)
ckdrbcu = sum(rbcu[0:43])/len(rbcu[0:43])
print("The average rbcu for CKD patients is:")
print(ckdrbcu)
print("The percent change is")
print((ckdrbcu - avrbcu)/avrbcu * 100)
#The same percent change as Albumin and Sugar.
#Pus Cells in Urine
avpus = sum(pus)/len(pus)
print("The average pus is:")
print(avpus)
ckdpus = sum(pus[0:43])/len(pus[0:43])
print("The average pus for CKD patients is:")
print(ckdpus)
print("The percent change is")
print((ckdpus - avpus)/avpus * 100)
#Same percent change as Albumin, Sugar, and RBC.
#These results together show that the glomerular filtration barrier is deteriorated in CKD patients.
#Pus Cell Clumps
avpcc = sum(pcc)/len(pcc)
print("The average pcc is:")
print(avpcc)
ckdpcc = sum(pcc[0:43])/len(pcc[0:43])
print("The average pcc for CKD patients is:")
print(ckdpcc)
print("The percent change is")
print((ckdpcc - avpcc)/avpcc * 100)
#Same as al, sug, rbcu, and pus
#Bacteria
avbac = sum(bac)/len(bac)
print("The average bac is:")
print(avbac)
ckdbac = sum(bac[0:43])/len(bac[0:43])
print("The average bac for CKD patients is:")
print(ckdbac)
print("The percent change is")
print((ckdbac - avbac)/avbac * 100)
#Same as al, sug, rbcu, pus, and pcc
#Blood Glucose Random
avbgr = sum(bgr)/len(bgr)
print("The average bgr is:")
print(avbgr)
ckdbgr = sum(bgr[0:43])/len(bgr[0:43])
print("The average bgr for CKD patients is:")
print(ckdbgr)
print("The percent change is")
print((ckdbgr - avbgr)/avbgr * 100)
#Blood Urea
avbu = sum(bu)/len(bu)
print("The average bu is:")
print(avbu)
ckdbu = sum(bu[0:43])/len(bu[0:43])
print("The average bu for CKD patients is:")
print(ckdbu)
print("The percent change is")
print((ckdbu - avbu)/avbu * 100)
#This percent change is also quite high. 
#This also supports the breakdown of the glomerular filtration barrier, as proteins from the urine enter the bloodstream.
#Serum Creatinine
avsc = sum(sc)/len(sc)
print("The average sc is:")
print(avsc)
ckdsc = sum(sc[0:43])/len(sc[0:43])
print("The average sc for CKD patients is:")
print(ckdsc)
print("The percent change is")
print((ckdsc - avsc)/avsc * 100)
#Another high percent change. This makes sense, because properly working kidneys remove creatinine from the blood. 
#Sodium
avna = sum(na)/len(na)
print("The average na is:")
print(avna)
ckdna = sum(na[0:43])/len(na[0:43])
print("The average na for CKD patients is:")
print(ckdna)
print("The percent change is")
print((ckdna - avna)/avna * 100)
#Potassium
avk = sum(k)/len(k)
print("The average k is:")
print(avk)
ckdk = sum(k[0:43])/len(k[0:43])
print("The average k for CKD patients is:")
print(ckdk)
print("The percent change is")
print((ckdk - avk)/avk * 100)
#Hemoglobin
avhem = sum(hem)/len(hem)
print("The average hem is:")
print(avhem)
ckdhem = sum(hem[0:43])/len(hem[0:43])
print("The average hem for CKD patients is:")
print(ckdhem)
print("The percent change is")
print((ckdhem - avhem)/avhem * 100)
#Packed Cell Volume
avpcv = sum(pcv)/len(pcv)
print("The average pcv is:")
print(avpcv)
ckdpcv = sum(pcv[0:43])/len(pcv[0:43])
print("The average pcv for CKD patients is:")
print(ckdpcv)
print("The percent change is")
print((ckdpcv - avpcv)/avpcv * 100)
#WBC Count
avwbc = sum(wbc)/len(wbc)
print("The average wbc is:")
print(avwbc)
ckdwbc = sum(wbc[0:43])/len(wbc[0:43])
print("The average wbc for CKD patients is:")
print(ckdwbc)
print("The percent change is")
print((ckdwbc - avwbc)/avwbc * 100)
#Red Blood Cell Count
avrbc = sum(rbc)/len(rbc)
print("The average rbc is:")
print(avrbc)
ckdrbc = sum(rbc[0:43])/len(rbc[0:43])
print("The average rbc for CKD patients is:")
print(ckdrbc)
print("The percent change is")
print((ckdrbc - avrbc)/avrbc * 100)
#Hypertension
avhyp = sum(hyp)/len(hyp)
print("The average hyp is:")
print(avhyp)
ckdhyp = sum(hyp[0:43])/len(hyp[0:43])
print("The average hyp for CKD patients is:")
print(ckdhyp)
print("The percent change is")
print((ckdhyp - avhyp)/avhyp * 100)
#Same as al, sug, rbcu, pus, pcc, and bac
#Diabetes
avdia = sum(dia)/len(dia)
print("The average dia is:")
print(avdia)
ckddia = sum(dia[0:43])/len(dia[0:43])
print("The average dia for CKD patients is:")
print(ckddia)
print("The percent change is")
print((ckddia - avdia)/avdia * 100)
#Same as al, sug, rbcu, pus, pcc, bac, and hyp
#Coronary Artery Disease
avcad = sum(cad)/len(cad)
print("The average cad is:")
print(avcad)
ckdcad = sum(cad[0:43])/len(cad[0:43])
print("The average cad for CKD patients is:")
print(ckdcad)
print("The percent change is")
print((ckdcad - avcad)/avcad * 100)
#Same as al, sug, rbcu, pus, pcc, bac, hyp, and dia. This is way too much of a coincidence.
#Appetite
avapp = sum(app)/len(app)
print("The average app is:")
print(avapp)
ckdapp = sum(app[0:43])/len(app[0:43])
print("The average app for CKD patients is:")
print(ckdapp)
print("The percent change is")
print((ckdapp - avapp)/avapp * 100)
#Same as al, sug, rbcu, pus, pcc, bac, hyp, dia, and cad.
#Pedal Edema
aved = sum(ed)/len(ed)
print("The average ed is:")
print(aved)
ckded = sum(ed[0:43])/len(ed[0:43])
print("The average ed for CKD patients is:")
print(ckded)
print("The percent change is")
print((ckded - aved)/aved * 100)
#Same as al, sug, rbcu, pus, pcc, bac, hyp, dia, cad, and app.
#Anemia
avan = sum(an)/len(an)
print("The average an is:")
print(avan)
ckdan = sum(an[0:43])/len(an[0:43])
print("The average an for CKD patients is:")
print(ckdan)
print("The percent change is")
print((ckdan - avan)/avan * 100)
#Same as al, sug, rbcu, pus, pcc, bac, hyp, dia, cad, app, and an.
#Rate of ckd
avckd = sum(ckd)/len(ckd)
print("The average ckd is:")
print(avckd)