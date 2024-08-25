def menu():
    print("Escolha uma opção:\n")
    print("1 - Criar usuario")
    print("2 - Deletar usuario")
    print("3 - Atualizar usuario")
    print("4 - Listar usuario")
    global menu_value
    menu_value = int(input("Digite um numero da opçao: "))
    return menu_value
    
def check_option(option):
    if option < 1 or option > 4:
         return True
    
def main():
    while check_option(menu()):
        print("valor Invalido")
        
       

if __name__=="__main__":
    main()