DCAT 3.0 Core
==============

The W3C Data Catalog Vocabulary (DCAT) is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the Web.

Overview
--------

DCAT 3.0 provides the core vocabulary for describing:

- **Datasets** - Collections of data
- **Distributions** - Specific representations of datasets
- **Data Services** - APIs providing access to data
- **Catalogs** - Collections of metadata about resources

**Official Specification:** https://www.w3.org/TR/vocab-dcat-3/

Core Classes
------------

The DCAT 3.0 implementation includes 9 core classes:

1. **Resource** - Base class for all cataloged resources (16 properties)
2. **Dataset** - Collection of data published by a single agent
3. **Distribution** - Specific representation of a dataset
4. **DataService** - Collection of operations providing access to datasets
5. **Catalog** - Curated collection of metadata about resources
6. **CatalogRecord** - Metadata about a dataset's entry in a catalog
7. **DatasetSeries** - Collection of datasets published separately
8. **Relationship** - Association between datasets
9. **Role** - Function of an entity with respect to another resource

Quick Example
-------------

.. code-block:: python

   from dartfx.dcat import Catalog, Dataset, Distribution

   # Create catalog
   catalog = Catalog(id="open-data-portal")
   catalog.add_title("Open Data Portal", lang="en")
   catalog.add_description("Central catalog for open datasets", lang="en")
   catalog.add_publisher("http://example.org/government")

   # Create dataset
   dataset = Dataset(id="population-2024")
   dataset.add_title("Population Statistics 2024", lang="en")
   dataset.add_description("Annual population data", lang="en")
   dataset.add_keyword("population")
   dataset.add_keyword("statistics")
   dataset.add_license("http://creativecommons.org/licenses/by/4.0/")

   # Create distribution
   distribution = Distribution(id="csv-dist")
   distribution.add_download_url("http://example.org/data.csv")
   distribution.add_media_type("text/csv")

   # Link everything
   dataset.add_distribution(distribution)
   catalog.add_dataset(dataset)

   # Serialize to RDF
   turtle = catalog.to_rdf(format='turtle')

RDF Serialization
-----------------

DCAT supports multiple RDF serialization formats:

.. code-block:: python

   # Turtle
   turtle = dataset.to_rdf(format='turtle')

   # RDF/XML
   xml = dataset.to_rdf(format='xml')

   # JSON-LD
   jsonld = dataset.to_rdf(format='json-ld')

   # N-Triples
   ntriples = dataset.to_rdf(format='nt')

Multilingual Support
--------------------

DCAT supports language-tagged literals:

.. code-block:: python

   dataset.add_title("Population Data", lang="en")
   dataset.add_title("Données de population", lang="fr")
   dataset.add_title("Bevölkerungsdaten", lang="de")

   dataset.add_description("Annual statistics", lang="en")
   dataset.add_description("Statistiques annuelles", lang="fr")

Features
--------

✅ **Pydantic Models** - Type-safe with automatic validation
✅ **RDF Native** - Full serialization/deserialization
✅ **Helper Methods** - Convenient ``add_*`` methods for all properties
✅ **Multilingual** - Language-tagged literals
✅ **Extensible** - Easy to extend for application profiles

Testing
-------

The DCAT 3.0 implementation includes 38 comprehensive tests:

.. code-block:: bash

   # Run all DCAT tests
   pytest tests/test_dcat.py -v

   # Run with coverage
   pytest tests/test_dcat.py --cov=dartfx.dcat.dcat

Compliance
----------

This implementation is fully compliant with:

- ✅ W3C DCAT Version 3.0
- ✅ RDF 1.1
- ✅ Dublin Core Terms
- ✅ FOAF vocabulary
- ✅ SPDX vocabulary

See Also
--------

- :doc:`dcat_us` - DCAT-US Implementation
- :doc:`dcat_ap` - DCAT-AP Implementation
- `DCAT_IMPLEMENTATION.md <../../DCAT_IMPLEMENTATION.md>`_ - Complete implementation guide
