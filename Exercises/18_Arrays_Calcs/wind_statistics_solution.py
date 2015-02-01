""" 
Wind Statistics
----------------

Topics: Using array methods over different axes, fancy indexing.

1. The data in 'wind.data' has the following format::

        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71
   
   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   cities in Ireland on that day.
   
   Use the 'loadtxt' function from numpy to read the data into
   an array.

2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds in Ireland.  In other words, reduce all the wind measurements
   from all the days and all the locations to a single set of statistics 
   for the entire dataset. 

3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds for each of the cities (columns).  You should end up with 12
   results for each of the statistics.
   
4. Calculate the min, max and mean windspeed and standard deviations of the 
   windspeeds for every day (rows) in the data set.  Here you'll reduce all 
   the cities numbers to a set of statistics for each day.  There a thousands
   of days, so your resulting data sets will be large.
   
5. Find the city which has the greatest windspeed on each day 
   (an integer column number for each day). 

6. Find the year, month and day on which the greatest windspeed was recorded.

7. Find the average windspeed in January for each city.

You should be able to perform all of these operations without using a for
loop or other looping construct.

Bonus
~~~~~

1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (It's ok to use
   a loop in this one.)


Notes
~~~~~

These data were analyzed in detail in the following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.

"""

from numpy import loadtxt, arange, searchsorted, add, zeros

wind_data = loadtxt('wind.data')

data = wind_data[:,3:]

print '2. Statistics over all values'
print '  min:', data.min()
print '  max:', data.max()
print '  mean:', data.mean()
print '  standard deviation:', data.std()
print

print '3. Statistics at each city (over all days)'
print '  min:', data.min(axis=0)
print '  max:', data.max(axis=0)
print '  mean:', data.mean(axis=0)
print '  standard deviation:', data.std(axis=0)
print

print '4. Statistics for each day (over all cities)'
print '  min:', data.min(axis=1)
print '  max:', data.max(axis=1)
print '  mean:', data.mean(axis=1)
print '  standard deviation:', data.std(axis=1)
print

print '5. Index of city with maximum wind speed for each day'
print '  daily max location:', data.argmax(axis=1)
print
  
daily_max = data.max(axis=1)
max_row = daily_max.argmax()

print '6. Day of maximum reading'
print '  Year:', int(wind_data[max_row,0])
print '  Month:', int(wind_data[max_row,1])
print '  Day:', int(wind_data[max_row,2])
print

january_indices = wind_data[:,1] == 1
january_data = data[january_indices]

print '7. Statistics for January'
print '  mean:', january_data.mean(axis=0)
print 

# Bonus

# compute the month number for each day in the dataset
months = (wind_data[:,0]-61)*12 + wind_data[:,1] - 1

# get set of unique months
month_values = set(months)

# initialize an array to hold the result
monthly_means = zeros(len(month_values))

for month in month_values:
    # find the rows that correspond to the current month
    day_mask = (months == month)
    
    # extract the data for the current month using fancy indexing
    month_data = data[day_mask]
    
    # find the mean
    monthly_means[month] = month_data.mean()
    
    # Note: experts might do this all-in one
    # monthly_means[month] = data[months==month].mean()

# In fact the whole for loop could reduce to the following one-liner
# monthly_means = array([data[months==month].mean() for month in month_values])
 

print "Bonus 1."
print "  mean:", monthly_means
print

