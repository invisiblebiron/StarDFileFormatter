'''
Created on 2016/08/26

@author: Brian
'''
targetFile = open('C:\\Users\\Brian\\Desktop\\animationDescriptions.de-DE.xml')

content = targetFile.readlines()

for line in content:
    print(line)
    
    
targetFile.close()