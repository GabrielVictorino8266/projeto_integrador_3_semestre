from mongoengine import connection
from core.utils.mongo_test_case import MongoTestCase

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

        self.valid_user_data = {
            'cpf': '18092754314',
            'password': '1996180',
            'name': 'Test User',
            'type': 'user'
        }
        self.db.users.insert_one(self.valid_user_data)
        
        super().setUp()

    def tearDown(self) -> None:
        self.db.users.drop()
        super().tearDown()
