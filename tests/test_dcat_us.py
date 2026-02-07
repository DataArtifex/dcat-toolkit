"""
Unit tests for DCAT-US classes (Pydantic-based).

Tests the DCAT-US 3.0 specific classes including:
- AccessRestriction
- CuiRestriction
- GeographicBoundingBox
- LiabilityStatement
- UseRestriction
"""

import pytest
from decimal import Decimal
from rdflib import Graph, URIRef, RDF
from dartfx.dcat import dcat_us


class TestAccessRestriction:
    """Test cases for the AccessRestriction class."""
    
    def test_create_access_restriction(self):
        """Test basic access restriction creation."""
        restriction = dcat_us.AccessRestriction(
            id="access-restriction-1",
            restrictionStatus="http://example.org/status/restricted"
        )
        assert restriction.id == "access-restriction-1"
        assert restriction.restrictionStatus == "http://example.org/status/restricted"
    
    def test_access_restriction_with_optional_fields(self):
        """Test access restriction with optional fields."""
        restriction = dcat_us.AccessRestriction(
            id="access-restriction-2",
            restrictionStatus="http://example.org/status/restricted",
            specificRestriction="http://example.org/restriction/classified",
            restrictionNote="This record is classified"
        )
        assert restriction.specificRestriction == "http://example.org/restriction/classified"
        assert restriction.restrictionNote == "This record is classified"
    
    def test_access_restriction_to_rdf(self):
        """Test serializing access restriction to RDF."""
        restriction = dcat_us.AccessRestriction(
            id="access-restriction-1",
            restrictionStatus="http://example.org/status/restricted"
        )
        
        graph = restriction.to_rdf_graph()
        assert len(graph) > 0
        
        # Check that the restriction has the correct type
        subject = URIRef(str(dcat_us.DCAT_US) + restriction.id)
        assert (subject, RDF.type, dcat_us.DCAT_US.AccessRestriction) in graph


class TestCuiRestriction:
    """Test cases for the CuiRestriction class."""
    
    def test_create_cui_restriction(self):
        """Test basic CUI restriction creation."""
        cui = dcat_us.CuiRestriction(
            id="cui-1",
            cuiBannerMarking="CUI",
            designationIndicator="CUI//SP-PRVCY"
        )
        assert cui.id == "cui-1"
        assert cui.cuiBannerMarking == "CUI"
        assert cui.designationIndicator == "CUI//SP-PRVCY"
    
    def test_cui_restriction_with_optional_field(self):
        """Test CUI restriction with optional field."""
        cui = dcat_us.CuiRestriction(
            id="cui-2",
            cuiBannerMarking="CUI",
            designationIndicator="CUI//SP-PRVCY",
            requiredIndicatorPerAuthority="Additional authority info"
        )
        assert cui.requiredIndicatorPerAuthority == "Additional authority info"
    
    def test_cui_restriction_to_rdf(self):
        """Test serializing CUI restriction to RDF."""
        cui = dcat_us.CuiRestriction(
            id="cui-1",
            cuiBannerMarking="CUI",
            designationIndicator="CUI//SP-PRVCY"
        )
        
        graph = cui.to_rdf_graph()
        assert len(graph) > 0
        
        subject = URIRef(str(dcat_us.DCAT_US) + cui.id)
        assert (subject, RDF.type, dcat_us.DCAT_US.CuiRestriction) in graph


class TestGeographicBoundingBox:
    """Test cases for the GeographicBoundingBox class."""
    
    def test_create_bounding_box(self):
        """Test basic bounding box creation."""
        bbox = dcat_us.GeographicBoundingBox(
            id="bbox-1",
            westBoundingLongitude=Decimal("-180.0"),
            eastBoundingLongitude=Decimal("180.0"),
            northBoundingLatitude=Decimal("90.0"),
            southBoundingLatitude=Decimal("-90.0")
        )
        assert bbox.id == "bbox-1"
        assert bbox.westBoundingLongitude == Decimal("-180.0")
        assert bbox.eastBoundingLongitude == Decimal("180.0")
        assert bbox.northBoundingLatitude == Decimal("90.0")
        assert bbox.southBoundingLatitude == Decimal("-90.0")
    
    def test_bounding_box_us_example(self):
        """Test bounding box with US coordinates."""
        bbox = dcat_us.GeographicBoundingBox(
            id="bbox-us",
            westBoundingLongitude=Decimal("-125.0"),
            eastBoundingLongitude=Decimal("-66.0"),
            northBoundingLatitude=Decimal("49.0"),
            southBoundingLatitude=Decimal("24.0")
        )
        assert bbox.westBoundingLongitude == Decimal("-125.0")
        assert bbox.eastBoundingLongitude == Decimal("-66.0")
    
    def test_bounding_box_to_rdf(self):
        """Test serializing bounding box to RDF."""
        bbox = dcat_us.GeographicBoundingBox(
            id="bbox-1",
            westBoundingLongitude=Decimal("-180.0"),
            eastBoundingLongitude=Decimal("180.0"),
            northBoundingLatitude=Decimal("90.0"),
            southBoundingLatitude=Decimal("-90.0")
        )
        
        graph = bbox.to_rdf_graph()
        assert len(graph) > 0
        
        subject = URIRef(str(dcat_us.DCAT_US) + bbox.id)
        assert (subject, RDF.type, dcat_us.DCAT_US.GeographicBoundingBox) in graph


class TestLiabilityStatement:
    """Test cases for the LiabilityStatement class."""
    
    def test_create_liability_statement(self):
        """Test basic liability statement creation."""
        statement = dcat_us.LiabilityStatement(id="liability-1")
        assert statement.id == "liability-1"
        assert len(statement.label) == 0
    
    def test_add_label(self):
        """Test adding labels to liability statement."""
        statement = dcat_us.LiabilityStatement(id="liability-1")
        statement.add_label("This data is provided as-is without warranty.")
        statement.add_label("Use at your own risk.")
        
        assert len(statement.label) == 2
        assert "This data is provided as-is without warranty." in statement.label
        assert "Use at your own risk." in statement.label
    
    def test_liability_statement_to_rdf(self):
        """Test serializing liability statement to RDF."""
        statement = dcat_us.LiabilityStatement(id="liability-1")
        statement.add_label("This data is provided as-is.")
        
        graph = statement.to_rdf_graph()
        assert len(graph) > 0
        
        subject = URIRef(str(dcat_us.DCAT_US) + statement.id)
        assert (subject, RDF.type, dcat_us.DCAT_US.LiabilityStatement) in graph


class TestUseRestriction:
    """Test cases for the UseRestriction class."""
    
    def test_create_use_restriction(self):
        """Test basic use restriction creation."""
        restriction = dcat_us.UseRestriction(
            id="use-restriction-1",
            restrictionStatus="http://example.org/status/restricted"
        )
        assert restriction.id == "use-restriction-1"
        assert restriction.restrictionStatus == "http://example.org/status/restricted"
    
    def test_use_restriction_with_all_fields(self):
        """Test use restriction with all fields."""
        restriction = dcat_us.UseRestriction(
            id="use-restriction-2",
            restrictionStatus="http://example.org/status/restricted",
            specificRestriction="http://example.org/restriction/no-commercial",
            restrictionNote="Non-commercial use only"
        )
        assert restriction.specificRestriction == "http://example.org/restriction/no-commercial"
        assert restriction.restrictionNote == "Non-commercial use only"
    
    def test_use_restriction_to_rdf(self):
        """Test serializing use restriction to RDF."""
        restriction = dcat_us.UseRestriction(
            id="use-restriction-1",
            restrictionStatus="http://example.org/status/restricted"
        )
        
        graph = restriction.to_rdf_graph()
        assert len(graph) > 0
        
        subject = URIRef(str(dcat_us.DCAT_US) + restriction.id)
        assert (subject, RDF.type, dcat_us.DCAT_US.UseRestriction) in graph


class TestRdfSerialization:
    """Test RDF serialization for DCAT-US classes."""
    
    def test_to_turtle(self):
        """Test serializing to Turtle format."""
        restriction = dcat_us.AccessRestriction(
            id="access-restriction-1",
            restrictionStatus="http://example.org/status/restricted",
            restrictionNote="Classified information"
        )
        
        turtle = restriction.to_rdf(format="turtle")
        assert "dcat-us:" in turtle or "http://resources.data.gov/ontology/dcat-us#" in turtle
        assert "restrictionStatus" in turtle
    
    def test_round_trip(self):
        """Test round-trip serialization and deserialization."""
        # Create original
        original = dcat_us.CuiRestriction(
            id="cui-1",
            cuiBannerMarking="CUI",
            designationIndicator="CUI//SP-PRVCY"
        )
        
        # Serialize
        turtle = original.to_rdf(format="turtle")
        
        # Deserialize
        subject = URIRef(str(dcat_us.DCAT_US) + "cui-1")
        restored = dcat_us.CuiRestriction.from_rdf(turtle, format="turtle", subject=subject)
        
        # Verify
        assert restored.id == original.id
        assert restored.cuiBannerMarking == original.cuiBannerMarking
        assert restored.designationIndicator == original.designationIndicator


class TestIntegration:
    """Integration tests for DCAT-US classes."""
    
    def test_complete_structure(self):
        """Test creating a complete DCAT-US structure."""
        # Create access restriction
        access_restriction = dcat_us.AccessRestriction(
            id="access-1",
            restrictionStatus="http://example.org/status/public",
            restrictionNote="Publicly accessible"
        )
        
        # Create use restriction
        use_restriction = dcat_us.UseRestriction(
            id="use-1",
            restrictionStatus="http://example.org/status/open",
            specificRestriction="http://example.org/restriction/attribution"
        )
        
        # Create bounding box
        bbox = dcat_us.GeographicBoundingBox(
            id="bbox-us",
            westBoundingLongitude=Decimal("-125.0"),
            eastBoundingLongitude=Decimal("-66.0"),
            northBoundingLatitude=Decimal("49.0"),
            southBoundingLatitude=Decimal("24.0")
        )
        
        # Create liability statement
        liability = dcat_us.LiabilityStatement(id="liability-1")
        liability.add_label("Data provided as-is without warranty")
        
        # Verify all objects created
        assert access_restriction.id == "access-1"
        assert use_restriction.id == "use-1"
        assert bbox.id == "bbox-us"
        assert liability.id == "liability-1"
    
    def test_multiple_rdf_serialization(self):
        """Test serializing multiple DCAT-US objects to RDF."""
        # Create objects
        restriction = dcat_us.AccessRestriction(
            id="access-1",
            restrictionStatus="http://example.org/status/restricted"
        )
        
        cui = dcat_us.CuiRestriction(
            id="cui-1",
            cuiBannerMarking="CUI",
            designationIndicator="CUI//SP-PRVCY"
        )
        
        # Serialize both to same graph
        graph = Graph()
        restriction.to_rdf_graph(graph)
        cui.to_rdf_graph(graph)
        
        # Verify both are in the graph
        restriction_uri = URIRef(str(dcat_us.DCAT_US) + "access-1")
        cui_uri = URIRef(str(dcat_us.DCAT_US) + "cui-1")
        
        assert (restriction_uri, RDF.type, dcat_us.DCAT_US.AccessRestriction) in graph
        assert (cui_uri, RDF.type, dcat_us.DCAT_US.CuiRestriction) in graph
