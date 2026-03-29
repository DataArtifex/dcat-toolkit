# SPDX-FileCopyrightText: 2024-present kulnor <pascal.heus@gmail.com>
#
# SPDX-License-Identifier: MIT

from .dcat import (
    DCAT,
    DcatResource,
    Relationship,
    Resource,
)
from .dcat import (
    Catalog as DcatCatalog,
)
from .dcat import (
    CatalogRecord as DcatCatalogRecord,
)
from .dcat import (
    DataService as DcatDataService,
)
from .dcat import (
    Dataset as DcatDataset,
)
from .dcat import (
    DatasetSeries as DcatDatasetSeries,
)
from .dcat import (
    Distribution as DcatDistribution,
)
from .dcat_ap import (
    DCATAP,
    ControlledVocabularies,
    DcatAPResource,
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
from .dcat_ap import (
    HVDCategory as DcatAPHVDCategory,
)

# Import HVD classes (these become the default exports)
from .dcat_ap_hvd import (
    DCATAP_HVD,
    HVD_REGULATION,
    Catalog,
    CatalogRecord,
    DataService,
    Dataset,
    DatasetSeries,
    Distribution,
    HVDCategory,
    HVDLicence,
    HVDResource,
)
from .dcat_us import (
    DCAT_US,
    AccessRestriction,
    CuiRestriction,
    DcatUSResource,
    GeographicBoundingBox,
    LiabilityStatement,
    UseRestriction,
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
