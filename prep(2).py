# prepare Titanic data for visualization

# Input format:
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

# Output format:
# Age,Number,Survived

import csv
from collections import defaultdict

with open('train.csv', 'rb') as csvfile:
    # map from age to number of people who died or survived
    age_died_m = defaultdict(lambda:0)
    age_died_f = defaultdict(lambda:0)
    age_survived_m = defaultdict(lambda:0)
    age_survived_f = defaultdict(lambda:0)

    reader = csv.DictReader(csvfile)
    for row in reader:
        # 'bucketize' the age (0-9, 10-19, ...)
        # -1 for unknown age
        if row['Age'] == '':
            age_bucket = "NA"
        else:
            age_bucket = int(float(row['Age']) / 10)
         
        if row['Survived'] == '1' and row['Sex'] == 'male':
            age_survived_m[age_bucket] += 1
        elif row['Survived'] == '1' and row['Sex'] == 'female':
            age_survived_f[age_bucket] += 1
        elif row['Sex'] == 'male':
            age_died_m[age_bucket] += 1
        else:
            age_died_f[age_bucket] += 1

with open('titanic.csv', 'wb') as csvfile:
    csvfile.write('Age,Number,Survived,Sex\n')
    
    writer = csv.writer(csvfile)

    # there are no ages in bucket 9 in our data, and xrange right bound is exclusive:
    for i in xrange(0, 9):
        # convert age_bucket to age range
        writer.writerow([str(i*10) + "-" + str((i+1)*10), age_survived_m[i], "Yes", "Male"])
        writer.writerow([str(i*10) + "-" + str((i+1)*10), age_died_m[i], "No", "Male"])
        writer.writerow([str(i*10) + "-" + str((i+1)*10), age_survived_f[i], "Yes", "Female"])
        writer.writerow([str(i*10) + "-" + str((i+1)*10), age_died_f[i], "No", "Female"])

    # add entries for unknown age
    writer.writerow(["Unknown", age_survived_m["NA"], "Yes", "Male"])
    writer.writerow(["Unknown", age_died_m["NA"], "No", "Male"])
    writer.writerow(["Unknown", age_survived_f["NA"], "Yes", "Female"])
    writer.writerow(["Unknown", age_died_f["NA"], "No", "Female"])
