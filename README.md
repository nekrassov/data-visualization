#Summary
(in no more than 4 sentences, briefly introduce your data visualization and add any context that can help readers understand it)

My Project shows the Titanic disaster demographics or passenger information between those passengers who survived and those who died.
You can read more on Titanic disaster here: https://en.wikipedia.org/wiki/RMS_Titanic
The data used for visualization was retrieved from https://www.kaggle.com/c/titanic/download/train.csv
with column explanation at https://www.kaggle.com/c/titanic/data 


#Design
(explain any design choices you made including changes to the visualization after collecting feedback)

After looking at available data, I decided to show how **survival rate for men is different than that for women in different age groups.**

I approached the project iteratively, and at first I created visualization to show survival for different ages with no breakdown by sex.
I used bar chart with age on X axis, and number of people on Y axis.
I realized that even after rounding fractional ages, I still have too many distinct ages, so I decided to work on age *ranges*.
For each age range I showed two bars in different colours: one for number of people who died, another for people who survived.

The data that we have is structured on individual basis. For my visualization I needed aggregated numbers for each age range. 
Rather than aggregating data in JavaScript, I performed data aggregation outside of my web page, using Python script:

    ipython prep.py
    
At first I transformed data to the format:

    Age,NumSurvived,NumDied
    
but after I started dimple.js coding, I realized that it is better to use the format: 

    Age,Number,Survived(Yes/No)

This data format works well for bar chart with grouping by survived/died flag.

dimple.js gave me a free bonus of mouse hover-over displaying exact number in each bar.
This stage is captured in prep(1).py/index(1).html

For the next iteration of the project I added 'sex' information to the aggregated data, and switched to *stacked* bar chart, where each bar is split into two parts:
one for women, another for men. To distinguish bars for number of people who died vs. those who survived, I marked the bars with 'D' and 'S' respectively.
This stage is captured in prep.py/index(2).html

After collecting feedback, I decided to switch my chart type to proportional grouped vertical bar chart by changing Y axis from Measure to Pct (percent).
While this showed rate/percentage, I lost information about total count per group. To fix that, I added count label to each bar.
I also made the chart wider to give more space for my bar labels.

This version is captured in prep(3).py/index(3).html

In my opinion, proportional grouped vertical bar chart is good choice for my message 
because we can clearly see the difference in survival rate between men and women for different age groups. 
In particular, higher percent of women survived in each age group compared to percent of men who survived.
Bar chart is easy to understand, shows different age groups side by side, allowing direct comparison of survival rate between age groups.
Also, by adding simple number labels, I was able to preserve count information.

**After receiving reviewer's feedback, I made the following changes:**

+ fixed inconsistent indents in index.html
+ removed numbers from the chart
+ switched survived/died and sex attributes in the stacked bar chart; that removed ambiguity in chart interpretation
+ grouped ages above 60 to single group 60+
+ added animation through classes (with pause feature)
+ imposed order on series to have "Died" represented by red colour

#Feedback
(include all feedback you received from others on your visualization from the first sketch to the final visualization)

+ I received feedback that it is not obvious *what* I'm trying to communicate with my visualization. To address this, I added clear statement: that I want to __*"show how survival rate for men is different than that for women in different age groups"*__
+ I received feedback that percent survived/died for each group may better communicate my message. That led to switch to percent bar chart.
+ I received feedback that I need to justify my choice of chart type. That is now addressed at the end of the previous section.

#Resources
(list any sources you consulted to create your visualization)

In addition to the data source web site noted in the Summary above, I used the following resources:

+ dimple.js   http://dimplejs.org/
+ Python      https://docs.python.org/2/index.html