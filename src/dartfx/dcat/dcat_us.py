"""
DCAT-US - Version 3.0

Data Catalog Application Profile for the United States of America

This module provides Pydantic-based models for the DCAT-US 3.0 specification,
which extends DCAT 3 with US-specific requirements and classes.

References:
- https://doi-do.github.io/dcat-us/
- https://www.w3.org/TR/vocab-dcat-3/

"""

# mypy: disable-error-code=misc

from __future__ import annotations

from decimal import Decimal
from typing import Annotated

from pydantic import Field
from rdflib import Namespace, URIRef

from dartfx.rdf.pydantic import RdfBaseModel, RdfProperty, dcterms

# DCAT-US Namespace
DCAT_US = Namespace("http://resources.data.gov/ontology/dcat-us#")

# Additional namespaces used in DCAT-US
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
ADMS = Namespace("http://www.w3.org/ns/adms#")
PROV = Namespace("http://www.w3.org/ns/prov#")
LOCN = Namespace("http://www.w3.org/ns/locn#")
VCARD = Namespace("http://www.w3.org/2006/vcard/ns#")
ORG = Namespace("http://www.w3.org/ns/org#")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
DQV = Namespace("https://www.w3.org/TR/vocab-dqv/")
GSP = Namespace("http://www.opengis.net/ont/geosparql#")
SPDX = Namespace("http://spdx.org/rdf/terms#")


class DcatUSResource(RdfBaseModel):
    """Base class for all DCAT-US resources."""

    rdf_namespace = DCAT_US
    rdf_prefixes = {
        "dcat-us": DCAT_US,
        "dcterms": dcterms.DCTERMS,
        "skos": SKOS,
        "adms": ADMS,
        "prov": PROV,
        "locn": LOCN,
        "vcard": VCARD,
        "org": ORG,
        "foaf": FOAF,
        "dqv": DQV,
        "gsp": GSP,
        "spdx": SPDX,
    }


class AccessRestriction(DcatUSResource):
    """Access Restriction.

    Definition:
    The "AccessRestriction" class used by NARA represents limitations placed on accessing
    specific records or information within their archives, ensuring controlled and responsible
    access based on legal, ethical, or security considerations.

    Notes:
    - The "AccessRestriction" class serves as a valuable tool within NARA's archival framework,
      enabling the organization to effectively manage and communicate access limitations for
      specific records or information.
    - By employing this class, NARA can categorize and enforce controlled access to sensitive
      content, safeguarding confidentiality, adhering to legal requirements, and preserving
      the integrity of historical data.
    - Researchers, archivists, and authorized users can rely on "AccessRestriction" to navigate
      and understand the accessibility parameters associated with archived materials, facilitating
      responsible information dissemination and usage.

    References:
    - https://doi-do.github.io/dcat-us/#properties-for-access_restriction

    """

    rdf_type = DCAT_US.AccessRestriction

    id: str

    # Mandatory properties
    restrictionStatus: Annotated[str | URIRef, RdfProperty(DCAT_US.restrictionStatus)]

    # Optional properties
    specificRestriction: Annotated[str | URIRef | None, RdfProperty(DCAT_US.specificRestriction)] = None
    restrictionNote: Annotated[str | None, RdfProperty(DCAT_US.restrictionNote)] = None


class CuiRestriction(DcatUSResource):
    """Controlled Unclassified Information (CUI) Restriction.

    Definition:
    Represents Controlled Unclassified Information (CUI), which is information that requires
    safeguarding or dissemination controls in accordance with applicable laws, regulations,
    and government-wide policies but is not classified as confidential.

    Notes:
    - The CUI Restriction class is designed to capture information related to Controlled
      Unclassified Information (CUI) in accordance with NARA guidelines.
    - Users of this class must provide the mandatory properties, i.e the CUI banner marking
      and designation indicator, to accurately describe the CUI status of a resource.
    - The optional property, "required indicator per authority," allows for additional
      information or context about CUI restrictions, providing flexibility for specific use cases.

    References:
    - https://doi-do.github.io/dcat-us/#properties-for-cui_restriction

    """

    rdf_type = DCAT_US.CuiRestriction

    id: str

    # Mandatory properties
    cuiBannerMarking: Annotated[str, RdfProperty(DCAT_US.cuiBannerMarking)]
    designationIndicator: Annotated[str, RdfProperty(DCAT_US.designationIndicator)]

    # Optional properties
    requiredIndicatorPerAuthority: Annotated[str | None, RdfProperty(DCAT_US.requiredIndicatorPerAuthority)] = None


class GeographicBoundingBox(DcatUSResource):
    """Geographic Bounding Box.

    Definition:
    GeographicBoundingBox describes the spatial extent of domain of application of a resource
    and is standardized in WGS 84 Lat/Long coordinate system.

    Notes:
    - All four bounding coordinates are mandatory
    - Coordinates use WGS 84 Lat/Long coordinate system
    - Values are xsd:decimal type

    References:
    - https://doi-do.github.io/dcat-us/#properties-for-geographic_bbox

    """

    rdf_type = DCAT_US.GeographicBoundingBox

    id: str

    # Mandatory properties (all coordinates required)
    westBoundingLongitude: Annotated[Decimal, RdfProperty(DCAT_US.westBoundingLongitude)]
    eastBoundingLongitude: Annotated[Decimal, RdfProperty(DCAT_US.eastBoundingLongitude)]
    northBoundingLatitude: Annotated[Decimal, RdfProperty(DCAT_US.northBoundingLatitude)]
    southBoundingLatitude: Annotated[Decimal, RdfProperty(DCAT_US.southBoundingLatitude)]


class LiabilityStatement(DcatUSResource):
    """Liability Statement.

    Definition:
    A formal declaration accompanying a dataset which outlines the responsibilities and
    limitations of the data provider in terms of the accuracy, completeness, and potential
    use of the data. It often serves to limit the legal exposure of the data provider by
    defining the scope of allowed uses and disclaiming warranties or guarantees.

    Notes:
    This statement often includes information of the following aspects:
    - Limitation of Responsibility: Clarifying that the publisher or provider is not
      responsible for any errors in the data, and any consequences resulting from its use.
    - No Guarantee of Validity: Indicating that there is no guarantee of the accuracy,
      reliability, or completeness of the data provided.
    - Absence of Endorsement: Stating that inclusion of the data in the catalog does not
      imply endorsement by the publisher or provider.
    - Use at Own Risk: Advising users that they use the data at their own risk and are
      responsible for ensuring its appropriateness for their intended purposes.

    The statement may be provided as a literal text or as a URL pointing to a detailed
    liability statement.

    References:
    - https://doi-do.github.io/dcat-us/#properties-for-liability_statement

    """

    rdf_type = DCAT_US.LiabilityStatement

    id: str

    # Optional properties
    label: Annotated[list[str], RdfProperty(Namespace("http://www.w3.org/2000/01/rdf-schema#").label)] = Field(
        default_factory=list
    )

    def add_label(self, value: str, lang: str | None = None) -> None:
        """Add a liability statement label/text."""
        del lang
        self.label.append(value)


class UseRestriction(DcatUSResource):
    """Use Restriction.

    Definition:
    A UseRestriction is a set of rules, guidelines, or legal provisions that dictate how a
    particular resource, asset, information, or object can be utilized. Use restrictions may
    encompass limitations on access, distribution, reproduction, modification, or sharing,
    and they are often put in place to protect privacy, intellectual property rights, security,
    or compliance with legal or ethical standards.

    References:
    - https://doi-do.github.io/dcat-us/#properties-for-use_restriction

    """

    rdf_type = DCAT_US.UseRestriction

    id: str

    # Mandatory properties
    restrictionStatus: Annotated[str | URIRef, RdfProperty(DCAT_US.restrictionStatus)]

    # Recommended properties
    specificRestriction: Annotated[str | URIRef | None, RdfProperty(DCAT_US.specificRestriction)] = None

    # Optional properties
    restrictionNote: Annotated[str | None, RdfProperty(DCAT_US.restrictionNote)] = None


# Rebuild models to handle forward references
AccessRestriction.model_rebuild()
CuiRestriction.model_rebuild()
GeographicBoundingBox.model_rebuild()
LiabilityStatement.model_rebuild()
UseRestriction.model_rebuild()


__all__ = [
    "DCAT_US",
    "DcatUSResource",
    "AccessRestriction",
    "CuiRestriction",
    "GeographicBoundingBox",
    "LiabilityStatement",
    "UseRestriction",
]
