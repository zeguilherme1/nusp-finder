import requests
import argparse
import string
import interacoes


def requisicao(id):
    url = f"https://icmc.usp.br/pessoas?id={id}"
    response = requests.get(url)
    cookies = response.cookies

    img_nome_value = cookies.get('imgNome')

    if img_nome_value:
        img_nome_value = img_nome_value.replace("+", " ")
        print(f"Nome: {img_nome_value}, NUSP:", int((id - 3) / 2))


def one_nusp_only():
    nusp  = int(input("Insira o número USP da pessoa que você deseja encontrar (ex. XXXXXX): "))
    id =  (nusp*2) + 3
    requisicao(id)


def multi_nusp():
    nusp =  input("Insira os NUSP's separados por um espaço (ex. XXXXXX XXXXXX XXXXXX): ")
    array_nusp = list(map(int, nusp.split()))
    for nusp in array_nusp:
        requisicao((nusp * 2) + 3)
    
def main():
    interacoes.menu()
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--single', action='store_true', help="Opção usada caso deseje encontrar apenas um número USP")
    parser.add_argument('--multi', action='store_true', help="Opção usada caso deseje encontrar vários números USP")
    args = parser.parse_args()

    if args.single:
        one_nusp_only()
    elif args.multi:
        multi_nusp()
if __name__ == '__main__':
    main()