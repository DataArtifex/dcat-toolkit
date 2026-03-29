"""
Unit tests for DCAT-AP classes (Pydantic-based).

Tests the DCAT-AP 3.0.1 extensions including:
- Extended Catalog
- Extended Dataset
- Extended Distribution
- Extended DataService
- Extended DatasetSeries
- Extended CatalogRecord
- Controlled Vocabularies
- High Value Datasets (HVD)
"""

from rdflib import RDF, URIRef

from dartfx.dcat import dcat_ap
from dartfx.dcat.dcat import DCAT


class TestCatalog:
    """Test cases for the DCAT-AP Catalog class."""

    def test_create_catalog(self) -> None:
        """Test basic DCAT-AP catalog creation."""
        catalog = dcat_ap.Catalog(id="catalog-1")
        catalog.add_title("European Data Catalog")
        assert catalog.id == "catalog-1"
        assert "European Data Catalog" in catalog.title

    def test_add_applicable_legislation(self) -> None:
        """Test adding applicable legislation (HVD)."""
        catalog = dcat_ap.Catalog(id="catalog-1")
        hvd_reg = catalog.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")
        assert len(catalog.applicableLegislation) == 1
        assert hvd_reg in catalog.applicableLegislation

    def test_add_geographical_coverage(self) -> None:
        """Test adding geographical coverage."""
        catalog = dcat_ap.Catalog(id="catalog-1")
        coverage = catalog.add_geographical_coverage("http://publications.europa.eu/resource/authority/country/DEU")  # noqa: F841
        assert len(catalog.spatial) == 1

    def test_catalog_to_rdf(self) -> None:
        """Test serializing DCAT-AP catalog to RDF."""
        catalog = dcat_ap.Catalog(id="catalog-1")
        catalog.add_title("Test Catalog")
        catalog.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")

        graph = catalog.to_rdf_graph()
        assert len(graph) > 0


class TestDataset:
    """Test cases for the DCAT-AP Dataset class."""

    def test_create_dataset(self) -> None:
        """Test basic DCAT-AP dataset creation."""
        dataset = dcat_ap.Dataset(id="dataset-1")
        dataset.add_title("European Dataset")
        assert dataset.id == "dataset-1"
        assert "European Dataset" in dataset.title

    def test_add_applicable_legislation(self) -> None:
        """Test adding applicable legislation (HVD)."""
        dataset = dcat_ap.Dataset(id="dataset-1")
        hvd_reg = dataset.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")  # noqa: F841
        assert len(dataset.applicableLegislation) == 1

    def test_set_access_rights(self) -> None:
        """Test setting access rights with EU vocabulary."""
        dataset = dcat_ap.Dataset(id="dataset-1")
        access = dataset.set_access_rights("http://publications.europa.eu/resource/authority/access-right/PUBLIC")
        assert dataset.accessRights == access

    def test_add_provenance(self) -> None:
        """Test adding provenance statement."""
        dataset = dcat_ap.Dataset(id="dataset-1")
        prov = dataset.add_provenance("http://example.org/provenance/1")  # noqa: F841
        assert len(dataset.provenance) == 1

    def test_add_qualified_attribution(self) -> None:
        """Test adding qualified attribution."""
        dataset = dcat_ap.Dataset(id="dataset-1")
        attr = dataset.add_qualified_attribution("http://example.org/attribution/1")  # noqa: F841
        assert len(dataset.qualifiedAttribution) == 1

    def test_add_other_identifier(self) -> None:
        """Test adding ADMS identifier."""
        dataset = dcat_ap.Dataset(id="dataset-1")
        ident = dataset.add_other_identifier("http://example.org/identifier/alt-1")  # noqa: F841
        assert len(dataset.otherIdentifier) == 1

    def test_dataset_to_rdf(self) -> None:
        """Test serializing DCAT-AP dataset to RDF."""
        dataset = dcat_ap.Dataset(id="dataset-1")
        dataset.add_title("Test Dataset")
        dataset.set_access_rights("http://publications.europa.eu/resource/authority/access-right/PUBLIC")

        graph = dataset.to_rdf_graph()
        assert len(graph) > 0


class TestDistribution:
    """Test cases for the DCAT-AP Distribution class."""

    def test_create_distribution(self) -> None:
        """Test basic DCAT-AP distribution creation."""
        dist = dcat_ap.Distribution(id="dist-1")
        dist.title.append("European Distribution")
        assert dist.id == "dist-1"

    def test_add_applicable_legislation(self) -> None:
        """Test adding applicable legislation (HVD)."""
        dist = dcat_ap.Distribution(id="dist-1")
        hvd_reg = dist.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")  # noqa: F841
        assert len(dist.applicableLegislation) == 1

    def test_set_availability(self) -> None:
        """Test setting planned availability."""
        dist = dcat_ap.Distribution(id="dist-1")
        avail = dist.set_availability("http://publications.europa.eu/resource/authority/planned-availability/AVAILABLE")
        assert dist.availability == avail

    def test_add_policy(self) -> None:
        """Test adding ODRL policy."""
        dist = dcat_ap.Distribution(id="dist-1")
        policy = dist.add_policy("http://example.org/policy/1")  # noqa: F841
        assert len(dist.hasPolicy) == 1

    def test_set_status(self) -> None:
        """Test setting distribution status."""
        dist = dcat_ap.Distribution(id="dist-1")
        status = dist.set_status("http://publications.europa.eu/resource/authority/distribution-status/COMPLETED")
        assert dist.status == status

    def test_distribution_to_rdf(self) -> None:
        """Test serializing DCAT-AP distribution to RDF."""
        dist = dcat_ap.Distribution(id="dist-1")
        dist.add_download_url("http://example.org/data.csv")
        dist.set_availability("http://publications.europa.eu/resource/authority/planned-availability/AVAILABLE")

        graph = dist.to_rdf_graph()
        assert len(graph) > 0


class TestDataService:
    """Test cases for the DCAT-AP DataService class."""

    def test_create_data_service(self) -> None:
        """Test basic DCAT-AP data service creation."""
        service = dcat_ap.DataService(id="service-1")
        service.add_title("European Data Service")
        assert service.id == "service-1"

    def test_add_applicable_legislation(self) -> None:
        """Test adding applicable legislation (HVD)."""
        service = dcat_ap.DataService(id="service-1")
        hvd_reg = service.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")  # noqa: F841
        assert len(service.applicableLegislation) == 1


class TestDatasetSeries:
    """Test cases for the DCAT-AP DatasetSeries class."""

    def test_create_dataset_series(self) -> None:
        """Test basic DCAT-AP dataset series creation."""
        series = dcat_ap.DatasetSeries(id="series-1")
        series.add_title("European Dataset Series")
        assert series.id == "series-1"

    def test_add_applicable_legislation(self) -> None:
        """Test adding applicable legislation (HVD)."""
        series = dcat_ap.DatasetSeries(id="series-1")
        hvd_reg = series.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")  # noqa: F841
        assert len(series.applicableLegislation) == 1

    def test_set_access_rights(self) -> None:
        """Test setting access rights."""
        series = dcat_ap.DatasetSeries(id="series-1")
        access = series.set_access_rights("http://publications.europa.eu/resource/authority/access-right/PUBLIC")
        assert series.accessRights == access


class TestCatalogRecord:
    """Test cases for the DCAT-AP CatalogRecord class."""

    def test_create_catalog_record(self) -> None:
        """Test basic DCAT-AP catalog record creation."""
        record = dcat_ap.CatalogRecord(id="record-1")
        record.title.append("Test Record")
        assert record.id == "record-1"

    def test_add_applicable_legislation(self) -> None:
        """Test adding applicable legislation (HVD)."""
        record = dcat_ap.CatalogRecord(id="record-1")
        hvd_reg = record.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")  # noqa: F841
        assert len(record.applicableLegislation) == 1


class TestControlledVocabularies:
    """Test cases for controlled vocabularies."""

    def test_controlled_vocabularies_exist(self) -> None:
        """Test that controlled vocabulary constants are defined."""
        assert dcat_ap.ControlledVocabularies.IANA_MEDIA_TYPES
        assert dcat_ap.ControlledVocabularies.EU_FREQUENCY
        assert dcat_ap.ControlledVocabularies.EU_FILE_TYPE
        assert dcat_ap.ControlledVocabularies.EU_DATA_THEME
        assert dcat_ap.ControlledVocabularies.EU_ACCESS_RIGHT

    def test_hvd_categories_exist(self) -> None:
        """Test that HVD category constants are defined."""
        assert dcat_ap.HVDCategory.GEOSPATIAL
        assert dcat_ap.HVDCategory.EARTH_OBSERVATION
        assert dcat_ap.HVDCategory.ENVIRONMENT
        assert dcat_ap.HVDCategory.METEOROLOGICAL
        assert dcat_ap.HVDCategory.STATISTICS
        assert dcat_ap.HVDCategory.COMPANIES


class TestHVDCompliance:
    """Test cases for High Value Datasets compliance."""

    def test_hvd_dataset(self) -> None:
        """Test creating an HVD-compliant dataset."""
        dataset = dcat_ap.Dataset(id="hvd-dataset-1")
        dataset.add_title("Geospatial HVD Dataset")
        dataset.add_description("High Value Dataset for geospatial data")

        # Add HVD regulation
        dataset.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")

        # Add HVD category
        dataset.add_theme(dcat_ap.HVDCategory.GEOSPATIAL)

        # Set access rights to PUBLIC (required for HVD)
        dataset.set_access_rights("http://publications.europa.eu/resource/authority/access-right/PUBLIC")

        assert len(dataset.applicableLegislation) == 1
        assert dcat_ap.HVDCategory.GEOSPATIAL in dataset.theme

    def test_hvd_distribution(self) -> None:
        """Test creating an HVD-compliant distribution."""
        dist = dcat_ap.Distribution(id="hvd-dist-1")
        dist.add_download_url("http://example.org/hvd-data.csv")

        # Add HVD regulation
        dist.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")

        # Set availability
        dist.set_availability("http://publications.europa.eu/resource/authority/planned-availability/AVAILABLE")

        # Set format using EU file type
        dist.add_media_type("text/csv")

        assert len(dist.applicableLegislation) == 1
        assert dist.availability is not None


class TestRdfSerialization:
    """Test RDF serialization for DCAT-AP classes."""

    def test_to_turtle(self) -> None:
        """Test serializing to Turtle format."""
        dataset = dcat_ap.Dataset(id="dataset-1")
        dataset.add_title("European Dataset")
        dataset.set_access_rights("http://publications.europa.eu/resource/authority/access-right/PUBLIC")

        turtle = dataset.to_rdf(format="turtle")
        assert "dcat:" in turtle or "http://www.w3.org/ns/dcat#" in turtle

    def test_round_trip(self) -> None:
        """Test round-trip serialization and deserialization."""
        # Create original
        original = dcat_ap.Dataset(id="dataset-1")
        original.add_title("Test Dataset")
        original.set_access_rights("http://publications.europa.eu/resource/authority/access-right/PUBLIC")

        # Serialize
        turtle = original.to_rdf(format="turtle")

        # Deserialize
        subject = URIRef(str(DCAT) + "dataset-1")
        restored = dcat_ap.Dataset.from_rdf(turtle, format="turtle", subject=subject)

        # Verify
        assert restored.id == original.id
        assert restored.title == original.title


class TestIntegration:
    """Integration tests for DCAT-AP structures."""

    def test_complete_catalog_structure(self) -> None:
        """Test creating a complete DCAT-AP catalog with HVD datasets."""
        # Create catalog
        catalog = dcat_ap.Catalog(id="eu-catalog")
        catalog.add_title("European Open Data Portal", lang="en")
        catalog.add_description("Catalog of European open datasets", lang="en")
        catalog.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")

        # Create HVD dataset
        dataset = dcat_ap.Dataset(id="hvd-geo-1")
        dataset.add_title("Geospatial Dataset", lang="en")
        dataset.add_description("High Value geospatial data", lang="en")
        dataset.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")
        dataset.add_theme(dcat_ap.HVDCategory.GEOSPATIAL)
        dataset.set_access_rights("http://publications.europa.eu/resource/authority/access-right/PUBLIC")

        # Create distribution
        dist = dcat_ap.Distribution(id="dist-1")
        dist.add_download_url("http://example.org/data.csv")
        dist.add_media_type("text/csv")
        dist.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")
        dist.set_availability("http://publications.europa.eu/resource/authority/planned-availability/AVAILABLE")

        # Link everything together
        dataset.add_distribution(dist)
        catalog.add_dataset(dataset)

        # Verify structure
        assert len(catalog.dataset) == 1
        assert len(catalog.dataset[0].distribution) == 1
        assert len(catalog.applicableLegislation) == 1

    def test_multiple_rdf_serialization(self) -> None:
        """Test serializing multiple DCAT-AP objects to RDF."""
        # Create objects
        catalog = dcat_ap.Catalog(id="catalog-1")
        catalog.add_title("Test Catalog")

        dataset = dcat_ap.Dataset(id="dataset-1")
        dataset.add_title("Test Dataset")
        dataset.set_access_rights("http://publications.europa.eu/resource/authority/access-right/PUBLIC")

        catalog.add_dataset(dataset)

        # Serialize to same graph
        graph = catalog.to_rdf_graph()

        # Verify both are in the graph
        catalog_uri = URIRef(str(DCAT) + "catalog-1")
        dataset_uri = URIRef(str(DCAT) + "dataset-1")

        assert (catalog_uri, RDF.type, DCAT.Catalog) in graph
        assert (dataset_uri, RDF.type, DCAT.Dataset) in graph
