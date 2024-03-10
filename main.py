nric = input('Enter an NRIC number: ')
nric = nric.strip().upper()

first_digit = ["T","G","F","S"]
table_1 = [2,7,6,5,4,3,2]
SandT_table = ['J','Z','I','H','G','F','E','D','C','B','A']
FandG_table = ['X','W','U','T','R','Q','P','N','M','L','K']

def validation(nric):
  if nric[0] in first_digit and len(nric) == 9 and nric[1:8].isdigit() == True and nric[-1].isalpha() == True:
    return True
  else:
    return False
    
def check_digit(nric):
  total_num = 0
  for i in range(7):
    num = int(nric[i+1]) * table_1[i]
    total_num += num
  if nric[0] in first_digit[:2]:
    total_num += 4
  remainder = total_num % 11
  if nric[0] in ['S','T']:
    if nric[-1] == SandT_table[remainder]:
      return True
    else:
      return False
  else:
    if nric[-1] == FandG_table[remainder]:
      return True
    else:
      return False
      
if validation(nric) == True:
  if check_digit(nric) == True:
    print('NRIC is valid.')
  else:
    print('NRIC is invalid.')
else:
  print('NRIC is invalid.')