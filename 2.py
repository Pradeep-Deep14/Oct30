print(min(max(False,-30,-4),12,7))

# False
#Because: the max method runs first,
#and it returns False (False is 0 and 0 is > -30 and -4). 
#The min function returns False as well (False is 0 and 0 is < 12 and 7)