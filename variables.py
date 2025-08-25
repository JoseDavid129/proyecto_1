jugador = input ( "Dame tu nombre: ")
juego = input ( "Dime el juego que quieres: ")
ciudad = input ("De que ciudad te conectas?: ") 
edad = int(input ('Dame tu edad: '))

print ('Hola', jugador, 'Bienvenido') 
print ('Tu juego', juego, 'ya esta listo')
print (jugador, 'Te conectas desde', ciudad)
print (jugador, 'tu edad es', edad, 'años' )

if edad >= 18:
    print("Puedes Jugar")
else: 
    print('No puedes jugar, pidele permiso a tus papis')

if ciudad.upper() == 'BOGOTA':
    print('Vives en la mejor ciudad del mundo')
else: 
    print('No vives en la mejor ciudad del mundo')
