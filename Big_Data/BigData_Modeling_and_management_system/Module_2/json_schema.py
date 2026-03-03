import sys
import json

filename = sys.argv[1]
lines = []


#Read the JSON file
try:
    with open(filename) as json_file:
        for line in json_file:
            if len(line) > 1: lines.append(json.loads(line))
except:
    print('Unable to read the file')
    print(filename)


# Create a funtion that iterates over the dictionary
def inner_levels(values, indent):
    ''' 
    This funtion is supposed to iterate over the dictiorary
    going down into levels is the values stored in a key is a dictionary
    '''
    try: 
        for key,value in values.items():
            print(indent,key)
            try: 
                inner_levels(value, indent + '....') # recall the same function to check if the value is a dict
            except:
                pass
    except:
        pass

for key,value in lines[0].items():
    print(key)
    inner_levels(value,'....')
        



