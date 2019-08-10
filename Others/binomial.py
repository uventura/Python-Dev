def factorial(n):
 if n == 0:
  return 1
 return n*factorial(n-1)

def combination(n,p):
 if n<p:
  return 0
 return (factorial(n)/(factorial(p)*factorial(n-p)))
    
def binomial(elements, combinations, result, basicList=[]):
 #In a binomial (n  p), elements is n and combinations is p.
    
 i = 0
 while i<len(elements):
  if len(basicList) == combinations-1:
    result.append(basicList+[elements[i]])
  else:
    binomial(elements[(i+1):], combinations, result, basicList+[elements[i]])
  i+=1

#Example
result = []

binomial(['a','b','c'], 2, result)
print("\nThe Result is {} combinations".format(int(combination(3,2))))
print('\n'+str(result))
