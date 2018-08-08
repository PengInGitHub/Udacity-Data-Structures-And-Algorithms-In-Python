"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Africa'] = {'Egypt': ['Cairo']}
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = (['Shanghai'])

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order."""
sortedAmericanCities = sorted(locations['North America']['USA'])
print 1
for city in sortedAmericanCities:
    print city
            
"""2. All cities in Asia, in alphabetic
order, next to the name of the country.
"""

cityCountryPairs = []
for countries, cities in locations['Asia'].iteritems():
    cityCountryPair = cities[0] + ' - ' + countries
    cityCountryPairs.append(cityCountryPair)
cityCountryPairs = sorted(cityCountryPairs)
print 2
for cityCountryPair in cityCountryPairs:
    print cityCountryPair
            
"""In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
