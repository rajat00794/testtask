import re
from infrastructure.server.app.application import init_app

import json


def test_user_create():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    flask_app = init_app("infrastructure.server.app.config.Config")
    file = open("fixture/fixture1.json", "rb")
    file = file.read()
    file = json.loads(file)
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.post(
            "/api/user/", data=json.dumps(file), content_type="application/json"
        )
        assert response.status_code == 201


def test_user_get():
    flask_app = init_app("infrastructure.server.app.config.Config")
    with flask_app.test_client() as test_client:
        login = test_client.post(
            f"/api/user/login/",
            content_type="application/json",
            data=json.dumps(dict(email="man1@d.com", password="Rajat322")),
        )
        token = json.loads(login.data)["data"]["access_token"]
        response = test_client.get(
            "/api/user/getall/",
            headers=dict(
                content_type="application/json", Authorization="Bearer {}".format(token)
            ),
        )
        assert response.status_code == 200
        objid = json.loads(response.data)["data"][0]["id"]
        response = test_client.get(
            f"/api/user/get/{objid}", content_type="application/json"
        )
        assert response.status_code == 308
