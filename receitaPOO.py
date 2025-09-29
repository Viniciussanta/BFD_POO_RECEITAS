class Ingrediente:
    proximo_id = 1

    def __init__(self,nome):
        self.id = Ingrediente.proximo_id
        Ingrediente.proximo_id +=1
        self.nome = nome

class ItemLista:
    proximo_id = 1

    def __init__(self, quantidade, receita, ingrediente):
        self.id = ItemLista.proximo_id
        ItemLista.proximo_id +=1
        self.quantidade = quantidade
        self.receita = receita
        self.ingrediente = ingrediente
    
    def atualizar_quantidade (self, nova_quantidade):        
        self.quantidade = nova_quantidade

    def __str__(self):
        return f"Ingrediente: {self.ingrediente.nome}, Quantidade: {self.quantidade}"


class Receita:
    proximo_id = 1

    def __init__(self, nome, descricao, passo):
        self.id = Receita.proximo_id
        Receita.proximo_id += 1
        self.nome = nome
        self.descricao = descricao
        self.passo = passo
        self.itens = []

    def adicionar_ingrediente(self, ingrediente, quantidade):
        novo_items = ItemLista(quantidade, self, ingrediente)
        self.itens.append(novo_items)
        print(f"'{ingrediente.nome}' adicionado à receita '{self.nome}'")

    def mostrar_preparo(self):
        print(f"\n--- Modo de Preparo: {self.nome} ---")
        print(self.passo) 
        print("-----------------------------------------")

    def remover_ingrediente(self, ingrediente_id):
        itens_remover = None
        for item in self.itens:
            if item.ingrediente.id == ingrediente_id:
                itens_remover = item
                break
        if itens_remover:
            self.itens.remove(itens_remover)
            print(f"Ingrediente com ID {ingrediente_id} removido da receita '{self.nome}'.")
        else:
            print(f"Ingrediente com ID {ingrediente_id} não encontrado na receita.")
    
    def listar_ingredientes(self):
        print(f"\n--- Ingredientes para: {self.nome} ---")
        if not self.itens:
            print("Nenhum ingrediente na lista.")
        else:
            for item in self.itens:
                print(item)
                print("------------------------------------")


print("Definindo insumos da receita...")

instrucoes_do_bolo = """
1. Em uma tigela, misture a farinha, o açúcar e os ovos.
2. Adicione o leite aos poucos e bata bem até a massa ficar homogênea.
3. Despeje a massa em uma forma untada.
4. Leve ao forno pré-aquecido a 180°C por aproximadamente 40 minutos.
5. Espere esfriar para desenformar.
"""

bolo_simples = Receita(
    nome="Bolo Simples",
    descricao="Um bolo fofinho para o café.",
    passo=instrucoes_do_bolo
)
print(f"Receita '{bolo_simples.nome}' criada.\n")

ingredientes_disponiveis = {
    1: Ingrediente("Farinha de Trigo"),
    2: Ingrediente("Açúcar"),
    3: Ingrediente("Ovo"),
    4: Ingrediente("Leite")
}

while True:
    print("\nMENU RECEITA")
    print("1 - Adicionar ingrediente")
    print("2 - Listar ingredientes")
    print("3 - Remover ingrediente")
    print("4 - Mostrar preparo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nIngredientes disponíveis:")
        for id_ing, ing in ingredientes_disponiveis.items():
            print(f"{id_ing} - {ing.nome}")
        try:
            escolha = int(input("Digite o ID do ingrediente: "))
            quantidade = input("Digite a quantidade: ")
            if escolha in ingredientes_disponiveis:
                bolo_simples.adicionar_ingrediente(ingredientes_disponiveis[escolha], quantidade)
            else:
                print("Ingrediente inválido.")
        except ValueError:
            print("Entrada inválida. Use números para o ID.")

    elif opcao == "2":
        bolo_simples.listar_ingredientes()

    elif opcao == "3":
        try:
            id_remover = int(input("Digite o ID do ingrediente para remover: "))
            bolo_simples.remover_ingrediente(id_remover)
        except ValueError:
            print("Entrada inválida. Use números para o ID.")

    elif opcao == "4":
        bolo_simples.mostrar_preparo()

    elif opcao == "0":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, tente novamente!")
