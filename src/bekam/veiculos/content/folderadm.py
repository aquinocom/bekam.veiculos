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
from bekam.veiculos.content.interfaces import IFolderAdm
from bekam.veiculos.config import PROJECTNAME

# Schema definition
schema = ATFolder.schema.copy()

schemata.finalizeATCTSchema(schema)


class FolderAdm(ATFolder):
    """
    """
    security = ClassSecurityInfo()
    implements(IFolderAdm)

    meta_type = 'FolderAdm'
    portal_type = 'FolderAdm'

    _at_rename_after_creation = True

    schema = schema


atapi.registerType(FolderAdm, PROJECTNAME)
