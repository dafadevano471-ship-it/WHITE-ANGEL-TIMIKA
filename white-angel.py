import os, threading
def speak():
    os.system('termux-tts-speak "White Angel, Defrit, Timika, Papua Tengah, Protected" &')
threading.Thread(target=speak).start()
os.system("clear")
print("\033[1;37m      .-'`'-.    .-'`'-.      ")
print("   .-'        \\/        '-.   ")
print(".-'   \\  WHITE ANGEL  /   '-.")
print("\033[1;36m\\  \\   /  DEFRIT - TIMIKA  \\  \\   /\033[0m")
print("\033[1;37m '-. \\  .'       '.  / .-'")
print("    '-.'           '.-'\033[0m")
os.system('figlet -f big "WHITE ANGEL" | lolcat')
os.system('figlet -f small "DEFRIT - TIMIKA" | lolcat')
print("\033[1;32m      [ PAPUA TENGAH - PROTECTED ]\033[0m\n")
