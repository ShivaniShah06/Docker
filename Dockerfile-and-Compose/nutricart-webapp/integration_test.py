import unittest
from webapp import app
from fastapi.testclient import TestClient


class healthCheckTest(unittest.TestCase):
    def test(self):
        client = TestClient(app)
        response = client.get('/healthz')
        assert response.status_code == 200
        print(f"Received status code: {response.status_code} from /healthz endpoint.")
        print("========================= TEST PASSED! =========================")

if __name__ == '__main__':
    unittest.main()
