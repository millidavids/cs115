# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# Sept. 29, 2012
# Programming Assignment 1
#
# ______________________________________________________________________________
#
# Purpose: The purpose of this assignment is to take an input from the user of
#          altitude of a satellite and compute the velocity, acceleration and
#          time of orbit completion. The output format was predetermined by
#          a standard provided in the assignment.
#
# Preconditions: The only input from the user is the altitude of the satellite.
#
# Post-conditions: The outputs of the program are the velocity, acceleration, and
#                 time of orbit completion. The outputs are formatting befitting
#                 the standard provided in the assignment.
#_______________________________________________________________________________

# Imports the math library.
import math

# Defines main.
def main():

    # Displays the introductory message.
    print('                 Satellite Orbital Calculations')
    print('                        by David Yurek')
    print(' ')

    # Prompts user for satellite altitude.
    sat_altitude_km = float(input("Please enter the altitude of the satellite "
                                  "in kilometers from the Earth's surface "))

    # Defines constant variables.
    earth_radius_km = 6378.1370                                                       # Earth radius in kilometers.
    earth_GM = float(3.986005 * (10 ** 14))                                           # Earth GM in m^3/s^2.
    orbit_radius_km = (sat_altitude_km + earth_radius_km)                             # Orbit radius in kilometers.
    orbit_radius_meters = orbit_radius_km * 1000                                      # Reassigns orbit radius > meters.

    # Calculations from provided equations.
    sat_velocity = math.sqrt(earth_GM / orbit_radius_meters)                          # Velocity calculated in m/s.
    acceleration = earth_GM / (orbit_radius_meters ** 2)                              # Acceleration calculated > m/s^2.
    orbit_time_seconds = math.sqrt(((4 * math.pi ** 2)                                # Orbit time in seconds.
                                    * orbit_radius_meters ** 3) / earth_GM)
    orbit_time_minutes = orbit_time_seconds / 60                                      # Orbit time converted to minutes.
    orbit_time_minutes = round(orbit_time_minutes, 2)                                 # Orbit time in minutes rounded.

    # Prints output in assigned format.
    print(' ')
    print('The satellite is travelling at', sat_velocity, 'meters / second.')
    print('The satellite is accelerating at', acceleration,
          'meters / second squared.')
    print('The satellite takes', orbit_time_seconds,
          'seconds for one orbit or', orbit_time_minutes, 'minutes.')

# Calls main.
main()