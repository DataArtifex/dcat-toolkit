# SPDX-FileCopyrightText: 2024-present kulnor <pascal.heus@gmail.com>
#
# SPDX-License-Identifier: MIT

from .dcat import (
    DCAT,
    DcatResource,
    Resource,
    Dataset as DcatDataset,
    Catalog as DcatCatalog,
    CatalogRecord as DcatCatalogRecord,
    DatasetSeries as DcatDatasetSeries,
    Distribution as DcatDistribution,
    DataService as DcatDataService,
    Relationship,
)

from .dcat_us import (
    DCAT_US,
    DcatUSResource,
    AccessRestriction,
    CuiRestriction,
    GeographicBoundingBox,
    LiabilityStatement,
    UseRestriction,
)

from .dcat_ap import (
    DCATAP,
    DcatAPResource,
    Catalog as DcatAPCatalog,
    Dataset as DcatAPDataset,
    Distribution as DcatAPDistribution,
    DataService as DcatAPDataService,
    DatasetSeries as DcatAPDatasetSeries,
    CatalogRecord as DcatAPCatalogRecord,
    ControlledVocabularies,
    HVDCategory as DcatAPHVDCategory,
)

# Import HVD classes (these become the default exports)
from .dcat_ap_hvd import (
    DCATAP_HVD,
    HVD_REGULATION,
    HVDResource,
    Catalog,
    Dataset,
    Distribution,
    DataService,
    DatasetSeries,
    CatalogRecord,
    HVDCategory,
    HVDLicence,
)

__all__ = [
    # DCAT core
    "DCAT",
    "DcatResource",
    "Resource",
    "DcatDataset",
    "DcatCatalog",
    "DcatCatalogRecord",
    "DcatDatasetSeries",
    "DcatDistribution",
    "DcatDataService",
    "Relationship",
    # DCAT-US
    "DCAT_US",
    "DcatUSResource",
    "AccessRestriction",
    "CuiRestriction",
    "GeographicBoundingBox",
    "LiabilityStatement",
    "UseRestriction",
    # DCAT-AP
    "DCATAP",
    "DcatAPResource",
    "DcatAPCatalog",
    "DcatAPDataset",
    "DcatAPDistribution",
    "DcatAPDataService",
    "DcatAPDatasetSeries",
    "DcatAPCatalogRecord",
    "ControlledVocabularies",
    "DcatAPHVDCategory",
    # DCAT-AP HVD (default exports - most specific)
    "DCATAP_HVD",
    "HVD_REGULATION",
    "HVDResource",
    "Catalog",
    "Dataset",
    "Distribution",
    "DataService",
    "DatasetSeries",
    "CatalogRecord",
    "HVDCategory",
    "HVDLicence",
]
