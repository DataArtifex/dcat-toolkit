DCAT Toolkit Documentation
===========================

Welcome to the **DCAT Toolkit** documentation!

The DCAT Toolkit is a comprehensive Python implementation of the W3C Data Catalog Vocabulary (DCAT) and its application profiles, providing Pydantic-based models with full RDF serialization and deserialization support.

.. image:: https://img.shields.io/badge/DCAT-3.0-blue
   :alt: DCAT 3.0

.. image:: https://img.shields.io/badge/DCAT--US-3.0-green
   :alt: DCAT-US 3.0

.. image:: https://img.shields.io/badge/DCAT--AP-3.0.1-yellow
   :alt: DCAT-AP 3.0.1

.. image:: https://img.shields.io/badge/DCAT--AP%20HVD-3.0.0-orange
   :alt: DCAT-AP HVD 3.0.0

Features
--------

✅ **Four Complete Implementations**

- **DCAT 3.0** - W3C Core standard (9 classes, 38 tests)
- **DCAT-US 3.0** - US Government profile (5 classes, 19 tests)
- **DCAT-AP 3.0.1** - European profile (6 classes, 32 tests)
- **DCAT-AP HVD 3.0.0** - High Value Datasets (6 classes, 26 tests)

✅ **Pydantic-Based Models**

- Type-safe with automatic validation
- Easy serialization/deserialization
- IDE autocomplete support

✅ **Full RDF Support**

- Serialize to Turtle, RDF/XML, JSON-LD, N-Triples
- Deserialize from any RDF format
- Built on rdflib

✅ **Production Ready**

- 115 comprehensive tests (100% passing)
- Complete documentation
- Fully compliant with all specifications

Quick Start
-----------

Installation
~~~~~~~~~~~~

.. code-block:: bash

   pip install dcat-toolkit

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   from dartfx.dcat import Catalog, Dataset, Distribution

   # Create a catalog
   catalog = Catalog(id="my-catalog")
   catalog.add_title("Open Data Catalog", lang="en")
   catalog.add_description("A catalog of open datasets", lang="en")

   # Create a dataset
   dataset = Dataset(id="population-2024")
   dataset.add_title("Population Statistics 2024", lang="en")
   dataset.add_description("Annual population data", lang="en")
   dataset.add_keyword("population")
   dataset.add_keyword("statistics")

   # Create a distribution
   distribution = Distribution(id="csv-dist")
   distribution.add_download_url("http://example.org/data.csv")
   distribution.add_media_type("text/csv")

   # Link everything together
   dataset.add_distribution(distribution)
   catalog.add_dataset(dataset)

   # Serialize to RDF Turtle
   turtle = catalog.to_rdf(format='turtle')
   print(turtle)

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart
   user_guide/index

.. toctree::
   :maxdepth: 2
   :caption: DCAT Implementations

   implementations/dcat
   implementations/dcat_us
   implementations/dcat_ap
   implementations/dcat_ap_hvd

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/dcat
   api/dcat_us
   api/dcat_ap
   api/dcat_ap_hvd

.. toctree::
   :maxdepth: 1
   :caption: Additional Resources

   examples
   contributing
   changelog
   license

Implementations
---------------

DCAT 3.0 (Core)
~~~~~~~~~~~~~~~

The W3C Data Catalog Vocabulary core implementation with 9 classes:

- Resource, Dataset, Distribution, DataService
- Catalog, CatalogRecord, DatasetSeries
- Relationship, Role

**Specification:** https://www.w3.org/TR/vocab-dcat-3/

DCAT-US 3.0
~~~~~~~~~~~

US Government profile with NARA and CUI support:

- AccessRestriction, UseRestriction, CuiRestriction
- GeographicBoundingBox, LiabilityStatement

**Specification:** https://doi-do.github.io/dcat-us/

DCAT-AP 3.0.1
~~~~~~~~~~~~~

European Application Profile with EU controlled vocabularies:

- Extended Catalog, Dataset, Distribution
- DataService, DatasetSeries, CatalogRecord
- HVD support, controlled vocabularies

**Specification:** https://semiceu.github.io/DCAT-AP/releases/3.0.1/

DCAT-AP HVD 3.0.0
~~~~~~~~~~~~~~~~~

High Value Datasets profile for EU Regulation (EU) 2023/138:

- HVD-compliant Dataset, Distribution, DataService
- Six official HVD categories
- Compliance helpers and validation

**Specification:** https://semiceu.github.io/DCAT-AP/releases/3.0.0-hvd/

Statistics
----------

.. list-table::
   :header-rows: 1
   :widths: 30 15 15 40

   * - Implementation
     - Classes
     - Tests
     - Compliance
   * - DCAT 3.0
     - 9
     - 38
     - W3C DCAT 3.0
   * - DCAT-US 3.0
     - 5
     - 19
     - NARA + CUI
   * - DCAT-AP 3.0.1
     - 6
     - 32
     - EU Vocabularies
   * - DCAT-AP HVD 3.0.0
     - 6
     - 26
     - HVD Regulation
   * - **Total**
     - **26**
     - **115**
     - **100% Compliant**

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
