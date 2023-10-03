def test(num):
    i=1
    while (i!=0.03*num+1 and i<0.03*num+1):
        print(i)
        i+=1

num=int(input("How many times? "))
test(num)