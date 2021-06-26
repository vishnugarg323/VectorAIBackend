import json

import pytest

from app.main import app
from app.api import crud


def test_create_card(test_app, monkeypatch):
    test_request_payload = {"title": "something", "type": "something else"}
    test_response_payload = {"id": 1, "title": "something", "type": "something else"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/cards/", data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_card_invalid_json(test_app):
    response = test_app.post("/cards/", data=json.dumps({"title": "something"}))
    assert response.status_code == 422