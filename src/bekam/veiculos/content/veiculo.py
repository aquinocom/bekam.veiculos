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
from bekam.veiculos.content.interfaces import IVeiculo
from bekam.veiculos.config import PROJECTNAME
from bekam.veiculos import _

# Schema definition
schema = ATContentTypeSchema.copy() + atapi.Schema((
    atapi.StringField(
        name='tipo_veiculo',
        required=True,
        searchable=True,
        vocabulary=[
            ('carro', 'CARRO'),
            ('moto', 'MOTO')
        ],
        widget=atapi.SelectionWidget(
            label=_(u'label_tipo_veiculo', u'Tipo de veículo'),
            format='select',
        ),
    ),
    atapi.StringField(
        name='marca',
        required=True,
        searchable=True,
        vocabulary=['ACURA', 'AGRALE', 'ALFA ROMEO', 'AM GEN', 'ASIA MOTORS', 'ASTON MARTIN', 'AUDI', 'BABY', 'BMW', 'BRM', 'BUGRE', 'CADILLAC', 'CBT JIPE', 'CHANA', 'CHANGAN', 'CHERY', 'CHRYSLER', 'CITROËN', 'CROSS LANDER', 'DAEWOO', 'DAIHATSU', 'DODGE', 'EFFA', 'ENGESA', 'ENVEMO', 'FERRARI', 'FIAT', 'FIBRAVAN', 'FORD', 'FOTON', 'FYBER', 'GEELY', 'GM - CHEVROLET', 'GREAT WALL', 'GURGEL', 'HAFEI', 'HONDA', 'HYUNDAI', 'ISUZU', 'IVECO', 'JAC', 'JAGUAR', 'JEEP', 'JINBEI', 'JPX', 'KIA MOTORS', 'LADA', 'LAMBORGHINI', 'LAND ROVER', 'LEXUS', 'LIFAN', 'LOBINI', 'LOTUS', 'MAHINDRA', 'MASERATI', 'MATRA', 'MAZDA', 'MCLAREN', 'MERCEDES-BENZ', 'MERCURY', 'MG', 'MINI', 'MITSUBISHI', 'MIURA', 'NISSAN', 'PEUGEOT', 'PLYMOUTH', 'PONTIAC', 'PORSCHE', 'RAM', 'RELY', 'RENAULT', 'ROLLS-ROYCE', 'ROVER', 'SAAB', 'SATURN', 'SEAT', 'SHINERAY', 'SMART', 'SSANGYONG', 'SUBARU', 'SUZUKI', 'TAC', 'TOYOTA', 'TROLLER', 'VOLVO', 'VW - VOLKSWAGEN', 'WAKE', 'WALK'],
        widget=atapi.SelectionWidget(
            label=_(u'label_marca', u'Marca'),
            format='select',
        ),
    ),
    atapi.IntegerField(
        name="ano",
        validators=('isInt',),
        searchable=True,
        widget=atapi.IntegerWidget(
            label=_(u'label_ano', u'Ano'),
        ),
    ),
    atapi.IntegerField(
        name="modelo",
        validators=('isInt',),
        searchable=True,
        widget=atapi.IntegerWidget(
            label=_(u'label_modelo', u'Modelo'),
        ),
    ),
    atapi.StringField(
        name="cor",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label=_(u'label_cor', u'Cor'),
        )
    ),
    atapi.StringField(
        name="valor",
        required=True,
        searchable=True,
        default="R$ ",
        widget=atapi.StringWidget(
            label=_(u'label_valor', u'Valor'),
        )
    ),
    atapi.StringField(
        name="valor_promocional",
        required=False,
        searchable=True,
        default="R$ ",
        widget=atapi.StringWidget(
            label=_(u'label_valor_promocional', u'Valor promocional'),
        )
    ),
    atapi.TextField(
        name='descricao',
        required=False,
        searchable=True,
        storage=atapi.AnnotationStorage(migrate=True),
        validators=('isTidyHtmlWithCleanup',),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u'label_descricao', u'Descrição'),
            rows=20,
            allow_file_upload=False,
        ),
    ),
    ImageField(
        name='imagem_1',
        sizes={
            'large': (768, 768),
            'preview': (400, 400),
            'mini': (200, 200),
            'thumb': (128, 128),
            'tile': (64, 64),
            'icon': (32, 32),
            'listing': (16, 16),
        },
        required=True,
        widget=atapi.ImageWidget(
            label=_(u'label_imagem_1', u'Imagem'),
        ),
    ),
    ImageField(
        name='imagem_2',
        sizes={
            'large': (768, 768),
            'preview': (400, 400),
            'mini': (200, 200),
            'thumb': (128, 128),
            'tile': (64, 64),
            'icon': (32, 32),
            'listing': (16, 16),
        },
        required=False,
        widget=atapi.ImageWidget(
            label=_(u'label_imagem_2', u'Imagem'),
        ),
    ),
    ImageField(
        name='imagem_3',
        sizes={
            'large': (768, 768),
            'preview': (400, 400),
            'mini': (200, 200),
            'thumb': (128, 128),
            'tile': (64, 64),
            'icon': (32, 32),
            'listing': (16, 16),
        },
        required=False,
        widget=atapi.ImageWidget(
            label=_(u'label_imagem_3', u'Imagem'),
        ),
    ),
    ImageField(
        name='imagem_4',
        sizes={
            'large': (768, 768),
            'preview': (400, 400),
            'mini': (200, 200),
            'thumb': (128, 128),
            'tile': (64, 64),
            'icon': (32, 32),
            'listing': (16, 16),
        },
        required=False,
        widget=atapi.ImageWidget(
            label=_(u'label_imagem_4', u'Imagem'),
        ),
    ),
    ImageField(
        name='imagem_5',
        sizes={
            'large': (768, 768),
            'preview': (400, 400),
            'mini': (200, 200),
            'thumb': (128, 128),
            'tile': (64, 64),
            'icon': (32, 32),
            'listing': (16, 16),
        },
        required=False,
        widget=atapi.ImageWidget(
            label=_(u'label_imagem_5', u'Imagem'),
        ),
    ),
    ImageField(
        name='imagem_6',
        sizes={
            'large': (768, 768),
            'preview': (400, 400),
            'mini': (200, 200),
            'thumb': (128, 128),
            'tile': (64, 64),
            'icon': (32, 32),
            'listing': (16, 16),
        },
        required=False,
        widget=atapi.ImageWidget(
            label=_(u'label_imagem_6', u'Imagem'),
        ),
    ),
    ImageField(
        name='imagem_7',
        sizes={
            'large': (768, 768),
            'preview': (400, 400),
            'mini': (200, 200),
            'thumb': (128, 128),
            'tile': (64, 64),
            'icon': (32, 32),
            'listing': (16, 16),
        },
        required=False,
        widget=atapi.ImageWidget(
            label=_(u'label_imagem_7', u'Imagem'),
        ),
    ),
    ImageField(
        name='imagem_8',
        sizes={
            'large': (768, 768),
            'preview': (400, 400),
            'mini': (200, 200),
            'thumb': (128, 128),
            'tile': (64, 64),
            'icon': (32, 32),
            'listing': (16, 16),
        },
        required=False,
        widget=atapi.ImageWidget(
            label=_(u'label_imagem_8', u'Imagem'),
        ),
    ),
    ImageField(
        name='imagem_9',
        sizes={
            'large': (768, 768),
            'preview': (400, 400),
            'mini': (200, 200),
            'thumb': (128, 128),
            'tile': (64, 64),
            'icon': (32, 32),
            'listing': (16, 16),
        },
        required=False,
        widget=atapi.ImageWidget(
            label=_(u'label_imagem_9', u'Imagem'),
        ),
    ),
    ImageField(
        name='imagem_10',
        sizes={
            'large': (768, 768),
            'preview': (400, 400),
            'mini': (200, 200),
            'thumb': (128, 128),
            'tile': (64, 64),
            'icon': (32, 32),
            'listing': (16, 16),
        },
        required=False,
        widget=atapi.ImageWidget(
            label=_(u'label_imagem_10', u'Imagem'),
        ),
    ),
))
# schema['title'].widget.label='Modelo'
# schema['title'].widget.label_msgid='label_modelo'
schema['description'].widget.visible['edit'] = 'invisible'
schemata.finalizeATCTSchema(schema)


class Veiculo(ATCTContent, HistoryAwareMixin):
    """
    """

    security = ClassSecurityInfo()
    implements(IVeiculo)

    meta_type = 'Veiculo'
    portal_type = 'Veiculo'

    _at_rename_after_creation = True

    schema = schema

    # Metodos
    def __bobo_traverse__(self, REQUEST, name):
        """Transparent access to image scales
        """
        list_field_image = ['imagem_1',
                            'imagem_2',
                            'imagem_3',
                            'imagem_4',
                            'imagem_5',
                            'imagem_6',
                            'imagem_7',
                            'imagem_8',
                            'imagem_9',
                            'imagem_10',]
        for field_image in list_field_image:
            if name.startswith(field_image):
                field = self.getField(field_image)
                image = None
                if name == field_image:
                    image = field.getScale(self)
                else:
                    name_scale = field_image + '_'
                    scalename = name[len(name_scale):]
                    if scalename in field.getAvailableSizes(self):
                        image = field.getScale(self, scale=scalename)
                if image is not None and not isinstance(image, basestring):
                    # image might be None or '' for empty images
                    return image

        return ATCTContent.__bobo_traverse__(self, REQUEST, name)

atapi.registerType(Veiculo, PROJECTNAME)
