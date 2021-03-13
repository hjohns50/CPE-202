
#list -> int
#returns the max of a list
def max_list_iter(int_list): #must use iteration not recursion
   '''Finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError'''
   if (int_list == None):
        raise ValueError('empty list')
   if len(int_list) == 0:
      return None
   #max is a int used to store the highest number in the int list
   max = int_list[0]
   for val in int_list:
      if val > max:
         max = val
   return max

   #list -> list
   #reverse a list using recursion
def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if (int_list is None):
      raise ValueError
   if (len(int_list) == 0):
      return []
   return reverse_rec(int_list[1:]) + int_list[:1]

#int int int list -> int
#finds a item in a list that matches 
def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   #raises value error
   if (int_list is None):
      raise ValueError
   #raises index error 
   if (low < 0 or high >= len(int_list)):
      raise IndexError
   #if low and high pass each other that means that the target is not in the list
   if (low > high):
      return None
   #checks if low is target's index
   if (int_list[low] == target):
      return low
   #checks if high is target's index
   elif (int_list[high] == target):
      return high
   #adds one to low and subtracts one from high
   else:
      low += 1
      high -= 1
      return bin_search(target, low, high, int_list)