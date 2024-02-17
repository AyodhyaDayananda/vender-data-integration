from zoom import main
import json

class ServiceProvide:
    def get_params(self, params):
        self._params = params
        dictionary = json.loads(self._params)
        print('**********************')
        print(dictionary)
        print('**********************')
        service = main.DataProcessor()
        service.get_service(dictionary)
