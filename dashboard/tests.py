from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class DashboardViewTests(TestCase):
    def test_views(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('orderbook_bias'))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('trader_bias'))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('reddit_posts'))
        self.assertEqual(resp.status_code, 200)