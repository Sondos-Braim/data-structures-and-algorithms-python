import re
def find_word(string):
  x = re.sub("," , "", string)
  output=[]
  arr=x.split(' ')
  for i in arr:
    i=i.lower()
    if i in output:
      return i
    else:
      output.append(i)
