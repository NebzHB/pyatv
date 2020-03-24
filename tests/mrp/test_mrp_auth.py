"""Functional authentication tests with fake MRP Apple TV."""

from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

import pyatv
from pyatv import exceptions
from pyatv.const import Protocol
from pyatv.conf import MrpService, AppleTV
from pyatv.mrp.server_auth import PIN_CODE, CLIENT_IDENTIFIER, CLIENT_CREDENTIALS
from tests.fake_device import FakeAppleTV


class MrpAuthFunctionalTest(AioHTTPTestCase):
    def setUp(self):
        AioHTTPTestCase.setUp(self)

        self.service = MrpService(
            CLIENT_IDENTIFIER, self.fake_atv.get_port(Protocol.MRP)
        )
        self.conf = AppleTV("127.0.0.1", "Apple TV")
        self.conf.add_service(self.service)

    async def tearDownAsync(self):
        await self.handle.close()
        await super().tearDownAsync()

    async def get_application(self, loop=None):
        self.fake_atv = FakeAppleTV(self.loop)
        self.state, self.usecase = self.fake_atv.add_service(Protocol.MRP)
        return self.fake_atv.app

    @unittest_run_loop
    async def test_pairing_with_device(self):
        self.handle = await pyatv.pair(self.conf, Protocol.MRP, self.loop)

        self.assertTrue(self.handle.device_provides_pin)

        await self.handle.begin()
        self.handle.pin(PIN_CODE)

        await self.handle.finish()

        self.assertTrue(self.handle.has_paired)
        self.assertTrue(self.fake_atv.get_service(Protocol.MRP).has_paired)

    @unittest_run_loop
    async def test_pairing_with_bad_pin(self):
        self.handle = await pyatv.pair(self.conf, Protocol.MRP, self.loop)

        self.assertTrue(self.handle.device_provides_pin)

        await self.handle.begin()
        self.handle.pin(PIN_CODE + 1)

        with self.assertRaises(exceptions.PairingError):
            await self.handle.finish()

        self.assertFalse(self.handle.has_paired)
        self.assertFalse(self.fake_atv.get_service(Protocol.MRP).has_paired)

    @unittest_run_loop
    async def test_pairing_authentication(self):
        self.service.credentials = CLIENT_CREDENTIALS

        self.handle = await pyatv.connect(self.conf, self.loop)

        self.assertTrue(self.fake_atv.get_service(Protocol.MRP).has_authenticated)
