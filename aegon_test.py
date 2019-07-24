
for i in range(101):
    if i%3 == 0 and i%5 == 0 :
        result  = "FIZZ BUZZ"
    elif i%3 == 0:
        result = "FIZZ"
    elif i%5 == 0:
        result = "BUZZ"
    else:
        result =str(i)
    print("{} : {}".format(str(i), result))
