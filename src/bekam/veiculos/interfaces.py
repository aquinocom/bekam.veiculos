# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.viewlet.interfaces import IViewletManager


class IBekamVeiculosLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ITopoViewletManager(IViewletManager):
    """
    Marker interface for viewlets that can be displayed in my custom header
    viewlet manager
    """


class IPaginaInicialViewletManager(IViewletManager):
    """
    Marker interface for viewlets that can be displayed in my custom header
    viewlet manager
    """
