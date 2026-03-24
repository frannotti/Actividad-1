import random
categorias = {
   "lenguajes": ["python", "programa", "variable", "entero"],
   "estructuras": ["funcion", "bucle", "cadena", "lista"]
}

print("categorias disponibles: ")
for cat in categorias:
   print("-", cat)

choice = input("Elige una categoria: ")
word = random.choice(categorias[choice])

guessed = []
attempts = 6
score = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
           progress += letter + " "
        else:
           progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
       print("¡Ganaste!")
       score += 6
       break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    if len(letter) != 1 or not letter.isalpha():
       print("Entrada no valida ")
       continue 

    if letter in guessed:
       print("Ya usaste esa letra.")
    elif letter in word:
       guessed.append(letter)
       print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        score -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    score = 0
    print(f"¡Perdiste! La palabra era: {word}")
print(f"puntaje final: {score}")