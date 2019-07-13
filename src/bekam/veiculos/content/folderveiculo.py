# -*- coding: utf-8 -*-

# Zope3 imports
from zope.interface import implements

# Security
from AccessControl import ClassSecurityInfo

# Archetypes & ATCT imports
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.folder import ATFolder

# Product imports
from bekam.veiculos.content.interfaces import IFolderVeiculo
from bekam.veiculos.config import PROJECTNAME

# Schema definition
schema = ATFolder.schema.copy()

schemata.finalizeATCTSchema(schema)


class FolderVeiculo(ATFolder):
    """
    """
    security = ClassSecurityInfo()
    implements(IFolderVeiculo)

    meta_type = 'FolderVeiculo'
    portal_type = 'FolderVeiculo'

    _at_rename_after_creation = True

    schema = schema


atapi.registerType(FolderVeiculo, PROJECTNAME)
