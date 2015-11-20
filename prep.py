# prepare Titanic data for visualization

# Input format:
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

# Output format:
# Age,Sex,Class,PctSurvived

import csv
from collections import defaultdict

with open('train.csv', 'rb') as csvfile:
    # map from age,sex,class to number of people who fit the category
    map_surv = defaultdict(lambda:0)
    map_died = defaultdict(lambda:0)

    reader = csv.DictReader(csvfile)
    for row in reader:
        # 'bucketize' the age
        if row['Age'] == '':
            #age_bucket = "Unknown"
            # exclude this from plotting
            continue
        elif float(row['Age']) >= 55:
            age_bucket = '55+';
        elif float(row['Age']) >= 26:
            age_bucket = '26-54'
        elif float(row['Age']) >= 19:
            age_bucket = '19-25'
        elif float(row['Age']) >= 13:
            age_bucket = '13-18'
        else:
            age_bucket = '<13'
        
        key =  age_bucket + '_' + row['Sex'].capitalize() + '_' + row['Pclass']
        if row['Survived'] == '1':
            map_surv[key] += 1
        else:
            map_died[key] += 1

with open('titanic.csv', 'wb') as csvfile:
    csvfile.write('Age,Sex,Class,PctSurvived\n')
    writer = csv.writer(csvfile)
    all_keys = set(map_surv.keys() + map_died.keys())
    for key in all_keys:
        d = map_died[key]
        s = map_surv[key]
        pct = 100 * round(float(s) / float(d + s), 2)
        if pct == 0:
            pct = 1
        writer.writerow(key.split('_') + [pct])
    