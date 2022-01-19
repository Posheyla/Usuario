from Usuario import Usuario

guido = Usuario("Guido", "guido@gmai.com")
nibles = Usuario("Nibles", "nibles@gmai.com")
benny = Usuario("Benny","benny@gmail.com")

guido.hacer_depósito(100)
guido.hacer_depósito(100)
guido.hacer_depósito(100)

guido.mostrar_balance_usuario()

guido.hacer_retiro(100)

guido.mostrar_balance_usuario()

nibles.hacer_depósito(100)
nibles.hacer_depósito(50)

nibles.mostrar_balance_usuario()

nibles.hacer_retiro(50)
nibles.hacer_retiro(50)

nibles.mostrar_balance_usuario()

benny.hacer_depósito(1000)

benny.mostrar_balance_usuario()

benny.hacer_retiro(30)
benny.hacer_retiro(200)
benny.hacer_retiro(40)

benny.mostrar_balance_usuario()

benny.transferir_dinero(nibles,500)

benny.mostrar_balance_usuario()
nibles.mostrar_balance_usuario()

