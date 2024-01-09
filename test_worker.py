from worker_2_db import *

print("Asteroid worker test")
print("----------")
print("Testing function: \"sort_ast_by_pass_dist\"")
# Testing passing empty asteroids list
print("Empty asteroids list [] -->")
assert sort_ast_by_pass_dist([]) == []
print("OK")
print("----------")

# Testing if the sorting by distance of the list is done properly
print("Actual list good data, checking if sorting is correct -->")
list_unsorted = [['(2001 UP)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3092390', 0.019, 0.043, 1634131860, '2021-10-13 13:31:00', '2021-10-13 16:31:00', 64502, 48658232.921, '3092390'], ['(2008 SY150)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3428531', 0.031, 0.068, 1634091000, '2021-10-13 02:10:00', '2021-10-13 05:10:00', 56440, 38212310.608, '3428531'], ['(2014 KA91)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3673167', 0.021, 0.047, 1634090220, '2021-10-13 01:57:00', '2021-10-13 04:57:00', 20714, 24287902.734, '3673167'], ['(2018 VF4)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3836100', 0.023, 0.052, 1634124480, '2021-10-13 11:28:00', '2021-10-13 14:28:00', 40740, 31043596.356, '3836100'], ['(2019 SW8)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3873141', 0.019, 0.043, 1634141940, '2021-10-13 16:19:00', '2021-10-13 19:19:00', 58537, 53322355.414, '3873141'], ['(2019 UN3)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3879314', 0.038, 0.086, 1634134440, '2021-10-13 14:14:00', '2021-10-13 17:14:00', 75414, 41458428.073, '3879314'], ['(2020 UC4)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54076013', 0.016, 0.036, 1634137920, '2021-10-13 15:12:00', '2021-10-13 18:12:00', 72466, 57148313.415, '54076013'], ['(2021 CT1)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54110078', 0.023, 0.052, 1634111400, '2021-10-13 07:50:00', '2021-10-13 10:50:00', 20075, 30951757.236, '54110078'], ['(2021 SF2)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54200444', 0.036, 0.081, 1634095860, '2021-10-13 03:31:00', '2021-10-13 06:31:00', 11236, 31510633.785, '54200444'], ['(2021 TO)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54201815', 0.038, 0.086, 1634147220, '2021-10-13 17:47:00', '2021-10-13 20:47:00', 25391, 11816672.875, '54201815'], ['(2021 TG3)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54203028', 0.038, 0.084, 1634095140, '2021-10-13 03:19:00', '2021-10-13 06:19:00', 20902, 31189940.442, '54203028'], ['(2021 TX10)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54208049', 0.007, 0.017, 1634126280, '2021-10-13 11:58:00', '2021-10-13 14:58:00', 31032, 942082.384, '54208049']]
list_sorted_by_dist = [['(2021 TX10)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54208049', 0.007, 0.017, 1634126280, '2021-10-13 11:58:00', '2021-10-13 14:58:00', 31032, 942082.384, '54208049'], ['(2021 TO)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54201815', 0.038, 0.086, 1634147220, '2021-10-13 17:47:00', '2021-10-13 20:47:00', 25391, 11816672.875, '54201815'], ['(2014 KA91)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3673167', 0.021, 0.047, 1634090220, '2021-10-13 01:57:00', '2021-10-13 04:57:00', 20714, 24287902.734, '3673167'], ['(2021 CT1)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54110078', 0.023, 0.052, 1634111400, '2021-10-13 07:50:00', '2021-10-13 10:50:00', 20075, 30951757.236, '54110078'], ['(2018 VF4)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3836100', 0.023, 0.052, 1634124480, '2021-10-13 11:28:00', '2021-10-13 14:28:00', 40740, 31043596.356, '3836100'], ['(2021 TG3)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54203028', 0.038, 0.084, 1634095140, '2021-10-13 03:19:00', '2021-10-13 06:19:00', 20902, 31189940.442, '54203028'], ['(2021 SF2)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54200444', 0.036, 0.081, 1634095860, '2021-10-13 03:31:00', '2021-10-13 06:31:00', 11236, 31510633.785, '54200444'], ['(2008 SY150)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3428531', 0.031, 0.068, 1634091000, '2021-10-13 02:10:00', '2021-10-13 05:10:00', 56440, 38212310.608, '3428531'], ['(2019 UN3)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3879314', 0.038, 0.086, 1634134440, '2021-10-13 14:14:00', '2021-10-13 17:14:00', 75414, 41458428.073, '3879314'], ['(2001 UP)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3092390', 0.019, 0.043, 1634131860, '2021-10-13 13:31:00', '2021-10-13 16:31:00', 64502, 48658232.921, '3092390'], ['(2019 SW8)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3873141', 0.019, 0.043, 1634141940, '2021-10-13 16:19:00', '2021-10-13 19:19:00', 58537, 53322355.414, '3873141'], ['(2020 UC4)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54076013', 0.016, 0.036, 1634137920, '2021-10-13 15:12:00', '2021-10-13 18:12:00', 72466, 57148313.415, '54076013']]
assert sort_ast_by_pass_dist(list_unsorted) == list_sorted_by_dist
print("OK")
print("----------")

# Testing when providing list with elements of various index length
print("Data with various index length -->")
list_unsorted_various_index = [['(2001 UP)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3092390', 0.019, 0.043, 1634131860, '2021-10-13 13:31:00', '2021-10-13 16:31:00', 64502, 48658232.921], ['(2008 SY150)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3428531', 0.031, 0.068, 1634091000, '2021-10-13 02:10:00', '2021-10-13 05:10:00', 56440, 38212310.608, '3428531'], ['(2014 KA91)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3673167', 0.021, 0.047, 1634090220, '2021-10-13 01:57:00', '2021-10-13 04:57:00', 20714, 24287902.734, '3673167'], ['(2018 VF4)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3836100', 0.023, 0.052, 1634124480, '2021-10-13 11:28:00', '2021-10-13 14:28:00', 40740, 31043596.356, '3836100'], ['(2019 SW8)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3873141', 0.019, 0.043, 1634141940, '2021-10-13 16:19:00', '2021-10-13 19:19:00', 58537, 53322355.414, '3873141'], ['(2019 UN3)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3879314', 0.038, 0.086, 1634134440, '2021-10-13 14:14:00', '2021-10-13 17:14:00', 75414, 41458428.073, '3879314'], ['(2020 UC4)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54076013', 0.016, 0.036, 1634137920, '2021-10-13 15:12:00', '2021-10-13 18:12:00', 72466, 57148313.415, '54076013'], ['(2021 CT1)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54110078', 0.023, 0.052, 1634111400, '2021-10-13 07:50:00', '2021-10-13 10:50:00', 20075, 30951757.236, '54110078'], ['(2021 SF2)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54200444', 0.036, 0.081, 1634095860, '2021-10-13 03:31:00', '2021-10-13 06:31:00', 11236, 31510633.785, '54200444'], ['(2021 TO)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54201815', 0.038, 0.086, 1634147220, '2021-10-13 17:47:00', '2021-10-13 20:47:00', 25391, 11816672.875, '54201815'], ['(2021 TG3)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54203028', 0.038, 0.084, 1634095140, '2021-10-13 03:19:00', '2021-10-13 06:19:00', 20902, 31189940.442, '54203028'], ['(2021 TX10)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54208049', 0.007, 0.017, 1634126280, '2021-10-13 11:58:00', '2021-10-13 14:58:00', 31032, 942082.384, '54208049']]
assert sort_ast_by_pass_dist(list_unsorted_various_index) == []
print("OK")
print("----------")

# Testing when providing list with a shorter index length then expected
print("Data with short index length -->")
list_unsorted_index_short = [['(2001 UP)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3092390', 0.043, 1634131860, '2021-10-13 13:31:00', '2021-10-13 16:31:00', 64502, 48658232.921, '3092390'], ['(2008 SY150)', 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3428531', 0.031, 0.068, 1634091000, '2021-10-13 02:10:00', '2021-10-13 05:10:00', 56440, 38212310.608]]
assert sort_ast_by_pass_dist(list_unsorted_index_short) == []
print("OK")
print("----------")

# Mans Tests:
# Mana testa beigas

print("Asteroid worker test -> ALL OK")
print("----------------------------------------")