from graphdb_test.models import User


def mock_user_get(**kwargs):
    def get():
        return [
            {'ids': [2, 3, 4], 'total': 3,
             'user': {
                'id': 1,
                 'username': 'leroy'}
             }]
    return get()


class TestUserView():
    def test_get(self, mocker):
        mocker.patch.object(
            User, 'get', auto_spec=True, side_effect=mock_user_get)
        response = User(id=1).get()[0]

        assert response['user']['id'] == 1
        assert response['total'] == 3


class TestConnectionView():
    def test_get(self, mocker):
        mocker.patch.object(
            User, 'get', auto_spec=True, side_effect=mock_user_get)
        response = User(id=1).connections_between(2)

        assert response is True

    def test_when_response_is_false(self, mocker):
        mocker.patch.object(
            User, 'get', auto_spec=True, side_effect=mock_user_get)
        response = User(id=1).connections_between(22)

        assert response is False
