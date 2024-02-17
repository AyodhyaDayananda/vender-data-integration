from zoom import ExtractMeetingDetails, ExtractUserDetails


class DataProcessor:
    def get_service(self, params):
        meeting_data_processor = ExtractMeetingDetails()
        user_data_processor = ExtractUserDetails()
        user_data_processor.get_service(params)
        meeting_data_processor.get_service(params)


if __name__ == "__main__":
    data_processor = DataProcessor()
    x = {"USER_ID": "I9uGQ9IpRoSgLRkisQjG5A", "MEETING_ID": "75884989787"}
    data_processor.get_service(x)
