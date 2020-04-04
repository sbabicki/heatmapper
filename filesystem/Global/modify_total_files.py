import os
import sys
import csv 

continents = ["Asia", "Europe", "North_America", "South_America", "Oceania","Africa"]

for root, dirs, files in os.walk(os.getcwd()):
    print root
    os.chdir(root)
    for file in files:
        if file == "accumulated.txt":
            os.remove(file)
    os.chdir("..")

headers = ["Name", "Confirmed", "Deaths", "Recovered", "Active", "Confirmed_per_capita", "Deaths_per_capita",
         "IFR_0.30_expected", "IFR_0.65_expected", "IFR_1.0_expected", "IFR_0.30_expected_per_capita", 
         "IFR_0.65_expected_per_capita", "IFR_1.0_expected_per_capita", "Date"]
for continent in continents:
    for root, dirs, files in os.walk(os.getcwd()+"/"+continent):
        print root
        os.chdir(root)
        if files:
            files.sort()
            for file in files:
                if file[-4:] == ".txt" and file != "accumulated.txt":
                    data = csv.reader(open(root+"/"+file, "rb"), delimiter = '\t')
                    print file
                    next(data)
                    for row in data:
                        if not os.path.exists(root+"/"+row[0].replace(" ","_")+"/"):
                            os.mkdir(root+"/"+row[0].replace(" ","_"))
                        with open(root+"/"+row[0].replace(" ","_")+"/"+"accumulated.txt",'a') as csv_file: 
                            writer = csv.writer(csv_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            if os.path.getsize(root+"/"+row[0].replace(" ","_")+"/"+"accumulated.txt") == 0:
                                writer.writerow(headers)
                            row.append(file[-14:-4])
                            writer.writerow(row)
        os.chdir("..")
    os.chdir("..")