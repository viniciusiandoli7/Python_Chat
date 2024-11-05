# titulo: hashzap
# botao de "iniciar chat"
# abrir um popup
# titulo: Bem vindo ao HashZap
# campo de texto "Escreva seu nome"
# campo de texto "Entrar"
# "Vinicius entrou no chat" = deve conter um codigo com isso
# campo de texto "Digite uma mensagem"
# botao de "Enviar"
# ira armazenar no tunel de comunicao a mensagem, fazendo com que outra pessoa veja

import flet as ft

# 1 - criar a função principal do sistema (todas as estruturas estarão aqui)

def main(pagina):
    # Criar o elemento da pagina
    titulo = ft.Text("FlashZap")

    #  Função que o tunel irá executar quando for chamado
    def tunel_de_comunicacao(mensagem):

        chat.controls.append(ft.Text(mensagem, size=16))
        

        pagina.update()

        # Criação de tunel de comunicacao - ele enviará as mensagems ou notificações para todos os usuarios conectados no chat
    pagina.pubsub.subscribe(tunel_de_comunicacao)

    def enviar_mensagem(evento):
    #enviar a mensagem no chat
        msg = f"{campo_nome.value}: {campo_mensagem.value}"
    
        # executar o tunel 
        # ele pagará a informação passada e enviará para execução da função
        # que por sua vez irá transmitir para todos os users

        pagina.pubsub.send_all(msg)
     
        # limpar o campo de texto
        campo_mensagem.value = ""

        pagina.update()
        
    campo_mensagem = ft.TextField(label="Digite sua mensagem :D", on_submit= enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    chat = ft.Column()
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])

    def entrar_chat(evento):
        # botao = entrar no chat

        # limpar a tela
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)

        # fechar pop-up
        janela.open=False

        # criar o chat: informar o usuário que entrou no chat
        entrada_usuario = f"{campo_nome.value} entrou no chat"
        
        pagina.pubsub.send_all(entrada_usuario)

        # aparecer um campo de texto = digite sua mensagem e o botao = enviar
        pagina.add(chat)
        pagina.add(linha_mensagem)
        pagina.update()
    
    mensagem_bemvindo = ft.Text(f"Bem vindo ao {titulo.value}")
    campo_nome = ft.TextField(label="Escreva seu nome :D", on_submit= entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click= entrar_chat)

    janela = ft.AlertDialog(
        title=mensagem_bemvindo,
        content= campo_nome,
        actions=[botao_entrar]
    )


    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        print("Clicou no botão")

    
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)




    # Adicionar o elemento da pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    
    
# 2 - Executar o sistema
ft.app(main, view=ft.AppView.WEB_BROWSER)