import convert

c = 10.0
f = convert.celsius_to_fahrenheit(c)
print(f'{c: .2f} C = {f: .2f} F')

meters = 2.5
miles = convert.meters_per_second_to_miles_per_hour(meters)
print(f'{meters: .2f} meters = {miles: .2f} miles/hr')

miles = 5.5
meters = convert.miles_per_hour_to_meters_per_second(miles)
print(f'{miles: .2f} miles = {meters: .2f} m/s')
