from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestCWEModel:

    def test_cwe_in_db(self):
        cwe = mixer.blend('knowledge_base.CWEModel', top_25=True)
        assert cwe.top_25 == True
        assert cwe.rank == "0"

        cwe = mixer.blend('knowledge_base.CWEModel', rank=12)
        assert cwe.top_25 == False
        assert cwe.has_example == False
        assert cwe.has_tutorial == False
        assert cwe.has_attack == False
        assert cwe.rank == 12
