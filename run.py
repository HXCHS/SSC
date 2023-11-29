_IlIllIIIllllIIIIl ='clear'
_IIlIIllIIIIIIlIII ='cls'
_IIIlIIlIIIlllIIll ='nt'
_IIIIllllIllIllIII ='content'
_IIllIllllIlIIlIII ='classification'
_IIIIlllIIlIIIlIIl ='clearance_level'
_IIlIIllIIlllllIlI ='SCA'
_IllIIlllIlIlIIIll ='Student'
_IIlIIlllIIIIllIlI ='SSC'
_IlIIlIlIlllllllll ='password'
import os ,time ,pyfiglet 
from colorama import init ,Fore ,Back ,Style 
init ()
IlIIIIIIIlIIllIll ={'aearnes01':{_IlIIlIlIlllllllll :_IlIIlIlIlllllllll ,_IIIIlllIIlIIIlIIl :_IIlIIlllIIIIllIlI },'dragondung':{_IlIIlIlIlllllllll :'bigdickrandy',_IIIIlllIIlIIIlIIl :_IIlIIlllIIIIllIlI },'daroon':{_IlIIlIlIlllllllll :'sailor',_IIIIlllIIlIIIlIIl :_IllIIlllIlIlIIIll }}
IlIIllllIIIllllIl ={'SSC-Agent-List':{_IIllIllllIlIIlIII :_IIlIIlllIIIIllIlI ,_IIIIllllIllIllIII :'Project Leader: Alexa Earnest, Agent: Donovin Mundie, Agent: Darren Saylor.'},'IperationAlpha':{_IIllIllllIlIIlIII :_IIlIIllIIlllllIlI ,_IIIIllllIllIllIII :"Attempt to 'Break Into' the school through a back door, durring lunch.\nThe Objective is to see if it is possile for anyone, an adult, to break in as well.\n \nAssigned Agents: Alexa Earnest \n \nDate: November 29th, 2023 | C Lunch\n \nResults: Successfully Broke Into the School \n \nDetails: Exited School at the Door at the end of D Hall Near the Activity Directors Office.\n I proceeded to Go to the door at the outside staircase near the C200s, a person came to the door and nodded no,\n they wouldnt let me in. I then walked the path to the YMCA and walked back, \n and headed to door C5 or D5 the one where the courtyard meets C100's and I was let in after I knocked on the door."},'IperationBravo':{_IIllIllllIlIIlIII :_IIlIIllIIlllllIlI ,_IIIIllllIllIllIII :''}}
def IlIlIIIIIlIllIIII ():
	os .system (_IIlIIllIIIIIIlIII if os .name ==_IIIlIIlIIIlllIIll else _IlIllIIIllllIIIIl );IIllIllIllIlllIII =pyfiglet .Figlet (font ='slant');IIIIIllllIIlllIIl =IIllIllIllIlllIII .renderText ('Agent Login');print (IIIIIllllIIlllIIl );IIlIlllIllIIlIIlI =input ('Enter your username: ');IlllIllllIIIIllII =input ('Enter your password: ');print ('Checking authorization...');IllIlIlIlIIlIlllI =20 
	for IlIlIllIIIIIIIIII in range (IllIlIlIlIIlIlllI +1 ):time .sleep (.1 );IIllIlllIllIlIlIl ='='*IlIlIllIIIIIIIIII +' '*(IllIlIlIlIIlIlllI -IlIlIllIIIIIIIIII );print (f"\r[{IIllIlllIllIlIlIl}] {IlIlIllIIIIIIIIII*100//IllIlIlIlIIlIlllI}% ",end ='',flush =True )
	if IIlIlllIllIIlIIlI in IlIIIIIIIlIIllIll and IlllIllllIIIIllII ==IlIIIIIIIlIIllIll [IIlIlllIllIIlIIlI ][_IlIIlIlIlllllllll ]:os .system (_IIlIIllIIIIIIlIII if os .name ==_IIIlIIlIIIlllIIll else _IlIllIIIllllIIIIl );print (f"\n{Fore.GREEN}Authentication successful!{Style.RESET_ALL}");return IlIIIIIIIlIIllIll [IIlIlllIllIIlIIlI ][_IIIIlllIIlIIIlIIl ]
	else :return 
def IIlIlllllllIIllII (IlIllIlIIlIlIlIlI ):
	IIllIIIlIlIlIllII ='-----------------------------------';IlIlIlIIlIlIIIIII =IlIllIlIIlIlIlIlI ;time .sleep (5 );os .system (_IIlIIllIIIIIIlIII if os .name ==_IIIlIIlIIIlllIIll else _IlIllIIIllllIIIIl );IIIIIIIIlIIIllIIl =pyfiglet .Figlet (font ='slant');IIIlIIIlllIlllllI =IIIIIIIIlIIIllIIl .renderText ('SSC Archives');print (IIIlIIIlllIlllllI );print (IIllIIIlIlIlIllII );print ('| Available files:');print (IIllIIIlIlIlIllII )
	for (IlllIlllIllIlIIIl ,IlIlllIIlIlIllIlI )in IlIIllllIIIllllIl .items ():
		IllIlIlIIllIIlIIl =IlIlllIIlIlIllIlI [_IIllIllllIlIIlIII ]
		if IlIlIlIIlIlIIIIII ==_IIlIIlllIIIIllIlI and IllIlIlIIllIIlIIl in [_IIlIIlllIIIIllIlI ,_IIlIIllIIlllllIlI ,_IllIIlllIlIlIIIll ]or IlIlIlIIlIlIIIIII ==_IIlIIllIIlllllIlI and IllIlIlIIllIIlIIl in [_IIlIIllIIlllllIlI ,_IllIIlllIlIlIIIll ]or IlIlIlIIlIlIIIIII ==_IllIIlllIlIlIIIll and IllIlIlIIllIIlIIl ==_IllIIlllIlIlIIIll :print (f"| {Fore.GREEN}{IlllIlllIllIlIIIl} - Classification: {IllIlIlIIllIIlIIl}{Style.RESET_ALL}");print (IIllIIIlIlIlIllII )
def IIlIlIIlllIllIIII (IllIlIIlIlIIlIllI ):
	IIIlIlIIIIIlIllll =IllIlIIlIlIIlIllI 
	if IIIlIlIIIIIlIllll in IlIIllllIIIllllIl :os .system (_IIlIIllIIIIIIlIII if os .name ==_IIIlIIlIIIlllIIll else _IlIllIIIllllIIIIl );print (f"{Fore.YELLOW}File content:{Style.RESET_ALL}\n{Fore.RED}{IlIIllllIIIllllIl[IIIlIlIIIIIlIllll][_IIIIllllIllIllIII]}{Style.RESET_ALL}")
	else :print ('Invalid File Choice.')
def IIlIIIIIIllIlllIl ():
	IIIIllIIIIIlIlIIl =IlIlIIIIIlIllIIII ()
	if IIIIllIIIIIlIlIIl :print (f"Welcome! Your clearance level is {Fore.YELLOW+Style.BRIGHT}{IIIIllIIIIIlIlIIl}{Style.RESET_ALL}.");IIlIlllllllIIllII (IIIIllIIIIIlIlIIl );IIlIllIllIIllIllI =input ('Enter the file you want to view: ');IIlIlIIlllIllIIII (IIlIllIllIIllIllI )
	else :print (f"\n{Fore.RED+Style.BRIGHT}Authentication failed.{Style.RESET_ALL}");time .sleep (2 );IlIlIIIIIlIllIIII ()
if __name__ =='__main__':IIlIIIIIIllIlllIl ()
