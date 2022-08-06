import unittest, time, os

from network import Network
from socket import socket
from threading import Thread
from server_tester import *
import server_tester

class Tests(unittest.TestCase):

    def test_a_scenario(self):

        server = Server(1, 5555)

        Thread(target=server.start).start()

        network = Network("127.0.0.1", 5555)

        network.start()

        try:
            server.s.close()
        except:
            pass

        self.assertEqual(server_tester.connected, 1, '\nسرور متصل نشده است.')

        with open('config.json', 'r') as f:
            loaded_data = json.load(f)
            self.assertEqual(loaded_data, config_sent[0], '\nداده‌ها را به درستی از فایل config.json استخراج نمی‌کنید.')

        Thread(target=server.pass_cycle).start()

        network.send_data(['1111'])

        self.assertEqual(network.get_data(), server_tester.data_sent, '\nتابع get_data را به درستی تکمیل نکرده‌اید.')

        self.assertEqual(server_tester.send_data_is_ok, True, '\nتابع send_data را به درستی تکمیل نکرده‌اید.')

        server.finish()