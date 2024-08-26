#from bearlibterminal import terminal as blt

# Define variaveis importantes
values = {
    'current_language': None,   # Defina o idioma padrão aqui - pt_BR ; en
    'mode': 0,                  # 0 - CLI; 1 - GUI
    'setup': 0                  # Se abre a tela de setup quando usa pela 1a vez
    }

""" Não sei se será usado:
is_fullscreen = False

def toggle_fullscreen():
    # Função que deixa o jogo em tela-cheia
    global is_fullscreen
    is_fullscreen = not is_fullscreen

    if is_fullscreen:
        blt.set("window: fullscreen=true")
        
    else:
        blt.set("window: fullscreen=false")

    #blt.delay(10)
    blt.refresh()
    clear_input_queue()
    
def clear_input_queue():
    # Clear the input queue
    while blt.has_input():
        blt.read()
"""