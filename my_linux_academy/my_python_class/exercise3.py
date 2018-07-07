#!/usr/bin/env python
user = [ { 'admin': True, 'active': True , 'name': 'Kevin' }, { 'admin': True, 'active': False, 'name': 'Jane' }, { 'admin': False, 'active': False, 'name': 'Mike' } ]
for mymember in user:
 if mymember['admin']: 
  print ("Admin: %s " %(mymember['name']))
 else:
  print ("Not Admin: %s ." %(mymember['name']))
 if mymember['active']: 
  print ("Active: %s " %(mymember['name']))
 else:
  print ("Not active: %s " %(mymember['name']))
 if mymember['admin'] and mymember['active']: 
  print ("Active  Admin : %s " %(mymember['name']))
 elif not mymember['admin'] and mymember['active']:
  print ("Active, not admin" %s  %(mymember['name']))
# elif not mymember['active'] and mymember['admin']:
#  print ("not Active but is an admin." %s %(mymember['name']))
