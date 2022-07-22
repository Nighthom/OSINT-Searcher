import shodan
from censys.search import CensysHosts
from os import system

class APICertificator:
    def __init__(self): 
        self.shodan_key = ""

        self.read_shodan_keyfile()
        
        self.shodanapi = shodan.Shodan(self.shodan_key)
        self.censysapi = CensysHosts()

        while self.check_censys_isvalid() == False:
            self.censys_certification()

    
    def read_shodan_keyfile(self):
        try:
            print("[~] Read Shodan API Key file...")
            with open("data/shodan_apikey.dat", "r") as keyfile:
                print("[*] Read Success!") 
                self.shodan_key = keyfile.read()
                if self.check_shodan_key() == False:
                    self.input_shodan_key()    
        except FileNotFoundError:
            print("[!] Key is not founded.")
            self.input_shodan_key()


    def input_shodan_key(self):
        is_valid = False
        while is_valid == False:
            self.shodan_key = input("[*] Input your Shodan API Key: ")
            is_valid = self.check_shodan_key()
        self.save_shodan_key()


    def save_shodan_key(self):
        print("[~] Save Shodan API Key file...")
        with open("data/shodan_apikey.dat", "w") as keyfile:
            keyfile.write(self.shodan_key)
            print("[~] Save Success!")


    def check_shodan_key(self):
        api = shodan.Shodan(self.shodan_key)
        check_text = "b00m"
        try:
            print("[~] Check your Shodan API key...")
            api.search(check_text)
            print("[~] Your key is valid!")
            return True
        except:
            print("[!] Shodan key is not available.")
            return False

    
    def check_censys_isvalid(self):
        check_text = "b00m"
       
        try:
            print("[~] Check your Censys Certification...")
            self.censysapi.search(check_text)
            print("[~] Your Censys Certification is valid.")
            return True
        except:
            print("[!] Censys Certification is not available.")
            return False


    def censys_certification(self):
        system("censys config")
        