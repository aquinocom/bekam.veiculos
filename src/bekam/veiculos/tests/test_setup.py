# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from bekam.veiculos.testing import BEKAM_VEICULOS_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that bekam.veiculos is properly installed."""

    layer = BEKAM_VEICULOS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if bekam.veiculos is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'bekam.veiculos'))

    def test_browserlayer(self):
        """Test that IBekamVeiculosLayer is registered."""
        from bekam.veiculos.interfaces import (
            IBekamVeiculosLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IBekamVeiculosLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = BEKAM_VEICULOS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['bekam.veiculos'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if bekam.veiculos is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'bekam.veiculos'))

    def test_browserlayer_removed(self):
        """Test that IBekamVeiculosLayer is removed."""
        from bekam.veiculos.interfaces import \
            IBekamVeiculosLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IBekamVeiculosLayer,
            utils.registered_layers())
