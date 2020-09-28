from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestCWEModel:

    def test_cwe_in_db(self):
        cwe = mixer.blend('api_cheat_sheet.CWEModel', top_25=True)
        assert cwe.top_25 == True
        assert cwe.rank == "0"

        cwe = mixer.blend('api_cheat_sheet.CWEModel', rank=12)
        assert cwe.top_25 == False
        assert cwe.has_example == False
        assert cwe.has_tutorial == False
        assert cwe.has_attack == False
        assert cwe.rank == '12'


# testy z fixture
@pytest.fixture()
def cwe(request, db):
    return mixer.blend('api_cheat_sheet.CWEModel', attack_example=request.param)


@pytest.mark.parametrize('cwe', ["example attack description"], indirect=True)
def test_cwe_has_attack(cwe):
    assert cwe.has_attack == True


@pytest.mark.parametrize('cwe', [None], indirect=True)
def test_cwe_doesnt_have_attack(cwe):
    assert cwe.has_attack == False

