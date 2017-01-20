import os

def add_bash_or_fish_segment(powerline):
    # bare : fish
    # bash : bash
    # zsh : zsh

    if powerline.args.shell == 'bare':
        powerline.append(' F ', Color.SSH_FG, Color.SSH_BG)
    else :
        powerline.append(' B ', Color.PATH_FG, Color.PATH_BG)

