# prepare Titanic data for visualization

# Input format:
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

# Output format:
# Age,Sex,Survived,Number

import csv
from collections import defaultdict

with open('train.csv', 'rb') as csvfile:
    # map from age,sex,survived(y/n) to number of people who fit the category
    map = defaultdict(lambda:0)

    reader = csv.DictReader(csvfile)
    for row in reader:
        # 'bucketize' the age (0-9, 10-19, ...)
        if row['Age'] == '':
            age_bucket = "Unknown"
        elif float(row['Age']) >= 60:
            age_bucket = "60+";
        else:
            a = int(float(row['Age']) / 10)
            age_bucket = str(a * 10) + '-' + str ((a + 1) * 10)
        
        key =  age_bucket + '_' + row['Sex'].capitalize() + '_' + row['Pclass'] + '_' + ('Survived' if row['Survived'] == '1' else 'Died')
        map[key] += 1

with open('titanic.csv', 'wb') as csvfile:
    csvfile.write('Age,Sex,Class,Survived,Number\n')
    writer = csv.writer(csvfile)
    for key, cnt in map.iteritems():
        writer.writerow(key.split('_') + [cnt])
    