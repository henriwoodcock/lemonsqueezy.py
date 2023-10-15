class MockResponse:
    def __init__(self, json_data, status_code, reason):
        self.json_data = json_data
        self.status_code = status_code
        self.reason = reason

    def json(self):
        return self.json_data
