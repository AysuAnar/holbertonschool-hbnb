from Model.baseclass import BaseClass
from Persistence.data_manager import DataManager
from datetime import datetime

class City(BaseClass):
    
    def __init__(self, name, country_id, id=None, created_at=None, updated_at=None):
        self.id = id if id else super().__init__()
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
        
        self.name = name
        self.country_id = country_id

    @staticmethod
    def get_all_cities():
        data_manager = DataManager()
        cities_data = data_manager.get_all('City')
        return [City(**data) for data in cities_data]

    @staticmethod
    def get_city_by_id(city_id):
        data_manager = DataManager()
        city_data = data_manager.get(city_id, 'City')
        return City(**city_data) if city_data else None

    @staticmethod
    def country_id_check(country_id):
        if country_id.isnumeric():
            return True
        raise ValueError("Country ID must be numeric")
