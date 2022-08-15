import unittest
import unittest.mock
import user_management


def get_mock_db_cursor(fetchone_return_value=None, fetchall_return_value=None):
    return unittest.mock.Mock(
        __enter__=lambda _: unittest.mock.Mock(
            execute=lambda query, params: None,
            fetchone=lambda: fetchone_return_value,
            fetchall=lambda: fetchall_return_value,
        ),
        __exit__=lambda *args: None,
    )


def get_mock_db_connection(mock_db_cursor):
    return unittest.mock.Mock(
        __enter__=lambda _: unittest.mock.Mock(
            cursor=lambda **kwargs: mock_db_cursor,
        ),
        __exit__=lambda *args: None,
    )


class TestUserManagement(unittest.TestCase):

    def test_check_email_not_in_use_with_available_email(self):
        test_email = 'a@b.com'
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=None)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = user_management.check_email_not_in_use(test_email)
            self.assertTrue(result)

    def test_check_email_not_in_use_with_unavailable_email(self):
        test_email = 'a@b.com'
        mock_user_id = 1
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=mock_user_id)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = user_management.check_email_not_in_use(test_email)
            self.assertFalse(result)

    def test_get_user_info(self):
        test_user_id = 2
        mock_user = {'full_name': 'Nazo', 'email_address': 'nazo@gmail.com', 'height': 170, 'weight': 65}
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=mock_user)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = user_management.get_user_info(test_user_id)
            self.assertEqual(result, mock_user)

    def test_check_login_details_with_valid_login(self):
        test_email = 'olivia@gmail.com'
        test_password = 'hahahaha'
        mock_user_id = 3
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value={'user_id': mock_user_id})
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = user_management.check_login_details(test_email, test_password)
            self.assertEqual(result, mock_user_id)

    def test_check_login_details_with_invalid_login(self):
        test_email = 'somerando@gmail.com'
        test_password = 'wrong'
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=None)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = user_management.check_login_details(test_email, test_password)
            self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
