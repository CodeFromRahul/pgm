x = [0,1,2,3,4]
y = [0.1,0.3,0.2,0.3,0.1]
expected   =0
variance = 0
l = 0
total=0

for i in range(len(x)):
  s= x[i] * y[i]
  l= x[i]*x[i]*y[i]
  total = total + l
  expected = expected + s
variance = total - expected* expected
print ("expected value is",expected)
print( " variance is",variance)