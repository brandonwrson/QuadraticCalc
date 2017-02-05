import math

def factoring():
    a = float(input("Insert value of a:"))
    b = float(input("Insert value of b:"))
    c = float(input("Insert value of c:"))
    
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        print ("This equation has no real solutions")
        

    else:
        solution = (-1 * b + math.sqrt(discriminant))/(2 * a)
        solution2 = ( -1 * b - math.sqrt(discriminant))/(2 * a)

        print ("x = %d, %f" % (solution, solution2))
       

        if math.sqrt(discriminant).is_integer() == True :
            factor = solution * -1
            factor2 = solution2 * -1

            if factor.is_integer() == False:
                h = ((factor).as_integer_ratio())
                
                y1,y2 = h

                speech1 = ("(%d x, + %f)" % (y2, y1))
                print (str(speech1))

            else:
                print ("(x + %d)" % (factor))
            if factor2.is_integer() == False:
                g = ((factor2).as_integer_ratio())                
                x1,x2 = g

                speech2 = ("(%d x, + %f)" % (x2, x1))
                print (str(speech2))
                

            else:
                print ("(x + %f)" % (factor2))
                
        
            


        else:
            print("Irrational Factors")
        
         
    
    playAgain = input("Do you want to try again? (Press any key)")



playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    factoring()
    




