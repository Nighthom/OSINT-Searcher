class QueryParser:
    def __init__(self):
        '''
        pase_option's key is shodan's query filter, 
        value is the censys's query filter.
        This paser work to replace Shodan's filter to 
        Censys's filter.
        ''' 
        self.parse_options = {
            "-ip": "not ip", 
            "-port": "not port",
            "ip": "ip", 
            "port": "services.port", 
        } 


    def to_censys_query(self, query):
        shodan_query_list = query.split(" ")

        query_data = shodan_query_list[0]
        shodan_query_list.remove(query_data)
        if shodan_query_list == []:
            return query

        censys_options = []
        for option in shodan_query_list:
            censys_options.append(self.to_censys_option(option))

        censys_query = query_data

        for option in censys_options:
            censys_query += " and "
            censys_query += option

        return censys_query

    def to_censys_option(self, option):
        for shodan_opt, censys_opt in self.parse_options.items():
            option = option.replace(shodan_opt, censys_opt)

        return option
            
