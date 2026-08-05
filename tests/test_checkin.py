import os
import unittest
from unittest import mock

import checkin


class FakeClient:
    def __init__(self, results):
        self.results = iter(results)
        self.calls = 0

    def checkin(self):
        self.calls += 1
        return next(self.results)


class CheckinResultTests(unittest.TestCase):
    def test_current_observation_message_is_normal(self):
        result = {
            'code': 1,
            'message': "Today's observation logged. Return tomorrow for more points.",
        }
        self.assertTrue(checkin.is_normal_checkin_result(result))

    def test_historic_success_message_is_normal(self):
        self.assertTrue(
            checkin.is_normal_checkin_result({'code': 0, 'message': 'Checkin! Got 15 Points'})
        )

    def test_unknown_error_is_failure(self):
        self.assertFalse(checkin.is_normal_checkin_result({'code': 2, 'message': 'Cookie expired'}))

    @mock.patch('checkin.time.sleep')
    def test_retry_stops_after_success(self, sleep):
        client = FakeClient([
            None,
            {'code': 0, 'message': 'Checkin! Got 15 Points'},
        ])

        result, success = checkin.checkin_with_retry(client, attempts=3, delay_seconds=1)

        self.assertTrue(success)
        self.assertEqual(result['code'], 0)
        self.assertEqual(client.calls, 2)
        sleep.assert_called_once_with(1)


class CookieTests(unittest.TestCase):
    def test_json_token_uses_real_cookie_name(self):
        self.assertEqual(checkin.extract_cookie('{"token":"abc"}'), 'koa:sess=abc')

    def test_missing_configuration_returns_no_accounts(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(checkin.get_cookies(), [])


if __name__ == '__main__':
    unittest.main()
