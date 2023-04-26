from pystyle import*
from pytube import YouTube
import speedtest
# pip3 install pystyle
# pip3 install pytube
# pip3 install speedtest-cli

print("\33[34m")
print(Box.Lines("[+]Youtube[+]"))
Write.Print("Welcome in my [+]Program[+]\n",Colors.red_to_purple,interval=0.1)
while(True):
    print("\33[34m")
    print(Box.DoubleCube("Choose"))
    Write.Print("1- High Quality\n2- Low Quality\n3- IF you need [+]Finish[+]",Colors.green_to_yellow, interval=0.1)
    print("\33[33m")
    user=eval(input(">> "))
    if(user== 1):
        print("\33[36m")
        print(Box.DoubleCube("High Quality"))
        url=Write.Input("URL: ",Colors.cyan_to_blue,interval=0.1)
        tube=YouTube(url).streams.get_highest_resolution().download("C:/Users/ahmed gmal/Downloads")
        Write.Print("Download is [+]Successful[+]\n",Colors.green_to_yellow,interval=0.1)
        test=speedtest.Speedtest()
        down=test.download()
        miga=round(down/10**6,2)
        Write.Print("Speed of [+]Download[+]: ",Colors.green_to_white,interval=0.1)
        print(miga,"\33[32mMiga")
    elif(user== 2):
        print("\33[36m")
        print(Box.DoubleCube("Low Quality"))
        url=Write.Input("URL: ",Colors.cyan_to_blue,interval=0.1)
        tube=YouTube(url).streams.get_lowest_resolution().download("C:/Users/ahmed gmal/Downloads")
        Write.Print("Download is [+]Successful[+]\n",Colors.green_to_yellow,interval=0.1)
        test=speedtest.Speedtest()
        down=test.download()
        miga=round(down/10**6,2)
        Write.Print("Speed of [+]Download[+]: ",Colors.green_to_white,interval=0.1)
        print(miga,"\33[32mMiga")
    elif(user== 3):
        Write.Print("Thank you for using \U0001F600",Colors.red_to_white)
        break;
    else:
        Write.Print("[+]ERROR[+] Please again!",Colors.purple_to_blue)



