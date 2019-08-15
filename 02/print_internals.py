# print is nothing but the below two lines
import sys
sys.stdout.write('Hello\n')

# print prints to stdout which is terminal by default 
# redefine stdout to be file

sys.stdout = open('data.dat','a')
print ('Hello\n')

# redirection a better way
textfile = open('text.dat', 'a')
print >> textfile,'Hello'
