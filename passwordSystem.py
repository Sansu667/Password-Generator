import random
import string

# Functions
def crearContraseña(lengthUser):

    # Conjunto de caracteres: letras, dígitos y símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generar una contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(lengthUser))
    return contrasena

def main():
    print("Password generator")
    while True:
        try:
            lengthUser = int(input("Ingrese la longitud de su contraseña: "))
            if lengthUser <= 5:
                print("Tu contraseña debe ser mayor de 5 carácteres para mayor seguridad")
                continue
            password = crearContraseña(lengthUser)
            print("Tu contraseña generada es: {}".format(password))
            break
        except ValueError:
            print("Introduce un número válido")

# Conditional
if __name__ == "__main__":
    main()