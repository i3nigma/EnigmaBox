
import os
import sys, traceback

def banner():
    print('''

                                                                                         
 \33[33m      ,ggggggg,                                                               ,ggggggggggg,                             
     ,dP""""""Y8b                                                             dP"""88""""""Y8,                           
     d8'    a  Y8                                                             Yb,  88      `8b                           
     88     "Y8P'                gg                                            `"  88      ,8P                           
     `8baaaa                     ""                                                88aaaad8P"\33[;m                            
\33[31m    ,d8P""""       ,ggg,,ggg,    gg     ,gggg,gg   ,ggg,,ggg,,ggg,     ,gggg,gg    88""""Y8ba    ,ggggg,       ,gg,   ,gg
    d8"           ,8" "8P" "8,   88    dP"  "Y8I  ,8" "8P" "8P" "8,   dP"  "Y8I    88      `8b  dP"  "Y8ggg   d8""8b,dP" 
    Y8,           I8   8I   8I   88   i8'    ,8I  I8   8I   8I   8I  i8'    ,8I    88      ,8P i8'    ,8I    dP   ,88"   \33[;m 
\33[32m    `Yba,,_____, ,dP   8I   Yb,_,88,_,d8,   ,d8I ,dP   8I   8I   Yb,,d8,   ,d8b,   88_____,d8',d8,   ,d8'  ,dP  ,dP"Y8, 
      `"Y8888888 8P'   8I   `Y88P""Y8P"Y8888P"8888P'   8I   8I   `Y8P"Y8888P"`Y8  88888888P"  P"Y8888P"    8"  dP"   "Y88
                                            ,d8I' \33[;m                                                                        
          Welcome to EnigmaBox!           \33[32m,dP'8I \33[;m                                                                        
                                         \33[32m,8"  8I \33[;m                                                                       
                                        \33[32m I8   8I \33[;m \33[100m#~>>>   Author: i3nigma (TheDarkIndian) - Contact: facebook.com/i3nigma17\33[;m                                                                      
                                         \33[32m`8, ,8I\33[;m                                                                         
                                          \33[32m`Y8P"  \33[;m                                                                        

\033[1m                                                                                        
#--->   By using EnigmaBox you can clone almost 60+ scripts & tools           <---#
#--->   In new versions I will update with fresh tools                        <---#
\033[;m
''')
def main():
    try:
	    print("""
	    \033[40mSpecify the category:\033[;m
	    \33[31m1: Bruteforce Scripts
	    2: Information Gathering tools
	    3: Web Application Hacking tools
	    4: Exploitation tools
	    \33[;m
	    """)

	    choice = raw_input('Select the category --> ')
	    if choice == '1':
		print("""
		\33[33m>>> \33[31mBruteforce Scripts
		\33[33m1: \33[92mWoodpecker - \33[34mhash Bruteforce
		\33[33m2: \33[92mDagon - \33[34mAdvanced Hash Manipulation
		\33[33m3: \33[92m3vilSSH - \33[34mSSH Protocol Bruteforcer & password list
		\33[33m4: \33[92mBlindy - \33[34mSimple Script for running BruteForce Blind MySql Injection
		\33[33m5: \33[92mXSStrike v1.2 - \33[34mFuzz, Crawl and Bruteforce Parameters for XSS
		\33[33m6: \33[92mBruteSploit - \33[34mCollection Of Method For Automated Generate, Bruteforce And Manipulation Wordlist
		\33[33m7: \33[92mLINSET - \33[34mWPA/WPA2 Hack Without Brute Force
		\33[33m8: \33[92mWfuzz - \33[34mThe Web Application Bruteforcer
		\33[33m9: \33[92mSentry - \33[34mBruteforce Attack Blocker
		\33[33m10: \33[92m[BTCrack v1.1] - \33[34mThe worlds first Bluetooth Pass phrase (PIN) Bruteforce Tool
		\33[33m11: \33[92mCrowbar - \33[34mBrute Forcing Tool for Pentests
		\33[33m12: \33[92mIPTV Brute-Force - \33[34mSearch And Brute Force Illegal IPTV Server
		\33[33m13: \33[92mbrut3k1t - \33[34mServer-side Brute-force Module (ssh, ftp, smtp, facebook, and more)
		\33[33m14: \33[92mdedsploit - \33[34mFramework for attacking network protocols
		\33[33m15: \33[92mPatator -\33[34mis a multi-purpose brute-forcer, with a modular design and a flexible usage
		\33[33m16: \33[92mHash Buster -\33[34m A Script Which Scraps Online Hash Crackers (MD5, SHA1, SHA2)
		\33[33m00: \33[92mBack to -\33[34m Main menu""")
	    	print ("\33[90mSelect the tool to clone\33[90m")
	    	opcion1 = raw_input("\33[31mEnigmaBox@r00t > \33[31m")
	  	
		if opcion1 == "1":
	     	   cmd = os.system("git clone https://github.com/ForceBru/HashBrute.git")
	    	elif opcion1 == "2":
		   cmd = os.system("git clone https://github.com/ekultek/dagon.git	")
		elif opcion1 == "3":
		   cmd = os.system("git clone https://github.com/i3nigma/3vilSSH.git")
		elif opcion1 == "4":
		   cmd = os.system("git clone https://github.com/missDronio/blindy.git")
		elif opcion1 == "5":
		   cmd = os.system("git clone https://github.com/UltimateHackers/XSStrike.git")
		elif opcion1 == "6":
		   cmd = os.system("git clone https://github.com/Screetsec/BruteSploit.git")
		elif opcion1 == "7":
		   cmd = os.system("git clone https://github.com/vk496/linset.git")
		elif opcion1 == "8":
		   cmd = os.system("git clone https://github.com/xmendez/wfuzz.git")
		elif opcion1 == "9":
		   cmd = os.system("git clone https://github.com/msimerson/sentry.git")
		elif opcion1 == "10":
		   cmd = os.system("git clone https://github.com/thierryzoller/BTcrack---Open-Source.git")
		elif opcion1 == "11":
		   cmd = os.system("git clone https://github.com/galkan/crowbar.git")
		elif opcion1 == "12":
		   cmd = os.system("git clone https://github.com/Pinperepette/IPTV.git")
		elif opcion1 == "13":
		   cmd = os.system("git clone https://github.com/ex0dus-0x/brut3k1t.git")
		elif opcion1 == "14":
		   cmd = os.system("git clone hhttps://github.com/ex0dus-0x/dedsploit.git")
		elif opcion1 == "15":
		   cmd = os.system("git clone https://github.com/lanjelot/patator.git")
		elif opcion1 == "16":
		   cmd = os.system("git clone https://github.com/UltimateHackers/Hash-Buster.git")
		elif opcion1 == "00":
		   main()

		else:
		   print("[!] Invalid Command")

	    if choice == '2':
		print("""
		\33[33m>>> \33[31mInformation Gathering Tools
		\33[33m1: \33[92mSn1per - \33[34mAutomated PenTest Recon Scanner
		\33[33m2: \33[92mDracnmap v2.2 - \33[34mExploit Network and Gathering Information with Nmap
		\33[33m3: \33[92mRED HAWK - \33[34mAll In One Tool For Information Gathering
		\33[33m4: \33[92mReconnoitre - \33[34mA Security Tool For Multithreaded Information Gathering And Service Enumeration
		\33[33m5: \33[92mJust-Metadata - \33[34mTool that Gathers and Analyzes Metadata about IP Addresses
		\33[33m6: \33[92mFlashlight - \33[34mAutomated Information Gathering Tool for Penetration Testers
		\33[33m7: \33[92m[LinEnum v0.2] -\33[34mAutomating local information gathering tasks on Linux hosts
		\33[33m8: \33[92mReconDog -\33[34m An All In One Tool For All Your Basic Information Gathering Needs
		\33[33m9: \33[92mDMitry -\33[34m Deepmagic Information Gathering Tool
		\33[33m10: \33[92mwig -\33[34m WebApp Information Gatherer
		\33[33m11: \33[92mPassive Spider -\33[34m Information Gathering from Search Engine Tool
		\33[33m12: \33[92m[Creepy] Geolocation -\33[34minformation Gathering through Social Networking Platforms
		\33[33m13: \33[92mInfoga v3.0 -\33[34m Email Information Gathering
		\33[33m14: \33[92mAngryFuzzer -\33[34m Tool for Information Gathering
		\33[33m15: \33[92mSnitch -\33[34m Information Gathering via dorks
		\33[33m16: \33[92mShodanwave -\33[34m Explore & Obtain Information from Netwave IP Camera
		\33[33m00: \33[92mBack to -\33[34m Main menu""")
	   	print ("\33[90mSelect the tool to clone\33[90m")
	    	opcion2 = raw_input("\33[31mEnigmaBox@r00t > \33[31m")

	    
	    	if opcion2 == "1":
		    cmd = os.system("git clone https://github.com/1N3/Sn1per.git")
	    	elif opcion2 == "2":
		    cmd = os.system("git clone https://github.com/Screetsec/Dracnmap.git")
	    	elif opcion2 == "3":
		    cmd = os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
	    	elif opcion2 == "4":
		    cmd = os.system("git clone https://github.com/codingo/Reconnoitre.git")
	    	elif opcion2 == "5":
		    cmd = os.system("git clone https://github.com/ChrisTruncer/Just-Metadata.git")
	    	elif opcion2 == "6":
		    cmd = os.system("git clone https://github.com/galkan/flashlight.git")  
	    	elif opcion2 == "7":
		    cmd = os.system("git clone https://github.com/rebootuser/LinEnum.git")
	    	elif opcion2 == "8":
		    cmd = os.system("git clone https://github.com/UltimateHackers/ReconDog.git")
	    	elif opcion2 == "9":
		    cmd = os.system("git clone https://github.com/jaygreig86/dmitry.git")
	    	elif opcion2 == "10":
		    cmd = os.system("git clone https://github.com/jekyc/wig.git")
	    	elif opcion2 == "11":
		    cmd = os.system("git clone https://github.com/RandomStorm/passive-spider.git")
	    	elif opcion2 == "12":
		    cmd = os.system("git clone https://github.com/ilektrojohn/creepy.git")
	    	elif opcion2 == "13":
		    cmd = os.system("git clone https://github.com/m4ll0k/Infoga.git")
	    	elif opcion2 == "14":
		    cmd = os.system("git clone https://github.com/ihebski/angryFuzzer.git")
	     	elif opcion2 == "15":
		    cmd = os.system("git clone https://github.com/Smaash/snitch.git")
	    	elif opcion2 == "16":
		    cmd = os.system("git clone https://github.com/fbctf/shodanwave.git")
	    	elif opcion2 == "00":
		    main()

	    	else:
		    print("[!] Invalid Command")
	 
	    if choice == '3':
		print("""
		\33[33m>>> \33[31mWeb application vulnerability scanners
		\33[33m1: \33[92mWebVulScan -\33[34m Web Application Vulnerability Scanner
		\33[33m2: \33[92mNagaScan -\33[34m Distributed Passive Scanner for Web Application
		\33[33m3: \33[92mWPSeku v0.2 -\33[34m Wordpress Security Scanner
		\33[33m4: \33[92mPybelt -\33[34m The Hackers Tool Belt
		\33[33m5: \33[92mBackdoorMan -\33[34m Toolkit That Helps You Find Malicious, Hidden And Suspicious PHP Scripts And Shells
		\33[33m6: \33[92mOpenDoor -\33[34m OWASP Directory Access Scanner
		\33[33m7: \33[92mLFISuite -\33[34m Totally Automatic LFI Exploiter (+ Reverse Shell) and Scanner
		\33[33m8: \33[92mDroopescan -\33[34m A plugin-based scanner that aids researchers in identifying issues with several CMSs
		\33[33m9: \33[92mWhitewidow 1.5.0 -\33[34m SQL Vulnerability Scanner
		\33[33m10: \33[92mYawast -\33[34m The YAWAST Antecedent Web Application Security Toolkit
		\33[33m11: \33[92mRaptor -\33[34m Web-based Source Code Vulnerability Scanner
		\33[33m12: \33[92mHellRaiser -\33[34m Vulnerability Scanner
		\33[33m13: \33[92mSCANNER -\33[34m INURLBR
		\33[33m14: \33[92mPopular Pentesting scanner in Python3.6 -\33[34m for SQLi/XSS/LFI/RFI and other Vulns
		\33[33m15: \33[92mWordpress Exploit Framework -\33[34m Developing and using modules which aid in the penetration testing of WP sites
		\33[33m16: \33[92mTNscan -\33[34m CMS Scanner
		\33[33m17: \33[92mUniscan -\33[34m Web vulnerability scanner
		\33[33m18: \33[92mATSCAN -\33[34m Advanced Search & Mass Exploit Scanner
		\33[33m19: \33[92mCMSmap -\33[34m Automates the process of detecting security flaws of the most popular CMSs
		\33[33m20: \33[92mKadimus -\33[34m is a tool to check sites to lfi vulnerability , and also exploit it

		\33[33m00: \33[92mBack to -\33[34m Main menu""")
	    	print ("\33[90mSelect the tool to clone\33[90m")
	    	opcion3 = raw_input("\33[31mEnigmaBox@r00t > \33[31m")
	    
		if opcion3 == "1":
		    cmd = os.system("git clone https://github.com/dermotblair/webvulscan.git")
	    	elif opcion3 == "2":
		    cmd = os.system("git clone https://github.com/brianwrf/NagaScan.git")
	  	elif opcion3 == "3":
		    cmd = os.system("git clone https://github.com/m4ll0k/WPSeku.git")
	    	elif opcion3 == "4":
		    cmd = os.system("git clone https://github.com/Ekultek/Pybelt.git")
	    	elif opcion3 == "5":
		    cmd = os.system("git clone https://github.com/yassineaddi/BackdoorMan.git")
	    	elif opcion3 == "6":
		    cmd = os.system("git clone https://github.com/stanislav-web/OpenDoor.git")        
	    	elif opcion3 == "7":
		    cmd = os.system("git clone https://github.com/D35m0nd142/LFISuite.git")       
	    	elif opcion3 == "8":
		    cmd = os.system("git clone https://github.com/droope/droopescan.git")       
	    	elif opcion3 == "9":
		    cmd = os.system("git clone https://github.com/Ekultek/whitewidow.git")        
	    	elif opcion3 == "10":
		    cmd = os.system("git cloneh ttps://github.com/adamcaudill/yawast.git")        
	    	elif opcion3 == "11":
		    cmd = os.system("git clone https://github.com/dpnishant/raptor.git")        
	    	elif opcion3 == "12":
		    cmd = os.system("git clone https://github.com/m0nad/HellRaiser.git")       
	    	elif opcion3 == "13":
		    cmd = os.system("git clone https://github.com/googleinurl/SCANNER-INURLBR.git")       
	    	elif opcion3 == "14":
		    cmd = os.system("git clone https://github.com/v3n0m-Scanner/V3n0M-Scanner.git")
	    	elif opcion3 == "15":
		    cmd = os.system("git clone https://github.com/rastating/wordpress-exploit-framework.git")
	    	elif opcion3 == "16":
		    cmd = os.system("git clone https://github.com/voletri/TNscan.git")       
	    	elif opcion3 == "17":
		    cmd = os.system("git clone https://github.com/poerschke/Uniscan.git")
	    	elif opcion3 == "18":
		    cmd = os.system("git clone https://github.com/AlisamTechnology/ATSCAN.git")       
	    	elif opcion3 == "19":
		    cmd = os.system("git clone https://github.com/Dionach/CMSmap.git")          
	    	elif opcion3 == "20":
		    cmd = os.system("git clone https://github.com/P0cL4bs/Kadimus.git")  
	    	elif opcion3 == "00":
		    main()

	    	else:
		    print("[!] Invalid Command")

	    if choice == '4':
		print("""
		\33[33m>>> \33[31mExploitation Tools
		\33[33m1: \33[92mEternalblue Doublepulsar -\33[34m Metasploit 
		\33[33m2: \33[92mThe Shadow Brokers -\33[34m Exploits
		\33[33m3: \33[92mNSA finest tool -\33[34m Fuzzbunch
		\33[33m4: \33[92mWinpayloads -\33[34m Undetectable Windows Payload Generation
		\33[33m5: \33[92mTheFatRat v1.8 -\33[34m Easy Tool For Generate Backdoor with Msfvenom
		\33[33m6: \33[92mStitch -\33[34m Python Remote Administration Tool (RAT)
		\33[33m7: \33[92mP0wnedShell -\33[34m PowerShell Runspace Post Exploitation Toolkit
		\33[33m8: \33[92mArchive -\33[34m leaked Equation Group materials
		\33[33m9: \33[92mBrutal -\33[34m Toolkit to quickly create various Payload
		\33[33m10: \33[92mBackdoorMe -\33[34m Powerful Auto-Backdooring Utility
		\33[33m11: \33[92mbackdoor-apk -\33[34m shell script that simplifies the process of adding a backdoor to any Android APK file
		\33[33m12: \33[92mDr0p1t Framework 1.3 -\33[34m A Framework That Creates An Advanced FUD Dropper With Some Tricks
		\33[33m13: \33[92mBrowserBackdoor -\33[34m Secure JavaScript WebSocket Backdoor and a Ruby Command-Line Listener
		\33[33m14: \33[92mNXcrypt -\33[34m Python Backdoor Framework
		\33[33m15: \33[92mWeevely3 -\33[34m Weaponized Web Shell
		\33[33m16: \33[92ml0l -\33[34m The Exploit Development Kit
		\33[33m17: \33[92mkimi -\33[34m Script To Generate Malicious Debian Packages (Debian Trojans)
		\33[33m18: \33[92mvenom -\33[34m (metasploit) shellcode generator/compiler/listener
		\33[33m19: \33[92mnWatch -\33[34m Tool for Host Discovery, PortScanning and Operating System Fingerprinting

		\33[33m00: \33[92mBack to -\33[34m Main menu""")
	 	print ("\33[90mSelect the tool to clone\33[90m")
	    	opcion4 = raw_input("\33[31mEnigmaBox@r00t > \33[31m")
	    
		if opcion4 == "1":
		    cmd = os.system("git clone https://github.com/ElevenPaths/Eternalblue-Doublepulsar-Metasploit.git")
	    	elif opcion4 == "2":
		    cmd = os.system("git clone https://github.com/misterch0c/shadowbroker.git")
	    	elif opcion4 == "3":
		    cmd = os.system("git clone https://github.com/fuzzbunch/fuzzbunch.git")
	    	elif opcion4 == "4":
		    cmd = os.system("git clone https://github.com/nccgroup/Winpayloads.git")
	    	elif opcion4 == "5":
		    cmd = os.system("git clone https://github.com/Screetsec/TheFatRat.git")
	    	elif opcion4 == "6":
		    cmd = os.system("git clone https://github.com/nathanlopez/Stitch.git")
	    	elif opcion4 == "7":
		    cmd = os.system("git clone https://github.com/Cn33liz/p0wnedShell.git")
	    	elif opcion4 == "8":
		    cmd = os.system("git clone https://github.com/adamcaudill/EquationGroupLeak.git")      
	    	elif opcion4 == "9":
		    cmd = os.system("git clone https://github.com/screetsec/brutal.git")
	    	elif opcion4 == "10":
		    cmd = os.system("git clone https://github.com/Kkevsterrr/backdoorme.git")
	    	elif opcion4 == "11":
		    cmd = os.system("git clone https://github.com/dana-at-cp/backdoor-apk.git")      
	    	elif opcion4 == "12":
		    cmd = os.system("git clone https://github.com/D4Vinci/Dr0p1t-Framework.git")
	    	elif opcion4 == "13":
		    cmd = os.system("git clone https://github.com/IMcPwn/browser-backdoor.git")
	    	elif opcion4 == "14":
		    cmd = os.system("git clone https://github.com/Hadi999/NXcrypt.git")      
	    	elif opcion4 == "15":
		    cmd = os.system("git clone https://github.com/epinna/weevely3.git")
	    	elif opcion4 == "16":
		    cmd = os.system("git clone https://github.com/roissy/l0l.git")      
	    	elif opcion4 == "17":
		    cmd = os.system("git clone https://github.com/ChaitanyaHaritash/kimi.git")
	    	elif opcion4 == "18":
		    cmd = os.system("git clone https://github.com/ChaitanyaHaritash/venom.git")      
	    	elif opcion4 == "19":
		    cmd = os.system("git clone https://github.com/suraj-root/nWatch.git")
	    	elif opcion4 == "00":
		    main()

	    	else:
		    print("[!] Invalid Command")
    
    except Exception as e:
        print("[!] Something went Wrong Please Try again.")


banner()
main()
