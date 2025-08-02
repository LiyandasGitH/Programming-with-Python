
'''
def main():
 #   latitude = 42.376
 #   longitude = -71.115
    coordinates = (42.376, -71.115)
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

#tuples: cannot be changed or editted!!!
main()
'''

import sys
def main():
 #   latitude = 42.376
 #   longitude = -71.115
    coordinates_tuple = (42.376, -71.115)
    coordinates_list = [42,376, -72,115]
    print(f"{sys.getsizeof(coordinates_tuple)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")

main()

# tuples take up less space ...
