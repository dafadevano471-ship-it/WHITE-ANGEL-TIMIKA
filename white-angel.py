import os, threading
def speak():
    os.system('espeak "White Angel, Defrit, Timika, Papua Tengah Protected" -s 130 > /dev/null 2>&1')
threading.Thread(target=speak).start()
os.system("clear")
print("          .")
print("         // \\\\")
print("        //   \\\\  WHITE ANGEL /")
print("        \\\\   /  DEFRIT - TIMIKA \\\\  //")
print("         \\_/_  _\\_//_")
print("              \\/ \\/")
os.system('figlet -f big "WHITE ANGEL" | lolcat')
os.system('figlet -f small "DEFRIT - TIMIKA" | lolcat')
print("      [ PAPUA TENGAH - PROTECTED ]\n")
0
