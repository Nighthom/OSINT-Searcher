class SearchEngine:
    def __init__(self, api):
        self.api = api
        self.result = ""
        self.query = input("[*] What query do you want to search?: ")
        self.count = input("[*] What count of result do you want to search?: ")

        if self.count == "":
            self.count = None
        else:
            self.count = int(self.count)
    def run(self):
        self.shodan_run()
        self.censys_run()
            

    def shodan_run(self):
        api = self.api.shodanapi
        
        filter_list = ["hostnames", "ip_str", "port", "product"]

        print("[~] Searching...")

        results = api.search(self.query, limit=self.count)
        self.shodan_print_result(results, filter_list)
            
        
    def shodan_print_result(self, results, filter_list):
        self.print_result("===============================")
        self.print_result("[+] Shodan search results")
        self.print_result(f"[+] query: {self.query}")
        self.print_result("===============================")
        for result in results['matches']:
            for filter in filter_list:
                try:
                    self.print_result(f"{filter.upper()}: {result[filter]}")
                except KeyError:
                    pass
            self.print_result("----------------------------")
    
        
    def censys_run(self):
        api = self.api.censysapi
        PER_PAGE = 1
        
        if self.count == None:
            results = api.search(self.query, per_page=PER_PAGE)
        else:
            results = api.search(self.query, per_page=PER_PAGE, pages=self.count)
        
        self.censys_print_result(results)


    def censys_print_result(self, results):
        self.print_result("===============================")
        self.print_result("[+] Censys search results")
        self.print_result(f"[+] query: {self.query}")
        self.print_result("===============================")
        for page in results:
            for data in page:
                ports = []
                service_names = []
                for service in data['services']:
                    ports.append(service['port'])
                    service_names.append(service['service_name'])

                self.print_result(f"IP: {data['ip']}")
                self.print_result(f"Ports: {ports}")
                self.print_result(f"Service Name: {service_names}")
                self.print_result("----------------------------")

            
    def print_result(self, text):
        print(text)
        self.result += text
        self.result += "\n"
        
