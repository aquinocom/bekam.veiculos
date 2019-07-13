# -*- coding: utf-8 -*-

# zope
from zope.component import getUtility

# plone
from plone.registry.interfaces import IRegistry
from plone.app.theming.interfaces import IThemeSettings


def get_theme_prefix(self):
    """Retorna o prefixo do caminho absoluto (plone.app.theming)
    """
    settings = getUtility(IRegistry).forInterface(IThemeSettings, False)
    if not settings.absolutePrefix:
        return ''
    else:
        return settings.absolutePrefix
