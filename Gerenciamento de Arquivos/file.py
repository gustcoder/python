import os


BASE_PATH = os.path.abspath(__file__)

dir = os.path.dirname(BASE_PATH)

file = open(dir + '/_file_test.dat', 'w')

file.write('##########################\n')
file.write('School of Net\n')
file.write('##########################\n')

file.close