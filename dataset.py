import pandas
import random

data=[]

for i in range(1000):
    age=random.randint(18,70)
    weight=random.randint(50,100)
    lastdonation=random.randint(0,365)
    bloodlevel=random.uniform(11.5,16.5)
    bloodpressure=random.choice(["Normal","High","Low"])
    illness=random.choice([1,0])
    disease=random.choice([0,1])
    eligible=((18<=age<=70)
              and(weight>=50 )and
              (lastdonation>90)and
              (bloodlevel>=11.5)and
              (bloodpressure=="Normal")and
              (illness==0)and
              (disease==0))

    data.append([age,weight,lastdonation,bloodlevel,bloodpressure,illness,disease,int(eligible)])
    count=0
    if int(eligible)==1:
        count+=1
print(count)

df=pandas.DataFrame(data,columns=["Age","Weight","LastDonation","BloodLevel","BloodPressure","Illness","Disease","Eligible"])
bp_map = {"Normal": 0, "High": 1, "Low": 2}
df["BloodPressure"] = df["BloodPressure"].map(bp_map)

df.to_csv("blooddonation_dataset.csv",index=False)
print("data saved")
