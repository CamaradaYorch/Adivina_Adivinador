#------------------------------------------------------------------

# Autor: [Jorge Mera]
# Fecha: [15/07/2023]
# Descripción: [Juego de adivinanzas para adivinar un color oculto]
# Versión: [1.2]

#------------------------------------------------------------------

import random
import time

# ▼ Define la longitud de la barra de animación
barra = 30
# ▼ Define los elementos de la animación de la barra
elementos = ['-', '\\', '|', '/']

# ▼ Animación de la barra al inicio del juego
for i in range(barra):
    frame = i % len(elementos)
    print(f'\r[{elementos[frame]}{"=" * i}{" " * (barra - i)}]', end='')
    time.sleep(0.1)

#------------------------------------------------------------------

class adivina_adivinador_v12:
    # ▼ Lista de colores disponibles
    def __init__(self, nombre):
        self.nombre = nombre
        self.colores = ["rojo", "azul", "verde", "amarillo", "naranja",
                        "rosa", "violeta", "negro", "blanco", "gris", "ocre", "sepia",
                        "cafe", "miel", "siena", "carmesi", "oro", "cian", "esmeralda",
                        "acua", "turquesa", "celeste", "morado", "plata"]
        self.color_oculto = random.choice(self.colores)
        # ► Color oculto seleccionado aleatoriamente
        self.intentos_restantes = 9
        # ► Intentos restantes del jugador
        self.letras_adivinadas = []
        # ► Lista de letras adivinadas por el jugado

#------------------------------------------------------------------

    # ▼ Verifica si la letra ingresada es válida (minúscula y no un número)
    def adivinar_letra(self, letra):
        if not letra.islower() or letra.isdigit():
            print("\n❗ Te dije que solo debes ingresar letras en minúscula ❗ ( ⇀‸↼‶ )\n ")  # noqa: E501
            return

#------------------------------------------------------------------

        # ▼ Verifica si la letra ya ha sido adivinada previament
        if letra in self.letras_adivinadas:
            print("\n🤦 Ya has usado esa letra ( ಠ _ ಠ )")
            return

#------------------------------------------------------------------

        # ▼ Agrega la letra a las letras adivinadas y verifica si es correcta
        self.letras_adivinadas.append(letra)
        if letra in self.color_oculto:
            print("\n✅ ¡Adivinaste la letra! <( ^ _ ^ )>")
        else:
            self.intentos_restantes -= 1
            print("\n❌ ¡Letra incorrecta! Te quedan ► {} ◄ intentos. (ㆆ_ㆆ)".format(self.intentos_restantes))  # noqa: E501

#------------------------------------------------------------------

    def adivinar_palabra(self, palabra):
        # ▼ Verifica si la palabra ingresada coincide con el color oculto
        if palabra == self.color_oculto:
            print("😃 ⭐⭐⭐ ¡Felicidades, {}! Adivinaste el color. (ﾉ☉ヮ⚆)ﾉ ⌒*:･ﾟ⭐⭐⭐".format(self.nombre))  # noqa: E501)
            mensaje = '''
▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦
      _____.___.               __      __.__                  
      \__  |   | ____  __ __  /  \    /  \__| ____            
       /   |   |/  _ \|  |  \ \   \/\/   /  |/    \           
       \____   (  <_> )  |  /  \        /|  |   |  \          
       / ______|\____/|____/    \__/\  / |__|___|  /          
       \/                            \/          \/           
                                                         
        _________    _____   ____     _______  __ ___________ 
       / ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \\
      / /_/  > __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/
      \___  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   
    /_____/     \/      \/     \/                   \/
 
▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦]
                Desarrollado por    
         🇯  🇴  🇷  🇬  🇪    🇲  🇪  🇷  🇦 \n'''

            print(mensaje)
            return True
            

        else:
            self.intentos_restantes -= 1
            print("🤪 ❌Palabra incorrecta.❌ Te quedan ► {} ◄  intentos.".format(self.intentos_restantes))  # noqa: E501)
            return False

#------------------------------------------------------------------

    def jugar(self):
        print("\n¡Hola, ► {} ◄ Juguemos".format(self.nombre))
        print(("\n\n   ██  Adivina Adivinador ██ "))
        print(("   ██    Debes adivinar   ██ \n"))
        print("  ► En qué color pienso hoy ◄  \n")

        print("  █▓▒▒▒▒▒▒▒▐███████▌▒▒▒▒▒▒▒▓█")
        print("  █▓▒▒▒▒▒▒▒▐░▀░▀░▀░▌▒▒▒▒▒▒▒▓█")
        print("  █▓▒▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌▒▒▒▒▒▒▒▓█")
        print("  █▓▒▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄▒▓█")
        print("  █▓▒▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐▒▓█")
        print("  ▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦")

        print(" \n------- ❗Ingresa solo❗ ---------")
        print("   ⚠️  letras en minúscula ⚠️")

#------------------------------------------------------------------

        while self.intentos_restantes > 0:
            letra = input("\n🔵 Ingresa una letra 🔵 ⊂( ◉‿◉ )つ \n ► ")

            if len(letra) > 1:
        # ▼ Si se ingresa una palabra completa, se verifica si es correcta
                if self.adivinar_palabra(letra):
                    return
            else:
        # ▼ Si se ingresa una letra, se verifica si es correcta
                self.adivinar_letra(letra)

            palabra_actualizada = self.obtener_palabra_mostrada()
            print(palabra_actualizada)

        # ▼ Verifica si el jugador ha adivinado la palabra completa
            if self.color_oculto == palabra_actualizada:
                print("\n😃 ¡Felicidades, ► {} ◄ ! Adivinaste el color. (ﾉ☉ヮ⚆)ﾉ ⌒*:･ﾟ⭐⭐⭐\n".format(self.nombre))  # noqa: E501)
                mensaje = '''
▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦
      _____.___.               __      __.__                  
      \__  |   | ____  __ __  /  \    /  \__| ____            
       /   |   |/  _ \|  |  \ \   \/\/   /  |/    \           
       \____   (  <_> )  |  /  \        /|  |   |  \          
       / ______|\____/|____/    \__/\  / |__|___|  /          
       \/                            \/          \/           
                                                         
        _________    _____   ____     _______  __ ___________ 
       / ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \\
      / /_/  > __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/
      \___  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   
    /_____/     \/      \/     \/                   \/
 
▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦]
                Desarrollado por    
         🇯  🇴  🇷  🇬  🇪    🇲  🇪  🇷  🇦 \n'''

                print(mensaje)
                return

        print("\n▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦\n")
        print(" ----- ¡Haz perdido! -------")
        print("  ......... _____ ......... ")
        print("  ........ /     \ ........")
        print("  ....... | () () | .......")
        print("  ........ \  ^  / ........")
        print("  ......... ||||| .........")
        print("\nSe te acabaron los intentos.")
        print("El color era: ⬜ - {} - ⬜ \n".format(self.color_oculto))
        print("▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦▦\n")
        print("       Desarrollado por    \n")
        print(" 🇯  🇴  🇷  🇬  🇪    🇲  🇪  🇷  🇦 \n")
        print("")

    def obtener_palabra_mostrada(self):
        # ▼ Obtiene la palabra mostrada hasta el momento, reemplazando las letras no adivinadas por "_"  # noqa: E501
        palabra_mostrada = ""
        for letra in self.color_oculto:
            if letra in self.letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_ "
        return palabra_mostrada

#------------------------------------------------------------------

# Solicitar al usuario que ingrese su nombre
nombre_usuario = input("\n¿Como te llamas?: ")
# Crear una instancia del juego con el nombre del usuario como parámetro
juego = adivina_adivinador_v12(nombre_usuario)
# Iniciar el juego
juego.jugar()

#------------------------------------------------------------------
#------------------------------------------------------------------

# Autor: [Jorge Mera]
# Fecha: [15/07/2023]
# Descripción: [Juego de adivinanzas para adivinar un color oculto]
# Versión: [1.2]

#------------------------------------------------------------------