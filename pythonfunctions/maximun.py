#Find the set of numbers that are greater than the treshhold "a"
maximum=[20,60,70,90,500,700,800,99]     
def findmax(a):
      for item in maximum:
        if item > a:
            print(item)
        else:
            continue   
    
print(findmax(330))

