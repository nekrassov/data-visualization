# prepare Titanic data for visualization

# Input format:
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

# Output format:
# Age,Number,Survived

import csv
from collections import defaultdict

with open('train.csv', 'rb') as csvfile:
    # map from age to number of people who died or survived
    age_died = defaultdict(lambda:0)
    age_survived = defaultdict(lambda:0)

    reader = csv.DictReader(csvfile)
    for row in reader:
        # 'bucketize' the age (0-9, 10-19, ...)
        # -1 for unknown age
        if row['Age'] == '':
            age_bucket = "NA"
        else:
            age_bucket = int(float(row['Age']) / 10)
         
        if row['Survived'] == '1':
            age_survived[age_bucket] += 1
        else:
            age_died[age_bucket] += 1

    #print 'Survived: ', age_survived
    #print 'Died: ', age_died
            
with open('titanic.csv', 'wb') as csvfile:
    csvfile.write('Age,Number,Survived\n')
    
    writer = csv.writer(csvfile)

    # there are no ages in bucket 9 in our data, and xrange right bound is exclusive:
    for i in xrange(0, 9):
        #print i, age_survived[i], age_died[i]
        
        # convert age_bucket to age range
        writer.writerow([str(i*10) + "-" + str((i+1)*10), age_survived[i], "Survived"])
        writer.writerow([str(i*10) + "-" + str((i+1)*10), age_died[i], "Died"])

    # add entries for unknown age
    writer.writerow(["Unknown", age_survived["NA"], "Survived"])
    writer.writerow(["Unknown", age_died["NA"], "Died"])
