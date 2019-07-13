# -*- coding: utf-8 -*-

# libs
import logging
import re

#zope
from zope.site.hooks import getSite

# plone
from plone.app.layout.viewlets.common import ViewletBase
from plone import api

# bekam
from bekam.veiculos.content.interfaces import IDestaque


logger = logging.getLogger('BEKAM VIEWLETS')


class RedesSociaisViewlet(ViewletBase):
    """Viewlet redes sociais
    """

    def __init__(self, context, request, view, manager=None):
        super(ViewletBase, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def get_redes_sociais(self):
        """
        """
        redes_sociais = dict()
        try:
            path = '/'.join(getSite().getPhysicalPath()) + '/administracao/redes-sociais'
            item = api.content.get(path=path)
            if item:
                redes_sociais['facebook'] = item.url_facebook.strip()
                redes_sociais['twitter'] = item.url_twitter.strip()
                redes_sociais['instagram'] = item.url_instagram.strip()
        except Exception as e:
            logger.error('RedesSociaisViewlet (get_redes_sociais): ' + str(e))
        return redes_sociais


class RecentesViewlet(ViewletBase):
    """Viewlet recentes
    """

    def __init__(self, context, request, view, manager=None):
        super(ViewletBase, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def get_veiculos(self):
        """
        """
        veiculos = []
        try:
            limit=4
            items = api.content.find(
                portal_type='Veiculo',
                sort_on='effective',
                sort_order='reverse',
                review_state='published',
                sort_limit=limit,
            )[:limit]
            for item in items:
                veiculos.append(dict(title=item.Title,
                                     valor=item.valor,
                                     ano=item.ano,
                                     modelo=item.modelo,
                                     valor_promocional=item.valor_promocional,
                                     url=item.getURL))
        except Exception as e:
            logger.error('RecentesViewlet (get_veiculos): ' + str(e))
        return veiculos

    def is_valor_promocional(self, valor_promocional):
        """
        """
        try:
            if valor_promocional:
                if len(valor_promocional) > 5:
                    return True
        except Exception as e:
            logger.error('RecentesViewlet (is_valor_promocional): ' + str(e))


class DestaquesViewlet(ViewletBase):
    """Viewlet destaques
    """

    def __init__(self, context, request, view, manager=None):
        super(ViewletBase, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def get_destaques(self):
        """
        """
        list_destaques = []
        try:
            path = '/'.join(getSite().getPhysicalPath()) + '/administracao/destaques'
            limit = 3
            items = api.content.find(
                object_provides=IDestaque.__identifier__,
                path={'query': path, 'depth': 1},
                sort_on='getObjPositionInParent',
                review_state='published',
                sort_limit=limit,
            )[:limit]
            for item in items:
                obj = item.getObject()
                dic = dict(title=obj.Title(),
                           text=obj.getText())
                if obj.getImage().filename:
                    image_tag = obj.getImage().restrictedTraverse('@@images').tag(fieldname='image', scale='preview')
                    dic['image_url'] = re.findall(r'src=[\'"]?([^\'" >]+)', image_tag)[0]
                else:
                    dic['image_url'] = None
                list_destaques.append(dic)
        except Exception as e:
            logger.error('DestaquesViewlet (get_destaques): ' + str(e))
        return list_destaques
