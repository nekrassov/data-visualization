# data-visualization

*** Summary
(in no more than 4 sentences, briefly introduce your data visualization and add any context that can help readers understand it)

My Project shows the Titanic disaster demographics or passenger information between those passengers who survived and those who died.
You can read more on Titanic disaster here: https://en.wikipedia.org/wiki/RMS_Titanic
The data used for visualization was retrieved from https://www.kaggle.com/c/titanic/download/train.csv
with column explanation at https://www.kaggle.com/c/titanic/data 


*** Design
explain any design choices you made including changes to the visualization after collecting feedback

After looking at available data columns, I decided to show survival for different ages.
I decided to use bar chart with Age on X axis, and number of people on Y axis.
For each Age (or Age group - will decide whether I need to group ages when I look closer at the data)
I will show two bars in different colours: one for number of people who died, another for people who survived.

A potential improvement of this visualization can be stacked bar chart, where each bar can be split into two parts:
one for women, another for men. To differentiate the two parts of the bar, I can use male/female symbol,
or use texture.

I will not attempt stacked bar chart at first.

With bar chart I can add mouse hover that shows number of men and women within each bar.

The data that we have is structured on individual basis. For my visualization I need numbers for each age. 
Rather than aggregating data in JavaScript, I will perform data aggregation outside of my web page, using Python script.

For my first iteration, I need data in the format "Age,NumSurvived,NumDied"

After I started preparing the data, I noticed that even after rounding fractional ages, I still have too many distinct ages,
so I decided to work on age ranges.

To prepare the data I run this script:
	ipython prep.py

After I started dimple coding, I realized that it is better to change from this format:
    AgeBucket,NumSurvived,NumDied
to:
    Age,Number,Survived
This data format works well for bar chart with grouping by survived/died flag.

dimple gave me a free bonus of mouse hover-over displaying exact number in each bar.
This stage is captured in prep(1).py/index(1).html
    
*** Feedback
include all feedback you received from others on your visualization from the first sketch to the final visualization


*** Resources
list any sources you consulted to create your visualization

In addition to the data source web site noted in the Summary above, I used the following resources:
dimple.js   http://dimplejs.org/
Python      https://docs.python.org/2/index.html
