# -*- coding: utf-8 -*-

# libs

# zope
from zope.interface import implements

# Security
from AccessControl import ClassSecurityInfo

# plone
from plone.app.blob.field import ImageField

# Products
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin
from Products.CMFCore.permissions import View

# bekam
from bekam.veiculos.content.interfaces import IDestaque
from bekam.veiculos.config import PROJECTNAME
from bekam.veiculos import _
# Schema definition
schema = ATContentTypeSchema.copy() + atapi.Schema((
    atapi.TextField(
        name='text',
        required=False,
        searchable=False,
        storage=atapi.AnnotationStorage(migrate=True),
        validators=('isTidyHtmlWithCleanup',),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u'label_text', u'Texto'),
            rows=20,
            allow_file_upload=False,
        ),
    ),
    ImageField(
        name='image',
        sizes={'large': (768, 768),
               'preview': (400, 400),
               'mini': (200, 200),
               'thumb': (128, 128),
               'tile': (64, 64),
               'icon': (32, 32),
               'listing': (16, 16),
               },
        required=False,
        widget=atapi.ImageWidget(
            label=_(u'label_image', u'Imagem'),
        ),
    ),
))
schema['description'].widget.visible['edit'] = 'invisible'
schemata.finalizeATCTSchema(schema)


class Destaque(ATCTContent, HistoryAwareMixin):
    """
    """

    security = ClassSecurityInfo()
    implements(IDestaque)

    meta_type = 'Destaque'
    portal_type = 'Destaque'

    _at_rename_after_creation = True

    schema = schema

    # Metodos
    security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        # Generate image tag using the api of the ImageField.
        if 'title' not in kwargs:
            kwargs['title'] = self.getImageCaption()
        return self.getField('image').tag(self, **kwargs)

    def __bobo_traverse__(self, REQUEST, name):
        """Transparent access to image scales
        """
        if name.startswith('image'):
            field = self.getField('image')
            image = None
            if name == 'image':
                image = field.getScale(self)
            else:
                scalename = name[len('image_'):]
                if scalename in field.getAvailableSizes(self):
                    image = field.getScale(self, scale=scalename)
            if image is not None and not isinstance(image, basestring):
                # image might be None or '' for empty images
                return image

        return ATCTContent.__bobo_traverse__(self, REQUEST, name)


atapi.registerType(Destaque, PROJECTNAME)
