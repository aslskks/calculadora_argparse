import sys
import argparse


def com(valor: str):
    if valor is None:
        print("Error: Debes proporcionar un valor para la operación.")
        sys.exit(1)

    if not valor.replace(".", "").isdigit():
        print(f"{valor} no es válido")
        sys.exit(1)
    elif valor.isdigit():
        valor = int(valor)
    else:
        valor = float(valor)
    return valor


def sumar(n1, n2):
    return n1 + n2


def restar(n1, n2):
    return n1 - n2


def div(n1, n2):
    return n1 / n2


def div_sin_punto(n1, n2):
    return n1 // n2


def multi(n1, n2):
    return n1 * n2


def poten(n1, n2):
    return n1 ** n2


def pregunta(args):
    n1 = com(args.n1)
    n2 = com(args.n2)
    resultado = None

    if args.operation == "suma":
        resultado = sumar(n1, n2)
    elif args.operation == "restar":
        resultado = restar(n1, n2)
    elif args.operation == "dividir":
        resultado = div(n1, n2)
    elif args.operation == "dividir_sin_decimal":
        resultado = div_sin_punto(n1, n2)
    elif args.operation == "multiplicacion":
        resultado = multi(n1, n2)
    elif args.operation == "potencia":
        resultado = poten(n1, n2)

    return str(resultado)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n1', type=str, help="elige el primer número")
    parser.add_argument('--n2', type=str, help="ingresa el segundo número")
    parser.add_argument('--operation', type=str, help="ingresa la operación")
    args = parser.parse_args()

    if not any([args.n1, args.n2, args.operation]):
        print("Error: Debes proporcionar al menos uno de los argumentos: --n1, --n2, --operation.")
        sys.exit(1)

    sys.stdout.write(str(pregunta(args)))


if __name__ == "__main__":
    main()
