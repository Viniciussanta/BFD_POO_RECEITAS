class Ingrediente:
    proximo_id = 1

    def __init__(self,nome):
        self.id = Ingrediente.proximo_id
        Ingrediente.proximo_id +=1
        self.nome = nome

class ItemLista:

    proximo_id = 1

    def __init__(self,quantidade,receita,ingrediente):
        self.id = ItemLista.proximo_id
        ItemLista.proximo_id +=1
        self.quantidade = quantidade
        self.receita = receita
        self.ingrediente = ingrediente
    
    def Atualizar_quantidade (self,nova_quantidade):
        
        self.quantidade = nova_quantidade

    def Obter_detalhes(self):
        return f"Ingrediente: {self.ingrediente.nome}, Quantidade: {self.quantidade}"
    
    def obter_detalhes(self):
        
        return f"Ingrediente: {self.ingrediente.nome}, Quantidade: {self.quantidade}"


class Receita:

    proximo_id = 1

    def __init__(self,nome, descricao,passo):
        self.id = Receita.proximo_id
        Receita.proximo_id += 1
        self.nome = nome
        self.descricao = descricao
        self.passo = passo
        self.itens = []

    def adicionar_ingrediente(self, Ingrediente, quantidade):
        novo_items = ItemLista(quantidade,self,Ingrediente)
        self.itens.append(novo_items)
        print(f"'{Ingrediente.nome}' adicionado à receita '{self.nome}'")

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
                print(item.obter_detalhes())
                print("------------------------------------")


print("Definindo insumos da receita...")


instrucoes_do_bolo = """
1. Em uma tigela, misture a farinha, o açúcar e os ovos.
2. Adicione o leite aos poucos e bata bem até a massa ficar homogênea.
3. Despeje a massa em uma forma untada.
4. Leve ao forno pré-aquecido a 180°C por aproximadamente 40 minutos.
5. Espere esfriar para desenformar.
"""


farinha = Ingrediente("Farinha de Trigo")
acucar = Ingrediente("Açúcar")
ovo = Ingrediente("Ovo")
leite = Ingrediente("Leite")
print("Insumos definidos.\n")



print("Criando o objeto Receita...")
bolo_simples = Receita(
    nome="Bolo Simples", 
    descricao="Um bolo fofinho para o café", 
    passo=instrucoes_do_bolo  
)
print(f"Receita '{bolo_simples.nome}' criada.\n")


print("Adicionando ingredientes à receita...")
bolo_simples.adicionar_ingrediente(farinha, "2 xícaras")
bolo_simples.adicionar_ingrediente(acucar, "1 xícara")
bolo_simples.adicionar_ingrediente(ovo, "3 unidades")
bolo_simples.adicionar_ingrediente(leite, "200 ml")



bolo_simples.listar_ingredientes()
bolo_simples.mostrar_preparo()



bolo_simples.remover_ingrediente(2) 



print("\nMostrando a lista de ingredientes após a remoção:")
bolo_simples.listar_ingredientes()