class DriverService:
    def __init__(self):
        self.drivers_collection = self.db['users']

    def get_all_drivers(self, query_params):
        query_filter =  {}

        if 'isActive' in query_params:
            query_filter['isActive'] = query_params['isActive']
        
        if 'licenseType' in query_params:
            query_filter['licenseType'] = query_params['licenseType']
    
        return self.drivers_collection.find(query_filter)
    
    def create_driver(self, driver_data):
        """Create a new driver."""
        driver_data['isActive'] = True
        return self.drivers_collection.insert_one(driver_data)