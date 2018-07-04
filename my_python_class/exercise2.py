#!/usr/bin/env python
user = { 'admin': True, 'active': False, 'name': 'Kevin' }
if user['admin']: 
  print ("Name is %s and he is an admin." %(user['name']))
else:
  print ("Name is %s and he is not an admin." %(user['name']))
if user['active']: 
  print ("Name is %s and he is active." %(user['name']))
else:
  print ("Name is %s and he is not active." %(user['name']))
if user['admin'] and user['active']: 
  print ("Name is %s and he is an admin and active." %(user['name']))
elif not user['admin'] and user['active']:
  print ("Name is %s and he is not admin but is active." %(user['name']))
elif not user['active'] and user['admin']:
  print ("Name is %s and he is not active but is an admin." %(user['name']))
