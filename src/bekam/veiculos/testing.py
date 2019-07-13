# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import bekam.veiculos


class BekamVeiculosLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=bekam.veiculos)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'bekam.veiculos:default')


BEKAM_VEICULOS_FIXTURE = BekamVeiculosLayer()


BEKAM_VEICULOS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BEKAM_VEICULOS_FIXTURE,),
    name='BekamVeiculosLayer:IntegrationTesting',
)


BEKAM_VEICULOS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BEKAM_VEICULOS_FIXTURE,),
    name='BekamVeiculosLayer:FunctionalTesting',
)


BEKAM_VEICULOS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        BEKAM_VEICULOS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='BekamVeiculosLayer:AcceptanceTesting',
)
