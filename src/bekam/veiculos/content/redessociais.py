# -*- coding: utf-8 -*-

# libs

# zope
from zope.interface import implements


# Security
from AccessControl import ClassSecurityInfo

# plone


# Products
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin

# bekam
from bekam.veiculos.content.interfaces import IRedesSociais
from bekam.veiculos.config import PROJECTNAME
from bekam.veiculos import _


# Schema definition
schema = ATContentTypeSchema.copy() + atapi.Schema((
    atapi.StringField(
        name="url_facebook",
        required=False,
        searchable=False,
        validators=('isURL',),
        widget=atapi.StringWidget(
            label=_(u'label_url_facebook', u'Facebook'),
            description=_(u'description_url_facebook', u'Informe a url do Facebook')
        )
    ),
    atapi.StringField(
        name="url_twitter",
        required=False,
        searchable=False,
        validators=('isURL',),
        widget=atapi.StringWidget(
            label=_(u'label_url_twitter', u'Twitter'),
            description=_(u'description_url_twitter', u'Informe a url do Twitter')
        )
    ),
    atapi.StringField(
        name="url_instagram",
        required=False,
        searchable=False,
        validators=('isURL',),
        widget=atapi.StringWidget(
            label=_(u'label_url_instagram', u'Instagram'),
            description=_(u'description_url_instagram', u'Informe a url do Instagram')
        )
    ),
))
schema['description'].widget.visible['edit'] = 'invisible'
schemata.finalizeATCTSchema(schema)


class RedesSociais(ATCTContent, HistoryAwareMixin):
    """Noticias
    """

    security = ClassSecurityInfo()
    implements(IRedesSociais)

    meta_type = 'RedesSociais'
    portal_type = 'RedesSociais'

    _at_rename_after_creation = True

    schema = schema

    # Metodos


atapi.registerType(RedesSociais, PROJECTNAME)
