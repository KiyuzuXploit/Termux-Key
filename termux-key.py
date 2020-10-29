import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
d ='\033[96m'
e ='\033[93m'
f ='\033[90m'

def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)
    os.system('termux-reload-settings')


def banner():
    os.system('clear')
    print(d+'Termux Key'.center(40))
    print(a+'Shortcut for help you'.center(40))
    print(b+'Author : Mr.Kiyuzu'.center(40))
    print("".join([i for i in "\n"*3]))


if __name__=='__main__':
    banner()
    from threading import Thread as td
    t = td(target=setup)
    t.start()
    while t.is_alive():
        for i in "-\|/-\|/\|/-\|/-\|/-\|/":
            print('\rManambahkan tombol '+i+' ',end="",flush=True)
            sleep(0.1)
    banner()
    print(a+'[•] Succes [•]')
    print(c+'[•] Tombol udh di tambahin bro ^_^ [•]')

# ini cuma shortcut buat bantu para nub