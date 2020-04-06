# from store_app import app
#
#
# class Initialized:
#     def setup(self):
#         app.config['TESTING'] = True
#         with app.test_client() as client:
#             self.client = client
#
#
# class TestUsers:
#
#     def test_create_new(self):
#         resp = self.client.post(
#
#             '/users',
#             json=('name', 'John Doe')
#         )
#         assert resp.status_code == 200