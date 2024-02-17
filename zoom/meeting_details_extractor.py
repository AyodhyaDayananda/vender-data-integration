import zoom
import logging

class ExtractMeetingDetails:
    def get_service(self, params):
        logging.basicConfig(level=logging.INFO)
        service = zoom.ZoomExtractor()
        if params.get("MEETING_ID"):
            payload = service._get_meeting_details_by_meeting_id(params.get("MEETING_ID"))
        else:
            payload = service.get_meeting_details(params.get("USER_ID"))
        logging.info(f'full payload : {payload}')
        print(f'meeting payload : {payload}')
        #self.flatten_payload(payload)

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
    data_processor = ExtractMeetingDetails()
    data_processor.get_service()
