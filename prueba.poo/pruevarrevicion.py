class RECTANGULO:
    def __init__(self,ancho,longitud) :
        self.ancho=ancho
        self.longitud=longitud

    def calculo(self):
        perimetro = 2 * self.ancho + 2*self.longitud
        return perimetro
    
    def calculo2 (self):
        area = self.ancho * self.longitud
        return area
rect = RECTANGULO(40, 10)

perimetro_result = rect.calculo()
area_result = rect.calculo2()

print("El perímetro del rectángulo es:",perimetro_result )

print("El área del rectángulo es:", area_result)

