"""
DCAT is an RDF vocabulary for representing data catalogs.

DCAT is developed and maintained by the W3C

References:
- https://www.w3.org/TR/vocab-dcat-3/

"""
from dartfx.rdf import dcterms
from dartfx.rdf import foaf
from dartfx.rdf import rdf
from dartfx.rdf import spdx

from dataclasses import dataclass, field
from datetime import date, datetime
from dateutil.parser import parse
from typing import Optional
from rdflib import DCAT

@dataclass(kw_only=True)
class DcatResource(rdf.RdfResource):
    def __post_init__(self):
        if hasattr(super(), '__post_init__'):
            super().__post_init__()
        self._namespace = DCAT
        
@dataclass(kw_only=True)
class DcatClass(DcatResource):
    pass
    
@dataclass(kw_only=True)
class DcatProperty(DcatResource):
    pass


@dataclass(kw_only=True)
class Resource(DcatClass):
    """Cataloged Resource.
    
    Definition:
    Resource published or curated by a single agent.

    References:
    - https://www.w3.org/TR/vocab-dcat-3/#Class:Resource
    
    """
    accessRights: Optional[list[dcterms.AccessRights]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    conformsTo: Optional[list[dcterms.ConformsTo]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    contactPoint: Optional[list[rdf.UriOrString]] = field(default_factory=list)
    creator: Optional[list[dcterms.Creator]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    description: Optional[list[dcterms.Description]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    issued: Optional[list[dcterms.Issued]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
#has part
#has policy
    identifier: Optional[list[dcterms.Identifier]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
#is referenced by
    keyword: Optional[list[str]] = field(default_factory=list)
    landingPage: Optional[list[rdf.Url]] = field(default_factory=list)
    license: Optional[list[dcterms.License]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS}) # https://www.w3.org/TR/vocab-dcat-3/#Property:resource_license
    language: Optional[list[dcterms.Language]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS}) # https://www.w3.org/TR/vocab-dcat-3/#Property:resource_language
#relation
#qualified relation
    publisher: Optional[list[dcterms.Publisher]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
#theme/category
    title: Optional[list[dcterms.Title]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    type: Optional[list[dcterms.Type]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    modified: Optional[list[datetime]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
#qualified attribution
#has current version
#has version
#previous version
#replaces
#status
    version: Optional[str] = field(default_factory=list)
    versionNotes: Optional[list[rdf.RdfString]] = field(default_factory=list, metadata={"namespace": "http://www.w3.org/ns/adms#"})
#version notes
#first
#last
#previous

    def add_access_rights(self, value: str, lang: Optional[str] = None):
        self.accessRights.append(dcterms.AccessRights(value=value, lang=lang))

    def add_conforms_to(self, value: str, lang: Optional[str] = None):
        self.conformsTo.append(dcterms.ConformsTo(value=value, lang=lang))

    def add_creator(self, value: str):
        self.creator.append(dcterms.AccrualPeriodicity(value=value))

    def add_description(self, value: str, lang: Optional[str] = None):
        self.description.append(dcterms.Description(value=value, lang=lang))

    def add_identifier(self, value):
        self.identifier.append(dcterms.Identifier(value=value))

    def add_keyword(self, value):
        self.keyword.append(value)

    def add_language(self, value: str):
        self.language.append(dcterms.Language(value=value))

    def add_landing_page(self, value: str|rdf.Url):
        if isinstance(value, str):
            value = rdf.Url(value=value)
        self.landingPage.append(value)
        return value

    def add_license(self, value):
        self.license.append(dcterms.License(value=value))

    def add_modified_date(self, value: str|date|datetime):
        if not isinstance(value, date): # note: datetime is date
            if isinstance(value, str):
                value = parse(value)
        self.modified.append(value)
        
    def add_publisher(self, value: str):
        if isinstance(value, str):
            value = dcterms.Publisher(value=value)
        if not isinstance(value, dcterms.Publisher):
            raise TypeError(f"Expected str or dcterms.publisher, got {type(value)}")
        self.publisher.append(value)
        return value
                
    def add_release_date(self, value: str|date|datetime):
        if not isinstance(value, date): # note: datetime is date
            if isinstance(value, str):
                value = parse(value)
        self.issued.append(value)

    def add_title(self, value: str, lang: Optional[str] = None):
        self.title.append(dcterms.Title(value=value, lang=lang))


    def add_type(self, value):
        self.identifier.append(dcterms.Type(value=value))


    def add_version_notes(self, value: str, lang: Optional[str] = None):
        self.description.append(rdf.RdfString(value=value, lang=lang))

@dataclass(kw_only=True)
class Dataset(Resource):
    distribution: Optional[list["Distribution"]] = field(default_factory=list)
    accrualPeriodicity: Optional[list[dcterms.AccrualPeriodicity]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS}) # The frequency at which a dataset is published.
    inSeries: Optional[list["rdf.Uri"]] = field(default_factory=list)
    spatial: Optional[list[dcterms.Spatial]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    theme: Optional[list["rdf.Uri"]] = field(default_factory=list)
#spatial resolution
#temporal coverage
#temporal resolution
#was generated by

    def add_accrual_peridodicity(self, value: str|dcterms.AccrualPeriodicity):
        if isinstance(value, str):
            value = dcterms.AccrualPeriodicity(vaue=value)
        if not isinstance(value, dcterms.AccrualPeriodicity):
            raise TypeError(f"Expected str or dcterms.AccrualPeriodicity, got {type(value)}")
        self.accrualPeriodicity.append(dcterms.AccrualPeriodicity(value=value))
        return value

    def add_distribution(self, value: "Distribution"):
        if not isinstance(value, Distribution):
            raise TypeError(f"Expected Distribution, got {type(value)}")
        self.distribution.append(value)
        
    def add_frequency(self, value: str):
        return self.add_accrual_peridodicity(value=value)

    def add_spatial(self, value: str):
        if isinstance(value, str):
            value = dcterms.Spatial(value=value)
        if not isinstance(value, dcterms.Spatial):
            raise TypeError(f"Expected str or dcterms.Spatial, got {type(value)}")
        self.spatial.append(value)   
        return value

    def add_theme(self, value: str|rdf.Uri):
        if isinstance(value, str):
            value = rdf.Uri(value=value)
        if not isinstance(value, rdf.Uri):
            raise TypeError(f"Expected str or rdf.Uri, got {type(value)}")
        self.theme.append(value)
        return value

        
@dataclass(kw_only=True)
class Catalog(Dataset):
    homepage: Optional[list[foaf.Homepage]] = field(default_factory=list, metadata={"namespace": foaf.FOAF})
    catalogRecord: Optional[list["CatalogRecord"]] = field(default_factory=list)
    themeTaxonomy: Optional[list["rdf.Uri"]] = field(default_factory=list)
    resource: Optional[list["Resource"]] = field(default_factory=list)
    dataset: Optional[list["Dataset"]] = field(default_factory=list)
    service: Optional[list["DataService"]] = field(default_factory=list)
    catalog: Optional[list["Catalog"]] = field(default_factory=list)
    
    def add_catalog(self, value: "Catalog"):
        if not isinstance(value, Catalog):
            raise TypeError(f"Expected Catalog, got {type(value)}")
        self.catalog.append(value)
   
    def add_catalog_record(self, value: "CatalogRecord"):
        if not isinstance(value, CatalogRecord):
            raise TypeError(f"Expected CatalogRecord, got {type(value)}")
        self.catalogRecord.append(value)
   
    def add_homepage(self, value: "foaf.Homepage"):
        if not isinstance(value, foaf.Homepage):
            raise TypeError(f"Expected foaf.Homepage, got {type(value)}")
        self.homepage.append(value)
        
    def add_dataset(self, value: "Dataset"):
        if not isinstance(value, Dataset):
            raise TypeError(f"Expected Dataset, got {type(value)}")
        self.dataset.append(value)

    def add_service(self, value: "DataService"):
        if not isinstance(value, DataService):  
            raise TypeError(f"Expected DataService, got {type(value)}")
        self.service.append(value)
        
    def add_resource(self, value: "Resource"):
        if not isinstance(value, Resource):
            raise TypeError(f"Expected Resource, got {type(value)}")
        self.resource.append(value)
    
    def add_theme_taxonomy(self, value: rdf.Uri|str):
        if isinstance(value, str):
            value = rdf.Uri(value=value)
        if not isinstance(value, rdf.Uri):
            raise TypeError(f"Expected str or rdf.Uri, got {type(value)}")
        self.themeTaxonomy.append(value)
        return value
    
@dataclass(kw_only=True)
class CatalogRecord(DcatClass):
    title: Optional[list[dcterms.Title]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    description: Optional[list[dcterms.Description]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    issued: Optional[list[datetime]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})

@dataclass(kw_only=True)
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
    pass

@dataclass(kw_only=True)
class Distribution(DcatClass):
    """DCAt Distribution
        
    Definition:
    A specific representation of a dataset. A dataset might be available in multiple serializations that may differ in various ways, 
    including natural language, media-type or format, schematic organization, temporal and spatial resolution, level of detail or
    profiles (which might specify any or all of the above).
    
    Usage:
    This represents a general availability of a dataset. It implies no information about the actual access method of the data, i.e., whether by direct download, API, or through a Web page. The use of dcat:downloadURL property indicates directly downloadable distributions.
    
    References:
    - https://www.w3.org/TR/vocab-dcat-3/#Class:Distribution
    """
    pass

    accessRights: Optional[list[dcterms.AccessRights]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    accessUrl: Optional[list[rdf.Url]] = field(default_factory=list)
    accessService: Optional[list["DataService"]] = field(default_factory=list)
    byteSize: Optional[int] = field(default=None)
    checksum: Optional[list[spdx.Checksum]] = field(default_factory=list, metadata={"namespace": spdx.SPDX})
    compressionFormat: Optional[list[rdf.UriOrString]] = field(default_factory=list)
    conformsTo: Optional[list[dcterms.ConformsTo]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    description: Optional[list[dcterms.Description]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})    
    downloadURL: Optional[list[rdf.Url]] = field(default_factory=list)
    format: Optional[list[rdf.UriOrString]] = field(default_factory=list)
#has policy
    mediaType: Optional[list[rdf.UriOrString]] = field(default_factory=list)
    packagingFormat: Optional[list[rdf.UriOrString]] = field(default_factory=list)
    issued: Optional[list[datetime]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    modified: Optional[list[datetime]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    license: Optional[list[dcterms.License]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
    rights: Optional[list[dcterms.Rights]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
#spatial resolution
#temporal resolution
    title: Optional[list[dcterms.Title]] = field(default_factory=list, metadata={"namespace": dcterms.DCTERMS})
     
    def add_download_url(self, value: str|rdf.Url):
        if isinstance(value, str):
            value = rdf.Url(value=value)
        self.downloadURL.append(value)
        return value

    def add_media_type(self, value: str|rdf.UriOrString):
        if isinstance(value, str):
            value = rdf.UriOrString(value=value)
        self.mediaType.append(value)
        return value



@dataclass(kw_only=True)
class DataService(Resource):
    """ Data Service.
    
    Definition:
    A collection of operations that provides access to one or more datasets or data processing functions.
    
    Notes:
    - If a dcat:DataService is bound to one or more specified Datasets, they are indicated by the dcat:servesDataset property.
    - The kind of service can be indicated using the dcterms:type property. 
      Its value may be taken from a controlled vocabulary such as the INSPIRE spatial data service type code list [INSPIRE-SDST].
    
    
    """
    servesDataset: Optional[list[Dataset]] = field(default_factory=list) # https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_serves_dataset
    endpointURL: Optional[list[rdf.Url]] = field(default_factory=list) # https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_url
    endpointDescription: Optional[list[rdf.RdfString]] = field(default_factory=list) # https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_description


    def add_description(self, value: str):
        self.description.append(value)
    
    def add_endpoint_url(self, value: str|rdf.Url):
        if isinstance(value, str):
            value = rdf.Url(value=value)
        self.endpointURL.append(value)
        return value

    def add_served_dataset(self, dataset: Dataset):
        self.servesDataset.append(dataset)


@dataclass(kw_only=True)
class Relationship(Resource):
    pass
 #relation
 # had role.
