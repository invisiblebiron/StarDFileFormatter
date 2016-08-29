'''
Created on 2016/08/26

@author: Brian
'''
import re

if __name__ == '__main__':
    pass

#Value regex
valueTagCheck = re.compile('(<Value>)(.*)(</Value>)')
keyTagCheck = re.compile('(<Key>)(.*)(</Key>)')

valueExample = '''<Key>Fried Egg</Key>
                  <Value>-5 1/10 10/194/default</Value>
               '''

moValue = valueTagCheck.search(valueExample)
moKey = keyTagCheck.search(valueExample)

print(moValue.group(2))
print(moKey.group(2))
print('\n')

newValue = moValue.group(1) + moValue.group(2) + '/' + moKey.group(2) + moValue.group(3)

print(newValue)
