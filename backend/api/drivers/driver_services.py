from core.mongo import MongoConnection

class DriverService:
    def __init__(self):
        self.db = MongoConnection.get_database()
        self.drivers_collection = self.db['users']

    def get_all_drivers(self, query_params):
        query_filter =  {}

        if 'isActive' in query_params:
            query_filter['isActive'] = query_params['isActive']
        
        if 'licenseType' in query_params:
            query_filter['licenseType'] = query_params['licenseType']
    
        return self.drivers_collection.find(query_filter)