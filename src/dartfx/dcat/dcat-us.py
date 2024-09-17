

from typing import Optional
from dartfx.ddi import rdf

from dataclasses import dataclass, field

from dartfx.rdf import skos

DCAT_US = "http://resources.data.gov/ontology/dcat-us#"

@dataclass(kw_only=True)
class DcatUSResource(rdf.RdfResource):
    def __post_init__(self):
        if hasattr(super(), '__post_init__'):
            super().__post_init__()
        self._namespace = DCAT_US

@dataclass(kw_only=True)
class DcatUSClass(DcatUSResource):
    pass
    
@dataclass(kw_only=True)
class DcatUSProperty(DcatUSResource):
    pass


@dataclass(kw_only=True)
class AccessRestriction(DcatUSClass):
    """Access Restriction.

    Definition:
    The "AccessRestriction" class used by NARA represents limitations placed on accessing specific records or information within their archives, 
    ensuring controlled and responsible access based on legal, ethical, or security considerations.
    
    Notes:
    - The "AccessRestriction" class serves as a valuable tool within NARA's archival framework, enabling the organization to effectively 
      manage and communicate access limitations for specific records or information. 
      By employing this class, NARA can categorize and enforce controlled access to sensitive content, safeguarding confidentiality, 
      adhering to legal requirements, and preserving the integrity of historical data. Researchers, archivists, and authorized users 
      can rely on "AccessRestriction" to navigate and understand the accessibility parameters associated with archived materials, 
      facilitating responsible information dissemination and usage.
    
    References:
    - https://doi-do.github.io/dcat-us/#properties-for-access_restriction
    
    """
    restrictionStatus: skos.Concept = field(default=None)
    specificRestriction: Optional[skos.Concept] = field(default=None)
    restrictionNote: Optional[rdf.RdfString] = field(default=None)
    
@dataclass(kw_only=True)
class CuiRestriction(DcatUSClass):
    """Controlled Unclassified Information (CUI).
    
    Controlled Unclassified Information (CUI) is information that requires safeguarding or dissemination controls 
    pursuant to and consistent with applicable law, regulations, and government-wide policies but is not classified.
    
    Definition:
    Represents Controlled Unclassified Information (CUI), which is information that requires safeguarding or dissemination controls
    in accordance with applicable laws, regulations, and government-wide policies but is not classified as confidential.    
    
    References:
    - https://doi-do.github.io/dcat-us/#properties-for-cui_restriction
    
    """
    cuiBannerMarking: str
    designationIndicator: str
    requiredIndicatorPerAuthority: Optional[str] = field(default=None)

class GeographicBoundingBox(DcatUSClass):
    """Geographic Bounding Box.
    
    Definition:
    GeographicBoundingBox describes the spatial extent of domain of application of an resource and is standardized in WGS 84 Lat/Long coordinate system.
    
    """
    westBoundingLongitude: float = field(metadata={"type": "xsd:decimal"})
    eastBoundingLongitude: float = field(metadata={"type": "xsd:decimal"})
    northBoundingLatitude: float = field(metadata={"type": "xsd:decimal"})
    southBoundingLatitude: float = field(metadata={"type": "xsd:decimal"})
    
class LiabilityStatement(DcatUSClass):
    """Liability Statement.
    
    Definition:
    A formal declaration accompanying a dataset intended to limit the legal exposure of the data provider by disclaiming warranties or guarantees.
    """
    label: list[rdf.RdfString] = field(default_factory=list)
    
class UseRestriction(DcatUSClass):
    """Use Restriction.
    
    Definition:
    A UseRestriction is a set of rules, guidelines, or legal provisions that dictate how a particular resource, 
    asset, information, or object can be utilized. Use restrictions may encompass limitations on access, 
    distribution, reproduction, modification, or sharing, and they are often put in place to protect privacy, 
    intellectual property rights, security, or compliance with legal or ethical standards.
    """
    restrictionStatus: skos.SkosConcept
    specificRestriction: Optional[skos.SkosConcept]  = field(default=None)
    restrictionNote: Optional[rdf.RdfString] = field(default=None)