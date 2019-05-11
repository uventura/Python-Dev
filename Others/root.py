'''
##############################################
###| ROOT APPROXIMATION WITH HERON THEOREM|###
##############################################
'''

print('|===| Root Approximation |===|\n')

answer = False

while(1):
 if answer == False:
  value = float(input('The value: '))
  a = value/2
  result = 0
 
  for i in range(100):
   result = (a + (value/a))/2
   a = result

  print('\n[ The result is {:.2f} ]\n'.format(result))

  answer = True

 else:
   print('-'*25)
   answer = input('New root?[y/n] ')
   if answer.lower() == 'y':
    print('-'*25)
    answer = False
   elif answer.lower() == 'n':
    print('-'*25+'\n Bye... ')
    break
