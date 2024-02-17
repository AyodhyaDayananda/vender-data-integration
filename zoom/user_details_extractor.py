import zoom
import logging

class ExtractUserDetails:
    def get_service(self, params):
        logging.basicConfig(level=logging.INFO)
        service = zoom.ZoomExtractor()
        payload = service._get_user_details_seervice(params.get("USER_ID"))
        # logging.info(f'full payload : {payload}')
        print(f'user payload : {payload}')
        self.flatten_payload(payload)

    @staticmethod
    def flatten_payload(payload_response):
        payload = {
            'USER_ID' : payload_response['id'],
            'FIRST_NAME' : payload_response['first_name'],
            'LAST_NAME' : payload_response['last_name'],
            'DISPLAY_NAME' : payload_response['display_name'],
            'EMAIL' : payload_response['email']
        }
        logging.info(f'flatten payload : {payload}')


####commenting this if you want to test this mannualy uncomment this
if __name__ == "__main__":
    data_processor = ExtractUserDetails()
    data_processor.get_service()
