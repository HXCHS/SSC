import os #line:1
import time #line:2
import pyfiglet #line:3
from colorama import init ,Fore ,Back ,Style #line:5
init ()#line:6
users ={"aearnes01":{"password":"password","clearance_level":"SSC"},"dragondung":{"password":"bigdickrandy","clearance_level":"SSC"},"daroon":{"password":"sailor","clearance_level":"Student"}}#line:13
files ={"SSC-Agent-List":{"classification":"SSC","content":"Project Leader: Alexa Earnest, Agent: Donovin Mundie, Agent: Darren Saylor."},"OperationAlpha":{"classification":"SCA","content":"Attempt to 'Break Into' the school through a back door, durring lunch.\nThe Objective is to see if it is possile for anyone, an adult, to break in as well.\n \nAssigned Agents: Alexa Earnest \n \nDate: November 29th, 2023 | C Lunch\n \nResults: Successfully Broke Into the School \n \nDetails: Exited School at the Door at the end of D Hall Near the Activity Directors Office.\n I proceeded to Go to the door at the outside staircase near the C200s, a person came to the door and nodded no,\n they wouldnt let me in. I then walked the path to the YMCA and walked back, \n and headed to door C5 or D5 the one where the courtyard meets C100's and I was let in after I knocked on the door."},"OperationBravo":{"classification":"SCA","content":""},}#line:20
def authenticate ():#line:23
    os .system ('cls'if os .name =='nt'else 'clear')#line:24
    OO00O00O0000O0OOO =pyfiglet .Figlet (font ='slant')#line:25
    O00000OO000O0O000 =OO00O00O0000O0OOO .renderText ('Agent Login')#line:26
    print (O00000OO000O0O000 )#line:27
    OO0OO000OOOO00O0O =input ("Enter your username: ")#line:28
    O00O0OOOO0000OOOO =input ("Enter your password: ")#line:29
    print ("Checking authorization...")#line:32
    O0OO00O000O0OOOOO =20 #line:33
    for O00000000OO000O0O in range (O0OO00O000O0OOOOO +1 ):#line:34
        time .sleep (0.1 )#line:35
        OOO000OOOOOO0000O ="="*O00000000OO000O0O +" "*(O0OO00O000O0OOOOO -O00000000OO000O0O )#line:36
        print (f"\r[{OOO000OOOOOO0000O}] {O00000000OO000O0O * 100 // O0OO00O000O0OOOOO}% ",end ="",flush =True )#line:37
    if OO0OO000OOOO00O0O in users and O00O0OOOO0000OOOO ==users [OO0OO000OOOO00O0O ]["password"]:#line:39
        os .system ('cls'if os .name =='nt'else 'clear')#line:40
        print (f"\n{Fore.GREEN}Authentication successful!{Style.RESET_ALL}")#line:41
        return users [OO0OO000OOOO00O0O ]["clearance_level"]#line:42
    else :#line:43
        return None #line:44
def display_files (O0OOOOO0OOOO0O000 ):#line:48
    time .sleep (5 )#line:49
    os .system ('cls'if os .name =='nt'else 'clear')#line:50
    O00O000O0OO00O0O0 =pyfiglet .Figlet (font ='slant')#line:51
    O0OO0O0000000O000 =O00O000O0OO00O0O0 .renderText ('SSC Archives')#line:52
    print (O0OO0O0000000O000 )#line:53
    print ("-----------------------------------")#line:54
    print ("| Available files:")#line:55
    print ("-----------------------------------")#line:56
    for O000O0O0O00OO000O ,O000O000OOO0O0OO0 in files .items ():#line:57
        OOO0O0O0OOOOOOOOO =O000O000OOO0O0OO0 ["classification"]#line:58
        if (O0OOOOO0OOOO0O000 =="SSC"and OOO0O0O0OOOOOOOOO in ["SSC","SCA","Student"])or (O0OOOOO0OOOO0O000 =="SCA"and OOO0O0O0OOOOOOOOO in ["SCA","Student"])or (O0OOOOO0OOOO0O000 =="Student"and OOO0O0O0OOOOOOOOO =="Student"):#line:61
            print (f"| {Fore.GREEN}{O000O0O0O00OO000O} - Classification: {OOO0O0O0OOOOOOOOO}{Style.RESET_ALL}")#line:62
            print ("-----------------------------------")#line:63
def view_file_content (O0O0000000OO0OOOO ):#line:67
    if O0O0000000OO0OOOO in files :#line:68
        os .system ('cls'if os .name =='nt'else 'clear')#line:69
        print (f"{Fore.YELLOW}File content:{Style.RESET_ALL}\n{Fore.RED}{files[O0O0000000OO0OOOO]['content']}{Style.RESET_ALL}")#line:70
    else :#line:71
        print ("Invalid File Choice.")#line:72
def main ():#line:74
    O00O000O0O0OOO00O =authenticate ()#line:75
    if O00O000O0O0OOO00O :#line:76
        print (f"Welcome! Your clearance level is {Fore.YELLOW + Style.BRIGHT}{O00O000O0O0OOO00O}{Style.RESET_ALL}.")#line:77
        display_files (O00O000O0O0OOO00O )#line:78
        OO00O00OO0O000000 =input ("Enter the file you want to view: ")#line:79
        view_file_content (OO00O00OO0O000000 )#line:80
    else :#line:81
        print (f"\n{Fore.RED + Style.BRIGHT}Authentication failed.{Style.RESET_ALL}")#line:82
        time .sleep (2 )#line:83
        authenticate ()#line:84
if __name__ =="__main__":#line:86
    main ()#line:87
