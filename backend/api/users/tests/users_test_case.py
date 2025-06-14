from mongoengine import connection
from core.utils.mongo_test_case import MongoTestCase
from users.auth_services import get_hash_password

class UsersTestCase(MongoTestCase):
    def setUp(self):
        self.db = connection.get_db()

        # self.mock_user_data = {
        #     '_id': '507f1f77bcf86cd799439011',
        #     'email': 'test@example.com',
        #     'name': 'Test User',
        #     'role': 'user'
        # }
        # self.test_user = SimpleUser(self.mock_user_data)
        # self.client.force_authenticate(user=self.test_user)

        cpf = '18092754314'
        birth_year = '1996'
        password = f"{cpf[-2:]}{birth_year}"
        self.valid_user_data = {
            'cpf': cpf,
            'password': password,
            'name': 'Test User',
            'type': 'user'
        }
        self.db.users.insert_one({**self.valid_user_data, password: get_hash_password(password)})
        
        super().setUp()

    def tearDown(self) -> None:
        self.db.users.drop()
        super().tearDown()
