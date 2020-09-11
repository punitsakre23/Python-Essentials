# Answer 1.

listy = [1,5,6,4,1,2,3,5]
sub_list = [1,1,5]

#    print("Original List :" + str(listy))
#   print("Original sub_list : " + str(sub_list))

flag = 0
# if(all(x in listy for x in sub_list)):
#     flag = 1

if (set(sub_list).issubset(set(listy))):
    flag = 1

if (flag):
    print("It's a Match")
else:
    print("It's Gone")

# Answer 2.


def checkPrimeNumbers(num):
    # for num in range(2,2500):
        count = 0
        for i in range(2,num):
            if num%i == 0:
                count = 1
        if (count == 0):
            # print(num, "Prime no.")
            return True
        else:
            return False

lst = list(range(1,2500))
isPrime = filter(checkPrimeNumbers, lst)
print("prime numbers between 1 - 2500:", list(isPrime))

# Answer 3)

def getCapitalize(*arg):
    for word in arg:
        string = word.split(" ")
        capitalized_list = [capital.capitalize() for capital in string]
        words = (" ").join(capitalized_list)
        print(words)

getCapitalize("hey this is sai","I am in mumbai","teaching is my passion")