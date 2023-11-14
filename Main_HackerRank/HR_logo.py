thickness = 5 #This must be an odd number
c = 'H'

# BUSCAR LA DOCUMENTACION DE LOS METODOS


#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print(" "+(c*thickness).ljust(thickness*2)+(c*thickness).rjust(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6)) 