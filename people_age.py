import csv

f=open("path/people_age.csv")
main_data = csv.reader(f)
#print(main_data)

p_age=[]
for idx,i in enumerate(main_data):
    p_age.append(i)
f.close()

max=0
index=0

for idx,i in enumerate(p_age[1:]):
    try:
        #print(i[0][-7:-1])
        if i[0][-7:-1].count('0') < 5:
            if max<int(i[1].replace(',', '')):
                max=int(i[1].replace(',', ''))
                index=idx+1
    except ValueError as e: print(e)
    except AttributeError as e: print(e)
            
#print(p_age[index][0],p_age[index][1])

max_chart=[]
for i in p_age[index][3:104]:
    max_chart.append(int(i.replace(',', '')))    
    
plt.plot(max_chart)
