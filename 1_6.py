age={'Anna':41, 'Pavel':45, 'Dmitry':49, 'Helen':45}
print(age)
print(age['Dmitry'])
print(age.get('Lidia'))
age.update({'Maria':12, 'Kate':7})
print(age)
a=age.pop('Maria')
print(age)
set_={1, 'Anna', 'Pavel', 2 ,'Anna', 2 , True}
print(set_)
set_.update({'Tom', 7})
set_.remove('Pavel')
print(set_)

