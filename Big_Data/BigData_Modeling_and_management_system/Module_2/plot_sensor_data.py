import sys
import re
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd
import seaborn as sns
''' 
************************************
************************************
The regular expresion module stands that: 
\d => Matches any Unicode decimal digit (that is, any character in Unicode character category [Nd]). 
        This includes [0-9], and also many other digit characters.
        Matches [0-9] if the ASCII flag is used.
====================================
\s => For Unicode (str) patterns:
        Matches Unicode whitespace characters (as defined by str.isspace()). 
        This includes [ \t\n\r\f\v], and also many other characters, 
            for example the non-breaking spaces mandated by typography rules in many languages.
        Matches [ \t\n\r\f\v] if the ASCII flag is used.
====================================
'.' => Dot In the default mode, this matches any character except a newline. 
'*' => Asterisk - Causes the resulting RE to match 0 or more repetitions of the preceding RE
'+' => Plus Causes the resulting RE to match 1 or more repetitions of the preceding RE

Regular expressions use the backslash character ('\') 
to indicate special forms or to allow special characters to be used without invoking their special meaning.
If I use the '\.' will be to find a dot in the pattern instead of matching any character.
************************************
************************************
The Matplotlib Library has it's own model dates, and to transform string to dates
It uses the functions epoch and num2date
====================================
dates.get_epoch()
Get the epoch used by dates.
Returns:
    epoch : str => String for the epoch (parsable by numpy.datetime64).
====================================
dates.num2date(x, tz=None)
Convert Matplotlib dates to datetime objects.
Returns:
    datetime or sequence of datetime
        Dates are returned in timezone tz.
        If x is a sequence, a sequence of datetime objects will be returned
************************************
************************************
References
https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch
https://docs.python.org/3/library/re.html#search-vs-match
'''

''' 
Understanding Epoch and it's transformartion 

What is Epoch?
In Python (and most systems), epoch time means:
The number of seconds that have passed since
January 1, 1970 at 00:00:00 UTC
This moment is called Unix Epoch.


epoch_str = 1419408016
epoch_to_date = datetime.fromtimestamp(epoch_str)
print(epoch_str,'transformed to epoch',epoch_to_date)


today = datetime.today()
today_in_epoch = today.timestamp()
print(today,'date transformed to epoch', today_in_epoch)
'''

#Start getting file name
try:
    file_name = sys.argv[1]
    lookup_measure = sys.argv[2]
except:
    file_name = 'Module_1_Introduction/coursera-hands-on-updates-2024/coursera-hands-on-updates-2024/big-data-2/sensor/wx-data.txt'
    lookup_measure = 'Ta'

time = []
time_h = []
meas = []
pattern = lookup_measure + "=(\d+\.\d+).*"

# Open and handle file txt
try:
    with open(file_name) as sensor_raw:
        for line in sensor_raw:
            sensor_line = re.split('\s+',line)
            sensor_measures = sensor_line[1].split(',')
            
            for measure in sensor_measures:
                
                measure_match = re.match(pattern,measure)
                if measure_match:
                    t = datetime.fromtimestamp(int(sensor_line[0]))
                    t_by_hour = t.strftime('%H')
                    t =  t.strftime('%H:%M:%S')
                    time_h.append(t_by_hour)
                    time.append(t)
                    meas.append(float(measure_match.group(1)))
except:
    print('unable to open file: ',file_name)

measures = pd.DataFrame({'Hour':time_h,'Time':time,'Measure':meas})
Hourly_mean = measures.groupby(['Hour']).agg({'Measure':'mean'}).reset_index()
print(measures.head(20))
print('=='*20)
print(Hourly_mean.head(20))

fig,ax =plt.subplots(1,2,figsize=(15,10))

ax[1].plot_date(
    data=Hourly_mean,
    x = 'Hour',
    y = 'Measure'
)

ax[0].plot_date(
    data=measures,
    x = 'Time',
    y = 'Measure'
)
plt.xlabel('Hours')
plt.xlabel('Time')
plt.ylabel(lookup_measure)
plt.xticks(rotation=45)
plt.show()
