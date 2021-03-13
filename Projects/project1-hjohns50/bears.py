# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    #n is an int
    #basecase
    if n == 42:
        return True
    #when n becomes less that 42 that trial is over
    elif n < 42:
        return False
    #tests n trying to have n equal to 42
    else:
        ones = n%10
        tens = (n%100)//10
        two = n/2
        three = n-((n%10)*((n%100)//10))
        five = n - 42
            
        #trys to operate on n 
        if n % 2 == 0 and bears(two):
            return True
        if ones != 0 and tens != 0:
            if n % 3 == 0 and bears(three):
                return True
        if ones != 0 and tens != 0:
            if n % 4 == 0 and bears(three):
                return True
        if n % 5 == 0 and bears(five):
             return True
    #if operations doesn't work then returns false
    return False