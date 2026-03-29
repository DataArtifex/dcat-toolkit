"""
DCAT-AP HVD - Version 3.0.0

DCAT Application Profile for High Value Datasets

This module provides Pydantic-based models for the DCAT-AP HVD specification,
which extends DCAT-AP 3.0 with specific requirements for High Value Datasets
as defined in Commission Implementing Regulation (EU) 2023/138.

DCAT-AP HVD provides usage guidelines on top of DCAT-AP for datasets that are
subject to the requirements imposed by the High-Value Dataset implementing regulation.

References:
- https://semiceu.github.io/DCAT-AP/releases/3.0.0-hvd/
- https://eur-lex.europa.eu/eli/reg_impl/2023/138/oj
- https://semiceu.github.io/DCAT-AP/releases/3.0.1/

"""

# mypy: disable-error-code=misc

from __future__ import annotations

from typing import Annotated

from pydantic import Field
from rdflib import Namespace, URIRef

from dartfx.rdf.pydantic import RdfBaseModel, RdfProperty, dcterms

# Import DCAT-AP classes
from .dcat_ap import (
    DCATAP,
)
from .dcat_ap import (
    Catalog as DcatAPCatalog,
)
from .dcat_ap import (
    CatalogRecord as DcatAPCatalogRecord,
)
from .dcat_ap import (
    DataService as DcatAPDataService,
)
from .dcat_ap import (
    Dataset as DcatAPDataset,
)
from .dcat_ap import (
    DatasetSeries as DcatAPDatasetSeries,
)
from .dcat_ap import (
    Distribution as DcatAPDistribution,
)

# HVD-specific namespace
DCATAP_HVD = Namespace("http://data.europa.eu/r5r/")

# HVD Regulation
HVD_REGULATION = "http://data.europa.eu/eli/reg_impl/2023/138/oj"

# EU Vocabularies
EU_HVD_CATEGORY = Namespace("http://data.europa.eu/bna/")


class HVDCategory:
    """High Value Dataset Categories.

    The six thematic categories of High Value Datasets as defined in
    Commission Implementing Regulation (EU) 2023/138.

    These are the official URIs from the EU Vocabularies HVD Categories
    Named Authority List.

    References:
    - https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/high-value-dataset-category

    """

    # Official HVD Categories from EU Vocabularies
    GEOSPATIAL = "http://data.europa.eu/bna/c_164e0bf5"
    EARTH_OBSERVATION = "http://data.europa.eu/bna/c_a9135398"
    ENVIRONMENT = "http://data.europa.eu/bna/c_ac64a52d"
    METEOROLOGICAL = "http://data.europa.eu/bna/c_b803a9a9"
    STATISTICS = "http://data.europa.eu/bna/c_dd313021"
    COMPANIES = "http://data.europa.eu/bna/c_e1da4e07"

    @classmethod
    def all_categories(cls) -> list[str]:
        """Return all HVD category URIs."""
        return [
            cls.GEOSPATIAL,
            cls.EARTH_OBSERVATION,
            cls.ENVIRONMENT,
            cls.METEOROLOGICAL,
            cls.STATISTICS,
            cls.COMPANIES,
        ]

    @classmethod
    def is_valid_category(cls, uri: str) -> bool:
        """Check if a URI is a valid HVD category."""
        return uri in cls.all_categories()


class HVDResource(RdfBaseModel):
    """Base class for HVD resources."""

    rdf_prefixes = {
        "dcatap": DCATAP,
        "dcterms": dcterms.DCTERMS,
    }


# Extend DCAT-AP classes with HVD-specific requirements


class Catalog(DcatAPCatalog):
    """DCAT-AP HVD Catalog.

    Extends DCAT-AP Catalog with HVD-specific requirements.

    For HVD, catalogs must contain datasets and/or data services that are
    subject to the HVD regulation.

    References:
    - https://semiceu.github.io/DCAT-AP/releases/3.0.0-hvd/#Catalogue

    """

    pass  # No additional mandatory properties for HVD Catalog


class Dataset(DcatAPDataset):
    """DCAT-AP HVD Dataset.

    Extends DCAT-AP Dataset with HVD-specific mandatory requirements.

    HVD Datasets MUST have:
    - Applicable legislation (HVD regulation)
    - HVD category
    - Contact point
    - Conforms to (for specific data requirements)
    - At least one distribution or data service

    References:
    - https://semiceu.github.io/DCAT-AP/releases/3.0.0-hvd/#Dataset

    """

    # HVD-specific mandatory property
    hvdCategory: Annotated[list[str | URIRef], RdfProperty(DCATAP.hvdCategory)] = Field(default_factory=list)

    def add_hvd_category(self, category: str | URIRef) -> str | URIRef:
        """Add HVD category (mandatory for HVD datasets).

        Args:
            category: HVD category URI from EU Vocabularies

        Returns:
            The added category URI

        Example:
            dataset.add_hvd_category(HVDCategory.GEOSPATIAL)
        """
        self.hvdCategory.append(category)
        return category

    def make_hvd_compliant(self, category: str | URIRef) -> None:
        """Make this dataset HVD-compliant by adding required properties.

        This is a convenience method that adds the HVD regulation and category.

        Args:
            category: HVD category URI from EU Vocabularies

        Example:
            dataset.make_hvd_compliant(HVDCategory.GEOSPATIAL)
        """
        # Add HVD regulation (mandatory)
        if HVD_REGULATION not in self.applicableLegislation:
            self.add_applicable_legislation(HVD_REGULATION)

        # Add HVD category (mandatory)
        if category not in self.hvdCategory:
            self.add_hvd_category(category)

    def is_hvd_compliant(self) -> bool:
        """Check if this dataset meets HVD mandatory requirements.

        Returns:
            True if the dataset has HVD regulation and at least one HVD category
        """
        has_regulation = HVD_REGULATION in self.applicableLegislation
        has_category = len(self.hvdCategory) > 0
        return has_regulation and has_category


class Distribution(DcatAPDistribution):
    """DCAT-AP HVD Distribution.

    Extends DCAT-AP Distribution with HVD-specific mandatory requirements.

    HVD Distributions MUST have:
    - Applicable legislation (HVD regulation)
    - Access URL (mandatory)
    - Licence (mandatory, must be compatible with CC-BY 4.0 or more permissive)
    - Access service (for API access)

    References:
    - https://semiceu.github.io/DCAT-AP/releases/3.0.0-hvd/#Distribution

    """

    def make_hvd_compliant(self) -> None:
        """Make this distribution HVD-compliant by adding required properties.

        This is a convenience method that adds the HVD regulation.
        Note: You still need to set licence and access URL manually.

        Example:
            distribution.make_hvd_compliant()
            distribution.add_access_url("http://example.org/data")
            distribution.add_license("http://creativecommons.org/licenses/by/4.0/")
        """
        # Add HVD regulation (mandatory)
        if HVD_REGULATION not in self.applicableLegislation:
            self.add_applicable_legislation(HVD_REGULATION)

    def is_hvd_compliant(self) -> bool:
        """Check if this distribution meets HVD mandatory requirements.

        Returns:
            True if the distribution has HVD regulation, access URL, and licence
        """
        has_regulation = HVD_REGULATION in self.applicableLegislation
        has_access_url = len(self.accessUrl) > 0
        has_licence = len(self.license) > 0
        return has_regulation and has_access_url and has_licence


class DataService(DcatAPDataService):
    """DCAT-AP HVD Data Service.

    Extends DCAT-AP DataService with HVD-specific mandatory requirements.

    HVD Data Services (APIs) MUST have:
    - Applicable legislation (HVD regulation)
    - HVD category
    - Endpoint URL (persistent)
    - Contact point

    Note: APIs are mandatory for HVD datasets.

    References:
    - https://semiceu.github.io/DCAT-AP/releases/3.0.0-hvd/#DataService

    """

    # HVD-specific mandatory property
    hvdCategory: Annotated[list[str | URIRef], RdfProperty(DCATAP.hvdCategory)] = Field(default_factory=list)

    def add_hvd_category(self, category: str | URIRef) -> str | URIRef:
        """Add HVD category (mandatory for HVD data services).

        Args:
            category: HVD category URI from EU Vocabularies

        Returns:
            The added category URI
        """
        self.hvdCategory.append(category)
        return category

    def make_hvd_compliant(self, category: str | URIRef) -> None:
        """Make this data service HVD-compliant by adding required properties.

        Args:
            category: HVD category URI from EU Vocabularies

        Example:
            service.make_hvd_compliant(HVDCategory.GEOSPATIAL)
        """
        # Add HVD regulation (mandatory)
        if HVD_REGULATION not in self.applicableLegislation:
            self.add_applicable_legislation(HVD_REGULATION)

        # Add HVD category (mandatory)
        if category not in self.hvdCategory:
            self.add_hvd_category(category)

    def is_hvd_compliant(self) -> bool:
        """Check if this data service meets HVD mandatory requirements.

        Returns:
            True if the service has HVD regulation and at least one HVD category
        """
        has_regulation = HVD_REGULATION in self.applicableLegislation
        has_category = len(self.hvdCategory) > 0
        has_endpoint = len(self.endpointURL) > 0
        return has_regulation and has_category and has_endpoint


class DatasetSeries(DcatAPDatasetSeries):
    """DCAT-AP HVD Dataset Series.

    Extends DCAT-AP DatasetSeries with HVD-specific mandatory requirements.

    HVD Dataset Series MUST have:
    - Applicable legislation (HVD regulation)
    - HVD category

    References:
    - https://semiceu.github.io/DCAT-AP/releases/3.0.0-hvd/#DatasetSeries

    """

    # HVD-specific mandatory property
    hvdCategory: Annotated[list[str | URIRef], RdfProperty(DCATAP.hvdCategory)] = Field(default_factory=list)

    def add_hvd_category(self, category: str | URIRef) -> str | URIRef:
        """Add HVD category (mandatory for HVD dataset series).

        Args:
            category: HVD category URI from EU Vocabularies

        Returns:
            The added category URI
        """
        self.hvdCategory.append(category)
        return category

    def make_hvd_compliant(self, category: str | URIRef) -> None:
        """Make this dataset series HVD-compliant by adding required properties.

        Args:
            category: HVD category URI from EU Vocabularies
        """
        # Add HVD regulation (mandatory)
        if HVD_REGULATION not in self.applicableLegislation:
            self.add_applicable_legislation(HVD_REGULATION)

        # Add HVD category (mandatory)
        if category not in self.hvdCategory:
            self.add_hvd_category(category)


class CatalogRecord(DcatAPCatalogRecord):
    """DCAT-AP HVD Catalog Record.

    Extends DCAT-AP CatalogRecord with HVD requirements.

    References:
    - https://semiceu.github.io/DCAT-AP/releases/3.0.0-hvd/#CatalogueRecord

    """

    pass  # No additional mandatory properties for HVD Catalog Record


# Rebuild models to handle forward references
Catalog.model_rebuild()
Dataset.model_rebuild()
Distribution.model_rebuild()
DataService.model_rebuild()
DatasetSeries.model_rebuild()
CatalogRecord.model_rebuild()


# HVD Licence Requirements
class HVDLicence:
    """HVD Licence Requirements.

    According to the HVD regulation, datasets must be made available under
    licences that are compatible with Creative Commons BY 4.0 or more permissive.

    This class provides common licence URIs that meet HVD requirements.

    References:
    - Article 3 of Regulation (EU) 2023/138

    """

    # Creative Commons licences (HVD compliant)
    CC_BY_4_0 = "http://creativecommons.org/licenses/by/4.0/"
    CC0_1_0 = "http://creativecommons.org/publicdomain/zero/1.0/"  # Public domain

    # EU-specific licences
    EU_NO_RESTRICTIONS = "http://publications.europa.eu/resource/authority/licence/NO_RESTRICTIONS"

    @classmethod
    def is_hvd_compliant(cls, licence_uri: str) -> bool:
        """Check if a licence URI is HVD-compliant.

        Note: This is a basic check. Full compliance requires manual verification
        that the licence is compatible with CC-BY 4.0 or more permissive.

        Args:
            licence_uri: The licence URI to check

        Returns:
            True if the licence is known to be HVD-compliant
        """
        compliant_licences = [
            cls.CC_BY_4_0,
            cls.CC0_1_0,
            cls.EU_NO_RESTRICTIONS,
        ]
        return licence_uri in compliant_licences


__all__ = [
    # Namespaces
    "DCATAP_HVD",
    "HVD_REGULATION",
    # HVD-specific classes
    "HVDResource",
    "Catalog",
    "Dataset",
    "Distribution",
    "DataService",
    "DatasetSeries",
    "CatalogRecord",
    # HVD categories and licences
    "HVDCategory",
    "HVDLicence",
]
