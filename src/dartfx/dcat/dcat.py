"""
DCAT is an RDF vocabulary for representing data catalogs.

DCAT is developed and maintained by the W3C

References:
- https://www.w3.org/TR/vocab-dcat-3/

"""
from __future__ import annotations

from datetime import date, datetime
from typing import Annotated, List, Optional, Union
from dateutil.parser import parse

from rdflib import Namespace, URIRef
from pydantic import Field

from dartfx.rdf.pydantic import RdfBaseModel, RdfProperty
from dartfx.rdf.pydantic import dcterms, foaf, spdx

# DCAT Namespace
DCAT = Namespace("http://www.w3.org/ns/dcat#")


class DcatResource(RdfBaseModel):
    """Base class for all DCAT resources."""
    
    rdf_namespace = DCAT
    rdf_prefixes = {
        "dcat": DCAT,
        "dcterms": dcterms.DCTERMS,
        "foaf": foaf.FOAF,
        "spdx": spdx.SPDX,
    }


class Resource(DcatResource):
    """Cataloged Resource.
    
    Definition:
    Resource published or curated by a single agent.

    References:
    - https://www.w3.org/TR/vocab-dcat-3/#Class:Resource
    
    """
    rdf_type = DCAT.Resource
    
    id: str
    
    # DCAT properties
    accessRights: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.accessRights)] = Field(default_factory=list)
    conformsTo: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.conformsTo)] = Field(default_factory=list)
    contactPoint: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.contactPoint)] = Field(default_factory=list)
    creator: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.creator)] = Field(default_factory=list)
    description: Annotated[Optional[List[str]], RdfProperty(dcterms.DCTERMS.description)] = Field(default_factory=list)
    issued: Annotated[Optional[List[datetime]], RdfProperty(dcterms.DCTERMS.issued)] = Field(default_factory=list)
    identifier: Annotated[Optional[List[str]], RdfProperty(dcterms.DCTERMS.identifier)] = Field(default_factory=list)
    keyword: Annotated[Optional[List[str]], RdfProperty(DCAT.keyword)] = Field(default_factory=list)
    landingPage: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.landingPage)] = Field(default_factory=list)
    license: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.license)] = Field(default_factory=list)
    language: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.language)] = Field(default_factory=list)
    publisher: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.publisher)] = Field(default_factory=list)
    title: Annotated[Optional[List[str]], RdfProperty(dcterms.DCTERMS.title)] = Field(default_factory=list)
    type: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.type)] = Field(default_factory=list)
    modified: Annotated[Optional[List[datetime]], RdfProperty(dcterms.DCTERMS.modified)] = Field(default_factory=list)
    version: Annotated[Optional[str], RdfProperty(DCAT.version)] = None
    versionNotes: Annotated[Optional[List[str]], RdfProperty(Namespace("http://www.w3.org/ns/adms#").versionNotes)] = Field(default_factory=list)

    def add_access_rights(self, value: Union[str, URIRef], lang: Optional[str] = None) -> None:
        """Add access rights information."""
        self.accessRights.append(value)

    def add_conforms_to(self, value: Union[str, URIRef], lang: Optional[str] = None) -> None:
        """Add conformance standard."""
        self.conformsTo.append(value)

    def add_creator(self, value: Union[str, URIRef]) -> None:
        """Add creator."""
        self.creator.append(value)

    def add_description(self, value: str, lang: Optional[str] = None) -> None:
        """Add description."""
        self.description.append(value)

    def add_identifier(self, value: str) -> None:
        """Add identifier."""
        self.identifier.append(value)

    def add_keyword(self, value: str) -> None:
        """Add keyword."""
        self.keyword.append(value)

    def add_language(self, value: Union[str, URIRef]) -> None:
        """Add language."""
        self.language.append(value)

    def add_landing_page(self, value: Union[str, URIRef]) -> Union[str, URIRef]:
        """Add landing page URL."""
        self.landingPage.append(value)
        return value

    def add_license(self, value: Union[str, URIRef]) -> None:
        """Add license."""
        self.license.append(value)

    def add_modified_date(self, value: Union[str, date, datetime]) -> None:
        """Add modified date."""
        if not isinstance(value, (date, datetime)):
            if isinstance(value, str):
                value = parse(value)
        self.modified.append(value)
        
    def add_publisher(self, value: Union[str, URIRef]) -> Union[str, URIRef]:
        """Add publisher."""
        self.publisher.append(value)
        return value
                
    def add_release_date(self, value: Union[str, date, datetime]) -> None:
        """Add release/issued date."""
        if not isinstance(value, (date, datetime)):
            if isinstance(value, str):
                value = parse(value)
        self.issued.append(value)

    def add_title(self, value: str, lang: Optional[str] = None) -> None:
        """Add title."""
        self.title.append(value)

    def add_type(self, value: Union[str, URIRef]) -> None:
        """Add type."""
        self.type.append(value)

    def add_version_notes(self, value: str, lang: Optional[str] = None) -> None:
        """Add version notes."""
        self.versionNotes.append(value)


class Dataset(Resource):
    """DCAT Dataset.
    
    Definition:
    A collection of data, published or curated by a single agent, and available for access or download in one or more representations.
    
    References:
    - https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset
    """
    rdf_type = DCAT.Dataset
    
    distribution: Annotated[Optional[List["Distribution"]], RdfProperty(DCAT.distribution)] = Field(default_factory=list)
    accrualPeriodicity: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.accrualPeriodicity)] = Field(default_factory=list)
    inSeries: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.inSeries)] = Field(default_factory=list)
    spatial: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.spatial)] = Field(default_factory=list)
    theme: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.theme)] = Field(default_factory=list)

    def add_accrual_periodicity(self, value: Union[str, URIRef]) -> Union[str, URIRef]:
        """Add accrual periodicity (update frequency)."""
        self.accrualPeriodicity.append(value)
        return value

    def add_distribution(self, value: "Distribution") -> None:
        """Add a distribution."""
        if not isinstance(value, Distribution):
            raise TypeError(f"Expected Distribution, got {type(value)}")
        self.distribution.append(value)
        
    def add_frequency(self, value: Union[str, URIRef]) -> Union[str, URIRef]:
        """Add frequency (alias for add_accrual_periodicity)."""
        return self.add_accrual_periodicity(value=value)

    def add_spatial(self, value: Union[str, URIRef]) -> Union[str, URIRef]:
        """Add spatial coverage."""
        self.spatial.append(value)   
        return value

    def add_theme(self, value: Union[str, URIRef]) -> Union[str, URIRef]:
        """Add theme/category."""
        self.theme.append(value)
        return value

        
class Catalog(Dataset):
    """DCAT Catalog.
    
    Definition:
    A curated collection of metadata about resources (e.g., datasets and data services in the context of a data catalog).
    
    References:
    - https://www.w3.org/TR/vocab-dcat-3/#Class:Catalog
    """
    rdf_type = DCAT.Catalog
    
    homepage: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(foaf.FOAF.homepage)] = Field(default_factory=list)
    catalogRecord: Annotated[Optional[List["CatalogRecord"]], RdfProperty(DCAT.record)] = Field(default_factory=list)
    themeTaxonomy: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.themeTaxonomy)] = Field(default_factory=list)
    resource: Annotated[Optional[List["Resource"]], RdfProperty(DCAT.resource)] = Field(default_factory=list)
    dataset: Annotated[Optional[List["Dataset"]], RdfProperty(DCAT.dataset)] = Field(default_factory=list)
    service: Annotated[Optional[List["DataService"]], RdfProperty(DCAT.service)] = Field(default_factory=list)
    catalog: Annotated[Optional[List["Catalog"]], RdfProperty(DCAT.catalog)] = Field(default_factory=list)
    
    def add_catalog(self, value: "Catalog") -> None:
        """Add a sub-catalog."""
        if not isinstance(value, Catalog):
            raise TypeError(f"Expected Catalog, got {type(value)}")
        self.catalog.append(value)
   
    def add_catalog_record(self, value: "CatalogRecord") -> None:
        """Add a catalog record."""
        if not isinstance(value, CatalogRecord):
            raise TypeError(f"Expected CatalogRecord, got {type(value)}")
        self.catalogRecord.append(value)
   
    def add_homepage(self, value: Union[str, URIRef]) -> None:
        """Add homepage."""
        self.homepage.append(value)
        
    def add_dataset(self, value: "Dataset") -> None:
        """Add a dataset."""
        if not isinstance(value, Dataset):
            raise TypeError(f"Expected Dataset, got {type(value)}")
        self.dataset.append(value)

    def add_service(self, value: "DataService") -> None:
        """Add a data service."""
        if not isinstance(value, DataService):  
            raise TypeError(f"Expected DataService, got {type(value)}")
        self.service.append(value)
        
    def add_resource(self, value: "Resource") -> None:
        """Add a resource."""
        if not isinstance(value, Resource):
            raise TypeError(f"Expected Resource, got {type(value)}")
        self.resource.append(value)
    
    def add_theme_taxonomy(self, value: Union[str, URIRef]) -> Union[str, URIRef]:
        """Add theme taxonomy."""
        self.themeTaxonomy.append(value)
        return value
    

class CatalogRecord(DcatResource):
    """DCAT Catalog Record.
    
    Definition:
    A record in a catalog, describing the registration of a single resource.
    
    References:
    - https://www.w3.org/TR/vocab-dcat-3/#Class:Catalog_Record
    """
    rdf_type = DCAT.CatalogRecord
    
    id: str
    title: Annotated[Optional[List[str]], RdfProperty(dcterms.DCTERMS.title)] = Field(default_factory=list)
    description: Annotated[Optional[List[str]], RdfProperty(dcterms.DCTERMS.description)] = Field(default_factory=list)
    issued: Annotated[Optional[List[datetime]], RdfProperty(dcterms.DCTERMS.issued)] = Field(default_factory=list)


class DatasetSeries(Dataset):
    """Dataset Series.
    
    Definition:
    A collection of datasets that are published separately, but share some characteristics that group them.
    
    Notes:
    - Dataset series can be also soft-typed via property dcterms:type as in the approach used in [GeoDCAT-AP], and adopted in [DCAT-AP-IT] and [GeoDCAT-AP-IT]).
    - Common scenarios for dataset series include: time series composed of periodically released subsets; map-series composed of items of the same type or theme but with differing spatial footprints.
    
    References:
    - https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset_Series
    
    """
    rdf_type = DCAT.DatasetSeries


class Distribution(DcatResource):
    """DCAT Distribution
        
    Definition:
    A specific representation of a dataset. A dataset might be available in multiple serializations that may differ in various ways, 
    including natural language, media-type or format, schematic organization, temporal and spatial resolution, level of detail or
    profiles (which might specify any or all of the above).
    
    Usage:
    This represents a general availability of a dataset. It implies no information about the actual access method of the data, i.e., whether by direct download, API, or through a Web page. The use of dcat:downloadURL property indicates directly downloadable distributions.
    
    References:
    - https://www.w3.org/TR/vocab-dcat-3/#Class:Distribution
    """
    rdf_type = DCAT.Distribution
    
    id: str
    
    accessRights: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.accessRights)] = Field(default_factory=list)
    accessUrl: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.accessURL)] = Field(default_factory=list)
    accessService: Annotated[Optional[List["DataService"]], RdfProperty(DCAT.accessService)] = Field(default_factory=list)
    byteSize: Annotated[Optional[int], RdfProperty(DCAT.byteSize)] = None
    checksum: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(spdx.SPDX.checksum)] = Field(default_factory=list)
    compressionFormat: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.compressFormat)] = Field(default_factory=list)
    conformsTo: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.conformsTo)] = Field(default_factory=list)
    description: Annotated[Optional[List[str]], RdfProperty(dcterms.DCTERMS.description)] = Field(default_factory=list)
    downloadURL: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.downloadURL)] = Field(default_factory=list)
    format: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS["format"])] = Field(default_factory=list)
    mediaType: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.mediaType)] = Field(default_factory=list)
    packagingFormat: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.packageFormat)] = Field(default_factory=list)
    issued: Annotated[Optional[List[datetime]], RdfProperty(dcterms.DCTERMS.issued)] = Field(default_factory=list)
    modified: Annotated[Optional[List[datetime]], RdfProperty(dcterms.DCTERMS.modified)] = Field(default_factory=list)
    license: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.license)] = Field(default_factory=list)
    rights: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(dcterms.DCTERMS.rights)] = Field(default_factory=list)
    title: Annotated[Optional[List[str]], RdfProperty(dcterms.DCTERMS.title)] = Field(default_factory=list)
     
    def add_download_url(self, value: Union[str, URIRef]) -> Union[str, URIRef]:
        """Add download URL."""
        self.downloadURL.append(value)
        return value

    def add_media_type(self, value: Union[str, URIRef]) -> Union[str, URIRef]:
        """Add media type."""
        self.mediaType.append(value)
        return value



class DataService(Resource):
    """ Data Service.
    
    Definition:
    A collection of operations that provides access to one or more datasets or data processing functions.
    
    Notes:
    - If a dcat:DataService is bound to one or more specified Datasets, they are indicated by the dcat:servesDataset property.
    - The kind of service can be indicated using the dcterms:type property. 
      Its value may be taken from a controlled vocabulary such as the INSPIRE spatial data service type code list [INSPIRE-SDST].
    
    References:
    - https://www.w3.org/TR/vocab-dcat-3/#Class:Data_Service
    """
    rdf_type = DCAT.DataService
    
    servesDataset: Annotated[Optional[List[Dataset]], RdfProperty(DCAT.servesDataset)] = Field(default_factory=list)
    endpointURL: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.endpointURL)] = Field(default_factory=list)
    endpointDescription: Annotated[Optional[List[Union[str, URIRef]]], RdfProperty(DCAT.endpointDescription)] = Field(default_factory=list)

    def add_description(self, value: str) -> None:
        """Add description."""
        self.description.append(value)
    
    def add_endpoint_url(self, value: Union[str, URIRef]) -> Union[str, URIRef]:
        """Add endpoint URL."""
        self.endpointURL.append(value)
        return value

    def add_served_dataset(self, dataset: Dataset) -> None:
        """Add a dataset served by this service."""
        self.servesDataset.append(dataset)


class Relationship(Resource):
    """DCAT Relationship.
    
    Definition:
    An association class for attaching additional information to a relationship between DCAT Resources.
    
    References:
    - https://www.w3.org/TR/vocab-dcat-3/#Class:Relationship
    """
    rdf_type = DCAT.Relationship


# Rebuild models to handle forward references
Dataset.model_rebuild()
Catalog.model_rebuild()
CatalogRecord.model_rebuild()
DatasetSeries.model_rebuild()
Distribution.model_rebuild()
DataService.model_rebuild()
Relationship.model_rebuild()


__all__ = [
    "DCAT",
    "DcatResource",
    "Resource",
    "Dataset",
    "Catalog",
    "CatalogRecord",
    "DatasetSeries",
    "Distribution",
    "DataService",
    "Relationship",
]
