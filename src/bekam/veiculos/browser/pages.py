# -*- coding: utf-8 -*-

# libs
import re
import logging
# zope

# plone
from plone import api

# Products
from Products.Five.browser import BrowserView

# bekam


logger = logging.getLogger('BEKAM PAGES')


class BuscaView(BrowserView):
    """ busca
    """

    def __init__(self, context, request):
        """
        """
        self.context = context
        self.request = request
        if 'termo' in self.request.form:
            self.termo = request.form['termo']
        else:
            self.termo = None
        self.request.set('termo', self.termo)

    def get_veiculos(self):
        """
        """
        veiculos = []
        try:
            if self.termo and self.termo.strip() != '':
                items = api.content.find(
                    portal_type='Veiculo',
                    SearchableText=self.termo,
                    sort_on='effective',
                    sort_order='reverse',
                    review_state='published'
                )
                for item in items:
                    veiculos.append(dict(title=item.Title,
                                         valor=item.valor,
                                         ano=item.ano,
                                         modelo=item.modelo,
                                         valor_promocional=item.valor_promocional,
                                         url=item.getURL))
        except Exception as e:
            logger.error('BuscaView (get_veiculos): ' + str(e))
        return veiculos

    def is_valor_promocional(self, valor_promocional):
        """
        """
        try:
            if valor_promocional:
                if len(valor_promocional) > 5:
                    return True
        except Exception as e:
            logger.error('BuscaView (is_valor_promocional): ' + str(e))


class VeiculoView(BrowserView):
    """ Veículo view
    """

    def __init__(self, context, request):
        """
        """
        self.context = context
        self.request = request

    def is_valor_promocional(self):
        """
        """
        valor_promocional = self.context.getValor_promocional()
        if len(valor_promocional) > 5:
            return True

    def get_images(self):
        """
        """
        list_imagens = []
        if self.context.getImagem_1().filename:
            image_tag = self.context.getImagem_1().restrictedTraverse('@@images').\
                tag(fieldname='imagem_1', scale='preview')
            list_imagens.append(re.findall(r'src=[\'"]?([^\'" >]+)', image_tag)[0])
        if self.context.getImagem_2().filename:
            image_tag = self.context.getImagem_2().restrictedTraverse('@@images').\
                tag(fieldname='imagem_2', scale='preview')
            list_imagens.append(re.findall(r'src=[\'"]?([^\'" >]+)', image_tag)[0])
        if self.context.getImagem_3().filename:
            image_tag = self.context.getImagem_3().restrictedTraverse('@@images').\
                tag(fieldname='imagem_3', scale='preview')
            list_imagens.append(re.findall(r'src=[\'"]?([^\'" >]+)', image_tag)[0])
        if self.context.getImagem_4().filename:
            image_tag = self.context.getImagem_4().restrictedTraverse('@@images').\
                tag(fieldname='imagem_4', scale='preview')
            list_imagens.append(re.findall(r'src=[\'"]?([^\'" >]+)', image_tag)[0])
        if self.context.getImagem_5().filename:
            image_tag = self.context.getImagem_5().restrictedTraverse('@@images').\
                tag(fieldname='imagem_5', scale='preview')
            list_imagens.append(re.findall(r'src=[\'"]?([^\'" >]+)', image_tag)[0])
        if self.context.getImagem_6().filename:
            image_tag = self.context.getImagem_6().restrictedTraverse('@@images').\
                tag(fieldname='imagem_6', scale='preview')
            list_imagens.append(re.findall(r'src=[\'"]?([^\'" >]+)', image_tag)[0])
        if self.context.getImagem_7().filename:
            image_tag = self.context.getImagem_7().restrictedTraverse('@@images').\
                tag(fieldname='imagem_7', scale='preview')
            list_imagens.append(re.findall(r'src=[\'"]?([^\'" >]+)', image_tag)[0])
        if self.context.getImagem_8().filename:
            image_tag = self.context.getImagem_8().restrictedTraverse('@@images').\
                tag(fieldname='imagem_8', scale='preview')
            list_imagens.append(re.findall(r'src=[\'"]?([^\'" >]+)', image_tag)[0])
        if self.context.getImagem_9().filename:
            image_tag = self.context.getImagem_9().restrictedTraverse('@@images').\
                tag(fieldname='imagem_9', scale='preview')
            list_imagens.append(re.findall(r'src=[\'"]?([^\'" >]+)', image_tag)[0])
        if self.context.getImagem_10().filename:
            image_tag = self.context.getImagem_10().restrictedTraverse('@@images').\
                tag(fieldname='imagem_10', scale='preview')
            list_imagens.append(re.findall(r'src=[\'"]?([^\'" >]+)', image_tag)[0])
        return list_imagens


class ListaVeiculosView(BrowserView):
    """ Lista veículos view
    """

    def __init__(self, context, request):
        """
        """
        self.context = context
        self.request = request

    def get_veiculos(self):
        """
        """
        veiculos = []
        try:
            items = api.content.find(
                portal_type='Veiculo',
                sort_on='effective',
                sort_order='reverse',
                review_state='published'
            )
            for item in items:
                veiculos.append(dict(title=item.Title,
                                     valor=item.valor,
                                     ano=item.ano,
                                     modelo=item.modelo,
                                     valor_promocional=item.valor_promocional,
                                     url=item.getURL))
        except Exception as e:
            logger.error('ListaVeiculosView (get_veiculos): ' + str(e))
        return veiculos

    def is_valor_promocional(self, valor_promocional):
        """
        """
        if valor_promocional:
            if len(valor_promocional) > 5:
                return True
