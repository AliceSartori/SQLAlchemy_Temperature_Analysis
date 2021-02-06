# sqlalchemy

Honolulu, Here I come! Congratulations! 
You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area.

First, I decided to analyze the last 12 months of data. August, did I say to my boss? Not a great period to go to Hawaii. Precipitations are possible and more relevant compared to other months, also the Std in 2016 tells me that there is a lot of variability in the weather. Maybe, I'll bring an umbrella with me. 
Unfortunately, I have good data for August 2016, not a lot for 2017 to compare.

![Summary Statistics](https://github.com/AliceSartori/sqlalchemy/blob/main/Precipitations%20over%2012-month%20period.png)

![Summary Statistics](https://github.com/AliceSartori/sqlalchemy/blob/main/Precipitations%20over%2012%20months%20period_Summary%20Statistics.png)

Analyzing the temperature of Hawaii, plotting a boxplot allows me to have an understanding of the distribution of the datapoints from the median of all stations in quartiles.
#determine if there are any potential outliers across all the stations visually.
#
#I can see that there are multiple potential outliers in my temperature datapoints that could skew my data and further investigations 
#should be done.

![Summary Statistics](https://github.com/AliceSartori/sqlalchemy/blob/main/Temperatures%20over%20a%2012-month%20period.png)


![Summary Statistics](https://github.com/AliceSartori/sqlalchemy/blob/main/Temperature%20over%2012-month%20period%2C%20station%20USC00519281.png)

I get the sense that June would be a better month for my vacation and this is also suggested by the temperature analysis. Just to make sure that June would be a good month, I decide to run a statistical un-paired test between June and December data. If the pvalue is smaller 0.05, we can reject the null hypothesis and say statistical meaninful high difference between these groups. My pvalue is pvalue=3.9025129038616655e-191. 


![Summary Statistics](https://github.com/AliceSartori/sqlalchemy/blob/main/Trip%20Average%20Temp.png)




![Summary Statistics](https://github.com/AliceSartori/sqlalchemy/blob/main/Predicted%20Temperatures%20for%20Historical%20Temperature%20-%20Hawaii.png)

