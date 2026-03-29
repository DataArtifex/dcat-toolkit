"""
Unit tests for DCAT core classes (Pydantic-based).

Tests the basic functionality of DCAT classes including:
- Resource creation and property addition
- Dataset creation and distribution management
- Catalog creation and dataset management
- Type validation and error handling
- RDF serialization and deserialization
"""

from datetime import datetime

import pytest
from rdflib import RDF, URIRef

from dartfx.dcat import dcat


class TestResource:
    """Test cases for the Resource class."""

    def test_create_resource(self) -> None:
        """Test basic resource creation."""
        resource = dcat.Resource(id="resource-1")
        assert resource.id == "resource-1"

    def test_add_title(self) -> None:
        """Test adding a title to a resource."""
        resource = dcat.Resource(id="resource-1")
        resource.add_title("Test Resource", lang="en")
        assert len(resource.title) == 1
        assert resource.title[0] == "Test Resource"

    def test_add_description(self) -> None:
        """Test adding a description to a resource."""
        resource = dcat.Resource(id="resource-1")
        resource.add_description("A test resource", lang="en")
        assert len(resource.description) == 1
        assert resource.description[0] == "A test resource"

    def test_add_keyword(self) -> None:
        """Test adding keywords to a resource."""
        resource = dcat.Resource(id="resource-1")
        resource.add_keyword("test")
        resource.add_keyword("example")
        assert len(resource.keyword) == 2
        assert "test" in resource.keyword
        assert "example" in resource.keyword

    def test_add_identifier(self) -> None:
        """Test adding an identifier to a resource."""
        resource = dcat.Resource(id="resource-1")
        resource.add_identifier("ID-12345")
        assert len(resource.identifier) == 1
        assert "ID-12345" in resource.identifier

    def test_add_landing_page(self) -> None:
        """Test adding a landing page URL."""
        resource = dcat.Resource(id="resource-1")
        url = resource.add_landing_page("http://example.org/page")  # noqa: F841
        assert len(resource.landingPage) == 1
        assert "http://example.org/page" in resource.landingPage

    def test_add_modified_date_string(self) -> None:
        """Test adding a modified date from string."""
        resource = dcat.Resource(id="resource-1")
        resource.add_modified_date("2024-01-15")
        assert len(resource.modified) == 1
        assert isinstance(resource.modified[0], datetime)

    def test_add_modified_date_datetime(self) -> None:
        """Test adding a modified date from datetime object."""
        resource = dcat.Resource(id="resource-1")
        now = datetime.now()
        resource.add_modified_date(now)
        assert len(resource.modified) == 1
        assert resource.modified[0] == now

    def test_add_release_date(self) -> None:
        """Test adding a release date."""
        resource = dcat.Resource(id="resource-1")
        resource.add_release_date("2024-01-01")
        assert len(resource.issued) == 1
        assert isinstance(resource.issued[0], datetime)

    def test_add_type(self) -> None:
        """Test adding a type to a resource."""
        resource = dcat.Resource(id="resource-1")
        resource.add_type("Dataset")
        assert len(resource.type) == 1


class TestDataset:
    """Test cases for the Dataset class."""

    def test_create_dataset(self) -> None:
        """Test basic dataset creation."""
        dataset = dcat.Dataset(id="dataset-1")
        assert dataset.id == "dataset-1"

    def test_add_distribution(self) -> None:
        """Test adding a distribution to a dataset."""
        dataset = dcat.Dataset(id="dataset-1")
        distribution = dcat.Distribution(id="dist-1")
        dataset.add_distribution(distribution)
        assert len(dataset.distribution) == 1
        assert dataset.distribution[0] == distribution

    def test_add_distribution_type_error(self) -> None:
        """Test that adding wrong type raises TypeError."""
        dataset = dcat.Dataset(id="dataset-1")
        with pytest.raises(TypeError):
            dataset.add_distribution("not a distribution")  # type: ignore[arg-type]

    def test_add_theme_string(self) -> None:
        """Test adding a theme from string."""
        dataset = dcat.Dataset(id="dataset-1")
        theme = dataset.add_theme("http://example.org/themes/science")  # noqa: F841
        assert len(dataset.theme) == 1
        assert "http://example.org/themes/science" in dataset.theme

    def test_add_spatial(self) -> None:
        """Test adding spatial coverage."""
        dataset = dcat.Dataset(id="dataset-1")
        spatial = dataset.add_spatial("New York")  # noqa: F841
        assert len(dataset.spatial) == 1

    def test_add_frequency(self) -> None:
        """Test adding update frequency."""
        dataset = dcat.Dataset(id="dataset-1")
        freq = dataset.add_frequency("monthly")  # noqa: F841
        assert len(dataset.accrualPeriodicity) == 1

    def test_add_accrual_periodicity_string(self) -> None:
        """Test adding accrual periodicity from string."""
        dataset = dcat.Dataset(id="dataset-1")
        period = dataset.add_accrual_periodicity("annual")  # noqa: F841
        assert len(dataset.accrualPeriodicity) == 1


class TestCatalog:
    """Test cases for the Catalog class."""

    def test_create_catalog(self) -> None:
        """Test basic catalog creation."""
        catalog = dcat.Catalog(id="catalog-1")
        assert catalog.id == "catalog-1"

    def test_add_dataset(self) -> None:
        """Test adding a dataset to a catalog."""
        catalog = dcat.Catalog(id="catalog-1")
        dataset = dcat.Dataset(id="dataset-1")
        catalog.add_dataset(dataset)
        assert len(catalog.dataset) == 1
        assert catalog.dataset[0] == dataset

    def test_add_dataset_type_error(self) -> None:
        """Test that adding wrong type raises TypeError."""
        catalog = dcat.Catalog(id="catalog-1")
        with pytest.raises(TypeError):
            catalog.add_dataset("not a dataset")  # type: ignore[arg-type]

    def test_add_service(self) -> None:
        """Test adding a data service to a catalog."""
        catalog = dcat.Catalog(id="catalog-1")
        service = dcat.DataService(id="service-1")
        catalog.add_service(service)
        assert len(catalog.service) == 1
        assert catalog.service[0] == service

    def test_add_catalog(self) -> None:
        """Test adding a sub-catalog."""
        catalog = dcat.Catalog(id="catalog-1")
        sub_catalog = dcat.Catalog(id="catalog-2")
        catalog.add_catalog(sub_catalog)
        assert len(catalog.catalog) == 1
        assert catalog.catalog[0] == sub_catalog

    def test_add_theme_taxonomy(self) -> None:
        """Test adding a theme taxonomy."""
        catalog = dcat.Catalog(id="catalog-1")
        taxonomy = catalog.add_theme_taxonomy("http://example.org/taxonomy")  # noqa: F841
        assert len(catalog.themeTaxonomy) == 1
        assert "http://example.org/taxonomy" in catalog.themeTaxonomy


class TestDistribution:
    """Test cases for the Distribution class."""

    def test_create_distribution(self) -> None:
        """Test basic distribution creation."""
        dist = dcat.Distribution(id="dist-1")
        assert dist.id == "dist-1"

    def test_add_download_url_string(self) -> None:
        """Test adding download URL from string."""
        dist = dcat.Distribution(id="dist-1")
        url = dist.add_download_url("http://example.org/data.csv")  # noqa: F841
        assert len(dist.downloadURL) == 1
        assert "http://example.org/data.csv" in dist.downloadURL

    def test_add_media_type(self) -> None:
        """Test adding media type."""
        dist = dcat.Distribution(id="dist-1")
        media = dist.add_media_type("text/csv")  # noqa: F841
        assert len(dist.mediaType) == 1


class TestDataService:
    """Test cases for the DataService class."""

    def test_create_data_service(self) -> None:
        """Test basic data service creation."""
        service = dcat.DataService(id="service-1")
        assert service.id == "service-1"

    def test_add_endpoint_url(self) -> None:
        """Test adding endpoint URL."""
        service = dcat.DataService(id="service-1")
        url = service.add_endpoint_url("http://api.example.org/v1")  # noqa: F841
        assert len(service.endpointURL) == 1
        assert "http://api.example.org/v1" in service.endpointURL

    def test_add_served_dataset(self) -> None:
        """Test adding a served dataset."""
        service = dcat.DataService(id="service-1")
        dataset = dcat.Dataset(id="dataset-1")
        service.add_served_dataset(dataset)
        assert len(service.servesDataset) == 1
        assert service.servesDataset[0] == dataset


class TestRdfSerialization:
    """Test RDF serialization and deserialization."""

    def test_resource_to_rdf(self) -> None:
        """Test serializing a resource to RDF."""
        resource = dcat.Resource(id="resource-1")
        resource.add_title("Test Resource")
        resource.add_description("A test resource")

        graph = resource.to_rdf_graph()
        assert len(graph) > 0

        # Check that the resource has the correct type
        subject = URIRef(str(dcat.DCAT) + resource.id)
        assert (subject, RDF.type, dcat.DCAT.Resource) in graph

    def test_dataset_to_rdf(self) -> None:
        """Test serializing a dataset to RDF."""
        dataset = dcat.Dataset(id="dataset-1")
        dataset.add_title("Test Dataset")
        dataset.add_keyword("test")
        dataset.add_keyword("example")

        graph = dataset.to_rdf_graph()
        subject = URIRef(str(dcat.DCAT) + dataset.id)

        # Check type
        assert (subject, RDF.type, dcat.DCAT.Dataset) in graph

    def test_catalog_with_dataset_to_rdf(self) -> None:
        """Test serializing a catalog with dataset to RDF."""
        catalog = dcat.Catalog(id="catalog-1")
        catalog.add_title("Test Catalog")

        dataset = dcat.Dataset(id="dataset-1")
        dataset.add_title("Test Dataset")
        catalog.add_dataset(dataset)

        graph = catalog.to_rdf_graph()

        # Both catalog and dataset should be in the graph
        catalog_subject = URIRef(str(dcat.DCAT) + catalog.id)
        dataset_subject = URIRef(str(dcat.DCAT) + dataset.id)

        assert (catalog_subject, RDF.type, dcat.DCAT.Catalog) in graph
        assert (dataset_subject, RDF.type, dcat.DCAT.Dataset) in graph
        assert (catalog_subject, dcat.DCAT.dataset, dataset_subject) in graph

    def test_to_turtle(self) -> None:
        """Test serializing to Turtle format."""
        dataset = dcat.Dataset(id="dataset-1")
        dataset.add_title("Test Dataset")
        dataset.add_description("A test dataset")

        turtle = dataset.to_rdf(format="turtle")
        assert "Test Dataset" in turtle
        assert "dcat:" in turtle or "http://www.w3.org/ns/dcat#" in turtle

    def test_round_trip(self) -> None:
        """Test round-trip serialization and deserialization."""
        # Create original
        original = dcat.Dataset(id="dataset-1")
        original.add_title("Test Dataset")
        original.add_description("A test dataset")
        original.add_keyword("test")

        # Serialize
        turtle = original.to_rdf(format="turtle")

        # Deserialize
        subject = URIRef(str(dcat.DCAT) + "dataset-1")
        restored = dcat.Dataset.from_rdf(turtle, format="turtle", subject=subject)

        # Verify
        assert restored.id == original.id
        assert restored.title == original.title
        assert restored.description == original.description
        assert restored.keyword == original.keyword


class TestIntegration:
    """Integration tests for complete DCAT structures."""

    def test_complete_catalog_structure(self) -> None:
        """Test creating a complete catalog with datasets and distributions."""
        # Create catalog
        catalog = dcat.Catalog(id="catalog-1")
        catalog.add_title("Test Catalog", lang="en")
        catalog.add_description("A test catalog", lang="en")

        # Create dataset
        dataset = dcat.Dataset(id="dataset-1")
        dataset.add_title("Test Dataset", lang="en")
        dataset.add_description("A test dataset", lang="en")
        dataset.add_keyword("test")
        dataset.add_theme("http://example.org/themes/testing")

        # Create distribution
        distribution = dcat.Distribution(id="dist-1")
        distribution.title.append("CSV Distribution")
        distribution.add_download_url("http://example.org/data.csv")
        distribution.add_media_type("text/csv")

        # Link everything together
        dataset.add_distribution(distribution)
        catalog.add_dataset(dataset)

        # Verify structure
        assert len(catalog.dataset) == 1
        assert len(catalog.dataset[0].distribution) == 1
        assert "http://example.org/data.csv" in catalog.dataset[0].distribution[0].downloadURL

    def test_catalog_with_service(self) -> None:
        """Test creating a catalog with a data service."""
        catalog = dcat.Catalog(id="catalog-1")

        dataset = dcat.Dataset(id="dataset-1")
        dataset.add_title("API Dataset", lang="en")

        service = dcat.DataService(id="service-1")
        service.add_title("Data API", lang="en")
        service.add_endpoint_url("http://api.example.org/v1")
        service.add_served_dataset(dataset)

        catalog.add_dataset(dataset)
        catalog.add_service(service)

        assert len(catalog.dataset) == 1
        assert len(catalog.service) == 1
        assert catalog.service[0].servesDataset[0] == dataset

    def test_complete_rdf_serialization(self) -> None:
        """Test complete RDF serialization of a catalog structure."""
        # Build structure
        catalog = dcat.Catalog(id="catalog-1")
        catalog.add_title("My Catalog")

        dataset = dcat.Dataset(id="dataset-1")
        dataset.add_title("My Dataset")
        dataset.add_keyword("test")

        distribution = dcat.Distribution(id="dist-1")
        distribution.add_download_url("http://example.org/data.csv")

        dataset.add_distribution(distribution)
        catalog.add_dataset(dataset)

        # Serialize
        graph = catalog.to_rdf_graph()

        # Verify all components are in the graph
        assert len(graph) > 0

        # Check subjects exist
        catalog_uri = URIRef(str(dcat.DCAT) + "catalog-1")
        dataset_uri = URIRef(str(dcat.DCAT) + "dataset-1")
        dist_uri = URIRef(str(dcat.DCAT) + "dist-1")

        assert (catalog_uri, RDF.type, dcat.DCAT.Catalog) in graph
        assert (dataset_uri, RDF.type, dcat.DCAT.Dataset) in graph
        assert (dist_uri, RDF.type, dcat.DCAT.Distribution) in graph
