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
from bekam.veiculos.content.interfaces import IFolderDestaque
from bekam.veiculos.config import PROJECTNAME

# Schema definition
schema = ATFolder.schema.copy()

schemata.finalizeATCTSchema(schema)


class FolderDestaque(ATFolder):
    """
    """
    security = ClassSecurityInfo()
    implements(IFolderDestaque)

    meta_type = 'FolderDestaque'
    portal_type = 'FolderDestaque'

    _at_rename_after_creation = True

    schema = schema


atapi.registerType(FolderDestaque, PROJECTNAME)
