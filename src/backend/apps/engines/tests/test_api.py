from django.urls import reverse
import json
import pytest


def test_get_engines_index_text_should_succeed(client) -> None:
    index_url = reverse('engines-index')
    response = client.get(index_url)
    assert response.status_code == 200
    assert json.loads(response.content) == {"status": "success", "info": "ENGINES index."}
