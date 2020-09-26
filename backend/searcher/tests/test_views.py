from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
import pytest
from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase

from searcher.views import login_required_view


@pytest.mark.django_db
class TestViews(TestCase):
    """
    pytest --cov
    pytest --cov=. #można sprawdzic sciezke ile w danym miejscu pokryte testami
    """

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        # mixer.blend('moje_api.NazwaModelu') # #jakby testowac z bazy
        cls.factory = RequestFactory()

    def test_login_required_view_authenticated(self):
        # mixer.blend('moje_api.NazwaModelu') # #jakby testowac z bazy
        path = reverse('login_required_view', kwargs={"cve_code": "CVE-2010-3333"})
        request = self.factory.get(path)
        request.user = mixer.blend(User)

        response = login_required_view(request, cve_code="CVE-2010-3333")
        assert response.status_code == 200

    def test_login_required_view_unauthenticated(self):
        """
        Sprawdza zachowanie dla niezalogowanego użytkownika
        """
        # mixer.blend('moje_api.NazwaModelu') # #jakby testowac z bazy
        path = reverse('login_required_view', kwargs={"cve_code": "CVE-2010-3333"})
        request = self.factory.get(path)
        request.user = AnonymousUser()

        response = login_required_view(request, cve_code="CVE-2010-3333")
        assert response.status_code == 302
        # testowanie przekierowania żeby user się zalogował (sprawdza url który pokazuje się niezalogowanemu uzytkownikowi
        # assert 'accounts/login' in response.url