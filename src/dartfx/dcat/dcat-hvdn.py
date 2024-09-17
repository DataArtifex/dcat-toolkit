"""
DCAT profile and extensions for the High-Value Data Network.

"""
from dartfx.rdf import rdf

from dataclasses import dataclass
from rdflib import DCAT

@dataclass(kw_only=True)
class DcatHvdnResource(rdf.RdfResource):
    def __post_init__(self):
        if hasattr(super(), '__post_init__'):
            super().__post_init__()
        self._namespace = DCAT
        
@dataclass(kw_only=True)
class DcatHvdnClass(DcatHvdnResource):
    pass
    
@dataclass(kw_only=True)
class DcatHvdnProperty(DcatHvdnResource):
    pass

