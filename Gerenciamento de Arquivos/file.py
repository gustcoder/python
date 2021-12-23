import os


BASE_PATH = os.path.abspath(__file__)

dir = os.path.dirname(BASE_PATH)

# file = open(dir + '/_file_test.dat', 'w')

# file.write('##########################\n')
# file.write('School of Net\n')
# file.write('##########################\n')

# file.close

file = open(dir + '/_file_test.dat', 'a')

file.write('##########################\n')
file.write('School of Net\n')
file.write('##########################\n')

file.writelines(['PFA\n', 'RabbitMQ\n', 'Docker\n'])

file.close