"""
Unit tests for DCAT-AP HVD classes (Pydantic-based).

Tests the DCAT-AP HVD extensions including:
- HVD Dataset
- HVD Distribution
- HVD DataService
- HVD DatasetSeries
- HVD compliance helpers
- HVD categories
- HVD licences
"""

import pytest
from rdflib import Graph, URIRef, RDF
from dartfx.dcat import dcat_ap_hvd


class TestHVDCategory:
    """Test cases for HVD categories."""
    
    def test_all_categories_exist(self):
        """Test that all 6 HVD categories are defined."""
        categories = dcat_ap_hvd.HVDCategory.all_categories()
        assert len(categories) == 6
        assert dcat_ap_hvd.HVDCategory.GEOSPATIAL in categories
        assert dcat_ap_hvd.HVDCategory.EARTH_OBSERVATION in categories
        assert dcat_ap_hvd.HVDCategory.ENVIRONMENT in categories
        assert dcat_ap_hvd.HVDCategory.METEOROLOGICAL in categories
        assert dcat_ap_hvd.HVDCategory.STATISTICS in categories
        assert dcat_ap_hvd.HVDCategory.COMPANIES in categories
    
    def test_is_valid_category(self):
        """Test category validation."""
        assert dcat_ap_hvd.HVDCategory.is_valid_category(
            dcat_ap_hvd.HVDCategory.GEOSPATIAL
        )
        assert not dcat_ap_hvd.HVDCategory.is_valid_category(
            "http://invalid.category"
        )


class TestHVDLicence:
    """Test cases for HVD licences."""
    
    def test_hvd_compliant_licences(self):
        """Test HVD-compliant licence URIs."""
        assert dcat_ap_hvd.HVDLicence.is_hvd_compliant(
            dcat_ap_hvd.HVDLicence.CC_BY_4_0
        )
        assert dcat_ap_hvd.HVDLicence.is_hvd_compliant(
            dcat_ap_hvd.HVDLicence.CC0_1_0
        )
        assert dcat_ap_hvd.HVDLicence.is_hvd_compliant(
            dcat_ap_hvd.HVDLicence.EU_NO_RESTRICTIONS
        )
    
    def test_non_compliant_licence(self):
        """Test non-HVD-compliant licence."""
        assert not dcat_ap_hvd.HVDLicence.is_hvd_compliant(
            "http://example.org/restrictive-licence"
        )


class TestHVDDataset:
    """Test cases for HVD Dataset."""
    
    def test_create_hvd_dataset(self):
        """Test creating an HVD dataset."""
        dataset = dcat_ap_hvd.Dataset(id="hvd-dataset-1")
        dataset.add_title("HVD Geospatial Dataset")
        assert dataset.id == "hvd-dataset-1"
    
    def test_add_hvd_category(self):
        """Test adding HVD category."""
        dataset = dcat_ap_hvd.Dataset(id="hvd-dataset-1")
        category = dataset.add_hvd_category(dcat_ap_hvd.HVDCategory.GEOSPATIAL)
        assert len(dataset.hvdCategory) == 1
        assert category in dataset.hvdCategory
    
    def test_make_hvd_compliant(self):
        """Test making dataset HVD-compliant."""
        dataset = dcat_ap_hvd.Dataset(id="hvd-dataset-1")
        dataset.make_hvd_compliant(dcat_ap_hvd.HVDCategory.GEOSPATIAL)
        
        # Check HVD regulation added
        assert dcat_ap_hvd.HVD_REGULATION in dataset.applicableLegislation
        
        # Check HVD category added
        assert dcat_ap_hvd.HVDCategory.GEOSPATIAL in dataset.hvdCategory
    
    def test_is_hvd_compliant(self):
        """Test HVD compliance check."""
        dataset = dcat_ap_hvd.Dataset(id="hvd-dataset-1")
        
        # Not compliant initially
        assert not dataset.is_hvd_compliant()
        
        # Make compliant
        dataset.make_hvd_compliant(dcat_ap_hvd.HVDCategory.STATISTICS)
        
        # Now compliant
        assert dataset.is_hvd_compliant()
    
    def test_complete_hvd_dataset(self):
        """Test creating a complete HVD-compliant dataset."""
        dataset = dcat_ap_hvd.Dataset(id="hvd-geo-1")
        dataset.add_title("European Geospatial Data", lang="en")
        dataset.add_description("High Value geospatial dataset", lang="en")
        
        # Make HVD compliant
        dataset.make_hvd_compliant(dcat_ap_hvd.HVDCategory.GEOSPATIAL)
        
        # Add contact point (mandatory for HVD)
        dataset.add_contact_point("http://example.org/contact")
        
        # Add conforms to (for specific data requirements)
        dataset.add_conforms_to("http://example.org/standard/geospatial")
        
        # Verify compliance
        assert dataset.is_hvd_compliant()
        assert len(dataset.contactPoint) > 0


class TestHVDDistribution:
    """Test cases for HVD Distribution."""
    
    def test_create_hvd_distribution(self):
        """Test creating an HVD distribution."""
        dist = dcat_ap_hvd.Distribution(id="hvd-dist-1")
        assert dist.id == "hvd-dist-1"
    
    def test_make_hvd_compliant(self):
        """Test making distribution HVD-compliant."""
        dist = dcat_ap_hvd.Distribution(id="hvd-dist-1")
        dist.make_hvd_compliant()
        
        # Check HVD regulation added
        assert dcat_ap_hvd.HVD_REGULATION in dist.applicableLegislation
    
    def test_is_hvd_compliant(self):
        """Test HVD compliance check for distribution."""
        dist = dcat_ap_hvd.Distribution(id="hvd-dist-1")
        
        # Not compliant initially
        assert not dist.is_hvd_compliant()
        
        # Add required properties
        dist.make_hvd_compliant()
        dist.add_access_url("http://example.org/data.csv")
        dist.add_license(dcat_ap_hvd.HVDLicence.CC_BY_4_0)
        
        # Now compliant
        assert dist.is_hvd_compliant()
    
    def test_complete_hvd_distribution(self):
        """Test creating a complete HVD-compliant distribution."""
        dist = dcat_ap_hvd.Distribution(id="hvd-dist-1")
        
        # Make HVD compliant
        dist.make_hvd_compliant()
        
        # Add mandatory properties
        dist.add_access_url("http://example.org/data.csv")
        dist.add_download_url("http://example.org/data.csv")
        dist.add_license(dcat_ap_hvd.HVDLicence.CC_BY_4_0)
        dist.add_media_type("text/csv")
        
        # Verify compliance
        assert dist.is_hvd_compliant()


class TestHVDDataService:
    """Test cases for HVD Data Service."""
    
    def test_create_hvd_data_service(self):
        """Test creating an HVD data service."""
        service = dcat_ap_hvd.DataService(id="hvd-api-1")
        service.add_title("HVD Geospatial API")
        assert service.id == "hvd-api-1"
    
    def test_add_hvd_category(self):
        """Test adding HVD category to data service."""
        service = dcat_ap_hvd.DataService(id="hvd-api-1")
        category = service.add_hvd_category(dcat_ap_hvd.HVDCategory.METEOROLOGICAL)
        assert len(service.hvdCategory) == 1
        assert category in service.hvdCategory
    
    def test_make_hvd_compliant(self):
        """Test making data service HVD-compliant."""
        service = dcat_ap_hvd.DataService(id="hvd-api-1")
        service.make_hvd_compliant(dcat_ap_hvd.HVDCategory.ENVIRONMENT)
        
        # Check HVD regulation added
        assert dcat_ap_hvd.HVD_REGULATION in service.applicableLegislation
        
        # Check HVD category added
        assert dcat_ap_hvd.HVDCategory.ENVIRONMENT in service.hvdCategory
    
    def test_is_hvd_compliant(self):
        """Test HVD compliance check for data service."""
        service = dcat_ap_hvd.DataService(id="hvd-api-1")
        
        # Not compliant initially
        assert not service.is_hvd_compliant()
        
        # Make compliant
        service.make_hvd_compliant(dcat_ap_hvd.HVDCategory.COMPANIES)
        service.add_endpoint_url("https://api.example.org/companies")
        
        # Now compliant
        assert service.is_hvd_compliant()


class TestHVDDatasetSeries:
    """Test cases for HVD Dataset Series."""
    
    def test_create_hvd_dataset_series(self):
        """Test creating an HVD dataset series."""
        series = dcat_ap_hvd.DatasetSeries(id="hvd-series-1")
        series.add_title("HVD Statistical Series")
        assert series.id == "hvd-series-1"
    
    def test_make_hvd_compliant(self):
        """Test making dataset series HVD-compliant."""
        series = dcat_ap_hvd.DatasetSeries(id="hvd-series-1")
        series.make_hvd_compliant(dcat_ap_hvd.HVDCategory.STATISTICS)
        
        # Check HVD regulation added
        assert dcat_ap_hvd.HVD_REGULATION in series.applicableLegislation
        
        # Check HVD category added
        assert dcat_ap_hvd.HVDCategory.STATISTICS in series.hvdCategory


class TestRdfSerialization:
    """Test RDF serialization for HVD classes."""
    
    def test_dataset_to_turtle(self):
        """Test serializing HVD dataset to Turtle."""
        dataset = dcat_ap_hvd.Dataset(id="hvd-dataset-1")
        dataset.add_title("HVD Dataset")
        dataset.make_hvd_compliant(dcat_ap_hvd.HVDCategory.GEOSPATIAL)
        
        turtle = dataset.to_rdf(format="turtle")
        assert "dcat:" in turtle or "http://www.w3.org/ns/dcat#" in turtle
        assert "hvdCategory" in turtle or "http://data.europa.eu/r5r/hvdCategory" in turtle
    
    def test_round_trip(self):
        """Test round-trip serialization."""
        # Create original
        original = dcat_ap_hvd.Dataset(id="hvd-dataset-1")
        original.add_title("Test HVD Dataset")
        original.make_hvd_compliant(dcat_ap_hvd.HVDCategory.EARTH_OBSERVATION)
        
        # Serialize
        turtle = original.to_rdf(format="turtle")
        
        # Deserialize
        from dartfx.dcat.dcat import DCAT
        subject = URIRef(str(DCAT) + "hvd-dataset-1")
        restored = dcat_ap_hvd.Dataset.from_rdf(turtle, format="turtle", subject=subject)
        
        # Verify
        assert restored.id == original.id
        assert restored.title == original.title


class TestCompleteHVDExample:
    """Integration test for complete HVD structure."""
    
    def test_complete_hvd_catalog(self):
        """Test creating a complete HVD-compliant catalog."""
        # Create catalog
        catalog = dcat_ap_hvd.Catalog(id="hvd-catalog")
        catalog.add_title("European HVD Catalog", lang="en")
        catalog.add_description("Catalog of High Value Datasets", lang="en")
        
        # Create HVD dataset
        dataset = dcat_ap_hvd.Dataset(id="hvd-geo-1")
        dataset.add_title("Geospatial HVD Dataset", lang="en")
        dataset.add_description("High Value geospatial data", lang="en")
        
        # Make dataset HVD-compliant
        dataset.make_hvd_compliant(dcat_ap_hvd.HVDCategory.GEOSPATIAL)
        
        # Add contact point (mandatory for HVD)
        dataset.add_contact_point("http://example.org/contact")
        
        # Create bulk download distribution
        bulk_dist = dcat_ap_hvd.Distribution(id="bulk-download")
        bulk_dist.make_hvd_compliant()
        bulk_dist.add_download_url("http://example.org/bulk-data.zip")
        bulk_dist.add_license(dcat_ap_hvd.HVDLicence.CC_BY_4_0)
        bulk_dist.add_media_type("application/zip")
        
        # Create API data service (mandatory for HVD)
        api_service = dcat_ap_hvd.DataService(id="hvd-api")
        api_service.add_title("Geospatial API", lang="en")
        api_service.make_hvd_compliant(dcat_ap_hvd.HVDCategory.GEOSPATIAL)
        api_service.add_endpoint_url("https://api.example.org/geospatial")
        api_service.add_contact_point("http://example.org/contact")
        
        # Create API distribution
        api_dist = dcat_ap_hvd.Distribution(id="api-access")
        api_dist.make_hvd_compliant()
        api_dist.add_access_url("https://api.example.org/geospatial")
        api_dist.add_license(dcat_ap_hvd.HVDLicence.CC_BY_4_0)
        api_dist.add_access_service(api_service)
        
        # Link everything
        dataset.add_distribution(bulk_dist)
        dataset.add_distribution(api_dist)
        catalog.add_dataset(dataset)
        catalog.add_service(api_service)
        
        # Verify HVD compliance
        assert dataset.is_hvd_compliant()
        assert bulk_dist.is_hvd_compliant()
        assert api_dist.is_hvd_compliant()
        assert api_service.is_hvd_compliant()
        
        # Verify structure
        assert len(catalog.dataset) == 1
        assert len(catalog.service) == 1
        assert len(dataset.distribution) == 2
    
    def test_hvd_with_multiple_categories(self):
        """Test HVD dataset with multiple categories."""
        dataset = dcat_ap_hvd.Dataset(id="multi-category")
        dataset.add_title("Multi-category HVD Dataset")
        
        # Add HVD regulation
        dataset.add_applicable_legislation(dcat_ap_hvd.HVD_REGULATION)
        
        # Add multiple HVD categories
        dataset.add_hvd_category(dcat_ap_hvd.HVDCategory.GEOSPATIAL)
        dataset.add_hvd_category(dcat_ap_hvd.HVDCategory.ENVIRONMENT)
        
        # Verify
        assert dataset.is_hvd_compliant()
        assert len(dataset.hvdCategory) == 2
    
    def test_serialize_complete_hvd_structure(self):
        """Test serializing complete HVD structure to RDF."""
        # Create minimal HVD structure
        catalog = dcat_ap_hvd.Catalog(id="hvd-catalog")
        catalog.add_title("HVD Catalog")
        
        dataset = dcat_ap_hvd.Dataset(id="hvd-dataset")
        dataset.add_title("HVD Dataset")
        dataset.make_hvd_compliant(dcat_ap_hvd.HVDCategory.STATISTICS)
        dataset.add_contact_point("http://example.org/contact")
        
        distribution = dcat_ap_hvd.Distribution(id="hvd-dist")
        distribution.make_hvd_compliant()
        distribution.add_access_url("http://example.org/data")
        distribution.add_license(dcat_ap_hvd.HVDLicence.CC0_1_0)
        
        dataset.add_distribution(distribution)
        catalog.add_dataset(dataset)
        
        # Serialize to RDF
        graph = catalog.to_rdf_graph()
        
        # Verify graph contains HVD-specific triples
        assert len(graph) > 0
        
        # Serialize to different formats
        turtle = catalog.to_rdf(format='turtle')
        xml = catalog.to_rdf(format='xml')
        jsonld = catalog.to_rdf(format='json-ld')
        
        assert len(turtle) > 0
        assert len(xml) > 0
        assert len(jsonld) > 0


class TestHVDRegulation:
    """Test HVD regulation constant."""
    
    def test_hvd_regulation_uri(self):
        """Test HVD regulation URI."""
        assert dcat_ap_hvd.HVD_REGULATION == "http://data.europa.eu/eli/reg_impl/2023/138/oj"
    
    def test_dataset_with_hvd_regulation(self):
        """Test adding HVD regulation to dataset."""
        dataset = dcat_ap_hvd.Dataset(id="test")
        dataset.add_applicable_legislation(dcat_ap_hvd.HVD_REGULATION)
        
        assert dcat_ap_hvd.HVD_REGULATION in dataset.applicableLegislation
