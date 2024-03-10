import math #Библиотека math для работы с sqrt
print("x^2+6x+9=0") #Пишем нужное уравнение и вводим коэффиценты
a = 1.0
b = 6.0
c = 9.0
Discriminant = b ** 2 - 4 * a * c 
print("Дискриминант D=", Discriminant)
#Условия D<0 нет решения, D==0 один корень x, D>0 два корня x1, x2
if Discriminant < 0: 
    print("Нет действительных корней")
elif Discriminant == 0:
    x = (-b) / (2*a)
    print("Уравнение имеет один корень:", x)
else:
    x1 = ((-b + math.sqrt(Discriminant)) / (2 * a))
    x2 = ((-b - math.sqrt(Discriminant)) / (2 * a))
    print ('Уравнение имеет два корня:')
    print ('x1 =', x1)
    print ('x2 =', x2)

      
