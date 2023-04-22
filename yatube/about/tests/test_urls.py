from django.test import TestCase, Client


class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_author_url_exists_at_desired_location(self):
        """Проверка доступности адреса /about/author/."""
        response = self.guest_client.get('author/')
        self.assertEqual(response.status_code, 200)

    def test_author_url_uses_correct_template(self):
        """Проверка шаблона для адреса /about/author/."""     
        response = self.guest_client.get('author/')
        self.assertTemplateUsed(response, 'author.html')

    def test_tech_url_exists_at_desired_location(self):
        """Проверка доступности адреса /about/tech/."""
        response = self.guest_client.get('tech/')
        self.assertEqual(response.status_code, 200)

    def test_tech_url_uses_correct_template(self):
        """Проверка шаблона для адреса /about/tech/."""     
        response = self.guest_client.get('tech/')
        self.assertTemplateUsed(response, 'tech.html')
