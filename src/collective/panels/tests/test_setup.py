# -*- coding: utf-8 -*-

"""
This is an integration "unit" test.
"""

import unittest

from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from collective.panels.config import PROJECTNAME, DEPENDENCIES
from collective.panels.testing import INTEGRATION_TESTING

class InstallTestCase(unittest.TestCase):
    """
    The class that tests the installation of a particular product.
    """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = api.portal.get_tool(name='portal_quickinstaller')

    def test_installed(self):
        """
        This method test the default GenericSetup profile of this package.
        """
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        """
        This method test that dependencies products are installed of this package.
        """
        expected = set(DEPENDENCIES)
        installed = self.qi.listInstalledProducts(showHidden=True)
        installed = set([product['id'] for product in installed])
        result = sorted(expected - installed)

        self.assertTrue(
            result,
            "These dependencies are not installed: " + ", ".join(result)
        )

#class UninstallTestCase(unittest.TestCase):

#    layer = INTEGRATION_TESTING

#    def setUp(self):
#        self.portal = self.layer['portal']
#        setRoles(self.portal, TEST_USER_ID, ['Manager'])
#        self.qi = getattr(self.portal, 'portal_quickinstaller')
#        self.qi.uninstallProducts(products=[PROJECTNAME])

#    def test_uninstalled(self):
#        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

