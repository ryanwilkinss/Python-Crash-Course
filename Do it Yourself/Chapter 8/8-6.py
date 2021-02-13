# Write a function called city_country() that takes in the name of a city and 
# its country. The function should return a string formatted like this:
# “Santiago, Chile”
# Call your function with at least three city-country pairs, and print the 
# value that’s returned.
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)
