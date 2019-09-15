import tcod as libtcod


def handle_keys(key):
    # TECLAS DE MOVIMENTAÇÃO
    if key.vk == libtcod.KEY_UP:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move': (1, 0)}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: colocar em fullscreen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # SAIR DO JOGO
        return {'exit': True}

    # Nenhuma tecla foi pressionada
    return {}