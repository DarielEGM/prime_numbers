#Function that returns prime numbers
#between 0 and the number declared

#Function that checks if a number is prime
def is_prime(num):
    #We verify that the passed number cannot be divided
    #for any number between 2 and that same number -1
    for i in range(2,num-1):
        #If it is divisible by any, we return false and the loop ends 
        if num%i==0: return False
    #If the loop ends, it means that it was not divisible so it is prime
    return True

#Function that returns a list with all prime numbers
def prime_numbers(num):
    #We create the list
    primes = []
    for i in range(3,num+1):
        #Verificamos si el valos es primo
        result = is_prime(i)
        #In case it is, we add it to the list
        if result ==True: primes.append(i)
        
    #Return the list
    return primes

#We create the result by calling the function and it is displayed
result = prime_numbers(13)
print(result)