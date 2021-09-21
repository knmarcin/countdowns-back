from rest_framework.test import APITestCase
from api.models import Countdown


class ApiReponseTests(APITestCase):
    def test_get_response_204(self):
        response = self.client.get('/countdowns/')
        self.assertEqual(response.status_code, 204)

    def test_get_response_200(self):
        Countdown.objects.create(title="New Year!", date="2021-12-24")
        response = self.client.get('/countdowns/')
        self.assertEqual(response.status_code, 200)

    def test_get_response_detail_view_204(self):
        response = self.client.get('/countdowns/1')
        self.assertEqual(response.status_code, 404)

    def test_get_response_detail_view_404(self):
        Countdown.objects.create(title="New Year!", date="2021-12-24")
        response = self.client.get('/countdowns/1')
        self.assertEqual(response.status_code, 200)

    def test_post_response_200(self):
        response = self.client.post(
            '/countdowns/',
            {
                "title": "x-mas",
                "date": "2021-12-24"
            }
        )
        self.assertEqual(response.status_code, 201)


    def test_post_response_detail_view_200(self):
        response = self.client.post(
            '/countdowns/1',
            {
                "title": "x-mas",
                "date": "2021-12-24"
            }
        )
        self.assertEqual(response.status_code, 201)


    def test_delete_object(self):
        Countdown.objects.create(title="New Year!", date="2021-12-24")
        response = self.client.delete(
            "/countdowns/1",
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_notexisting_object(self):
        response = self.client.delete(
            "/countdowns/1",
        )
        self.assertEqual(response.status_code, 404)

    def test_put(self):
        Countdown.objects.create(title="New Year!", date="2021-12-24")
        response = self.client.put(
            "/countdowns/1",
            {
                "title":"Christmas",
                "date":"2021-12-31"
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_put_bad(self):
        Countdown.objects.create(title="New Year!", date="2021-12-24")
        response = self.client.put(
            "/countdowns/1",
            {
                "title": 1,
                "dater": "2021-12-31"
            }
        )
        self.assertEqual(response.status_code, 400)

    def test_put_good(self):
        Countdown.objects.create(title="New Year!", date="2021-12-24")
        response = self.client.put(
            "/countdowns/1",
            {
                "date": "2021-12-31"
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_put_empty(self):
        Countdown.objects.create(title="New Year!", date="2021-12-24")
        response = self.client.put(
            "/countdowns/1",
            {

            }
        )
        self.assertEqual(response.status_code, 400)

