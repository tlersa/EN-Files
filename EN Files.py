import marshal, pyfiglet

try:
    import marshal, pyfiglet
except ImportError:
    os.system("pip install marshal")
    os.system("pip install pyfiglet")

    os.system("clear")

#--------------------------------
Black="\033[1;30m"       #Black
Red="\033[1;31m"         #Red
Green="\033[1;32m"       #Green
Yellow="\033[1;33m"      #Yellow
Blue="\033[1;34m"        #Blue
Purple="\033[1;35m"      #Purple
Cyan="\033[1;36m"        #Cyan
White="\033[1;37m"       #White
#--------------------------------

print(Yellow+"""
 _______   ________           ________ ___  ___       _______   ________      
|\  ___ \ |\   ___  \        |\  _____\\  \|\  \     |\  ___ \ |\   ____\     
\ \   __/|\ \  \\ \  \       \ \  \__/\ \  \ \  \    \ \   __/|\ \  \___|_    
 \ \  \_|/_\ \  \\ \  \       \ \   __\\ \  \ \  \    \ \  \_|/_\ \_____  \   
  \ \  \_|\ \ \  \\ \  \       \ \  \_| \ \  \ \  \____\ \  \_|\ \|____|\  \  
   \ \_______\ \__\\ \__\       \ \__\   \ \__\ \_______\ \_______\____\_\  \ 
    \|_______|\|__| \|__|        \|__|    \|__|\|_______|\|_______|\_________\
                                                                  \|_________|                                                                                                      
""")
print(White+"This Tool Was Programmed By : TLER AL-BISHI", "\nWebsite For All Accs : "+Blue+"https://linktr.ee/tler.sa")
print(White+"- "*25)

filee = input(Red+"[+] - Write The File Name Or Path : ")

open_file = open(filee, 'r').read()

compile_file = compile(open_file, '', 'exec')

encrypt_file = marshal.dumps(compile_file)

encrypt_code = open('New_'+str(filee), 'w')

encrypt_code.write('import marshal\nexec(marshal.loads('+repr(encrypt_file)+'))')

print(Green+"The File Has Been Successfully Encrypted! : "+str(filee))