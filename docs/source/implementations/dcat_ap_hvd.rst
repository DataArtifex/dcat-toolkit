DCAT-AP HVD 3.0.0
=================

DCAT Application Profile for High Value Datasets extends DCAT-AP with specific requirements for datasets subject to Commission Implementing Regulation (EU) 2023/138.

Overview
--------

DCAT-AP HVD provides usage guidelines on top of DCAT-AP for catalogued resources within the scope of the High-Value Dataset implementing regulation.

Key features:

- **Six HVD Categories** - Official thematic categories
- **HVD Regulation Compliance** - Automatic regulation reference
- **Compliance Helpers** - ``make_hvd_compliant()`` and ``is_hvd_compliant()`` methods
- **HVD Licences** - CC-BY 4.0 and more permissive licences
- **Mandatory APIs** - API support required for HVD datasets

**Official Specification:** https://semiceu.github.io/DCAT-AP/releases/3.0.0-hvd/
**HVD Regulation:** https://eur-lex.europa.eu/eli/reg_impl/2023/138/oj

HVD Categories
--------------

The six thematic categories of High Value Datasets:

.. code-block:: python

   from dartfx.dcat import HVDCategory

   # Official HVD Categories from EU Vocabularies
   HVDCategory.GEOSPATIAL           # Geospatial data
   HVDCategory.EARTH_OBSERVATION    # Earth observation & environment
   HVDCategory.ENVIRONMENT          # Environment
   HVDCategory.METEOROLOGICAL       # Meteorological data
   HVDCategory.STATISTICS           # Statistics
   HVDCategory.COMPANIES            # Company & ownership data

Quick Example
-------------

.. code-block:: python

   from dartfx.dcat import Dataset, Distribution, DataService, HVDCategory, HVDLicence

   # Create HVD dataset
   dataset = Dataset(id="hvd-geo-1")
   dataset.add_title("European Geospatial Data", lang="en")
   dataset.add_description("High Value geospatial dataset", lang="en")

   # Make HVD-compliant (adds regulation and category)
   dataset.make_hvd_compliant(HVDCategory.GEOSPATIAL)

   # Add mandatory contact point
   dataset.add_contact_point("http://example.org/contact")

   # Verify compliance
   if dataset.is_hvd_compliant():
       print("✅ Dataset is HVD-compliant!")

   # Create bulk download distribution
   bulk = Distribution(id="bulk-download")
   bulk.make_hvd_compliant()
   bulk.add_download_url("http://example.org/data.zip")
   bulk.add_license(HVDLicence.CC_BY_4_0)

   # Create API (MANDATORY for HVD)
   api = DataService(id="hvd-api")
   api.add_title("Geospatial API", lang="en")
   api.make_hvd_compliant(HVDCategory.GEOSPATIAL)
   api.add_endpoint_url("https://api.example.org/geospatial")
   api.add_contact_point("http://example.org/contact")

   dataset.add_distribution(bulk)

HVD Requirements
----------------

Mandatory for HVD Datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Applicable Legislation** - Must reference HVD regulation
2. **HVD Category** - At least one category from the six official categories
3. **Contact Point** - Mandatory contact information
4. **Conforms To** - For specific data requirements
5. **Distribution** - At least one distribution OR data service

Mandatory for HVD Distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Applicable Legislation** - Must reference HVD regulation
2. **Access URL** - Mandatory access point
3. **Licence** - Must be CC-BY 4.0 or more permissive

Mandatory for HVD Data Services (APIs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Applicable Legislation** - Must reference HVD regulation
2. **HVD Category** - At least one category
3. **Endpoint URL** - Persistent endpoint
4. **Contact Point** - Mandatory contact information

.. note::
   APIs are **MANDATORY** for HVD datasets!

Compliance Helpers
------------------

make_hvd_compliant()
~~~~~~~~~~~~~~~~~~~~

Automatically adds HVD regulation and category:

.. code-block:: python

   # For Dataset
   dataset.make_hvd_compliant(HVDCategory.GEOSPATIAL)
   # Adds: applicableLegislation + hvdCategory

   # For Distribution
   distribution.make_hvd_compliant()
   # Adds: applicableLegislation

   # For DataService
   api.make_hvd_compliant(HVDCategory.ENVIRONMENT)
   # Adds: applicableLegislation + hvdCategory

   # For DatasetSeries
   series.make_hvd_compliant(HVDCategory.COMPANIES)
   # Adds: applicableLegislation + hvdCategory

is_hvd_compliant()
~~~~~~~~~~~~~~~~~~

Checks if resource meets HVD mandatory requirements:

.. code-block:: python

   # For Dataset
   if dataset.is_hvd_compliant():
       # Has: HVD regulation + at least one HVD category
       print("✅ Dataset is HVD-compliant!")

   # For Distribution
   if distribution.is_hvd_compliant():
       # Has: HVD regulation + access URL + licence
       print("✅ Distribution is HVD-compliant!")

   # For DataService
   if api.is_hvd_compliant():
       # Has: HVD regulation + HVD category + endpoint URL
       print("✅ API is HVD-compliant!")

HVD Licences
------------

HVD datasets must be made available under licences that are **compatible with Creative Commons BY 4.0 or more permissive**.

Compliant Licences
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from dartfx.dcat import HVDLicence

   # Creative Commons BY 4.0 (minimum requirement)
   HVDLicence.CC_BY_4_0
   # "http://creativecommons.org/licenses/by/4.0/"

   # Creative Commons Zero (public domain - more permissive)
   HVDLicence.CC0_1_0
   # "http://creativecommons.org/publicdomain/zero/1.0/"

   # EU No Restrictions
   HVDLicence.EU_NO_RESTRICTIONS
   # "http://publications.europa.eu/resource/authority/licence/NO_RESTRICTIONS"

   # Check if licence is HVD-compliant
   if HVDLicence.is_hvd_compliant(licence_uri):
       print("✅ Licence is HVD-compliant!")

Complete HVD Example
--------------------

.. code-block:: python

   from dartfx.dcat import (
       Catalog, Dataset, Distribution, DataService,
       HVDCategory, HVDLicence
   )

   # Create HVD catalog
   catalog = Catalog(id="eu-hvd-portal")
   catalog.add_title("European HVD Portal", lang="en")
   catalog.add_description("Catalog of High Value Datasets", lang="en")

   # Create HVD dataset
   dataset = Dataset(id="hvd-statistics-1")
   dataset.add_title("EU Population Statistics", lang="en")
   dataset.add_description("Annual population data", lang="en")

   # Make HVD-compliant
   dataset.make_hvd_compliant(HVDCategory.STATISTICS)
   dataset.add_contact_point("http://example.org/contact")
   dataset.add_conforms_to("http://example.org/standard/statistics")

   # Create bulk download (recommended)
   bulk = Distribution(id="bulk-csv")
   bulk.make_hvd_compliant()
   bulk.add_download_url("http://example.org/population.csv")
   bulk.add_license(HVDLicence.CC0_1_0)  # Public domain
   bulk.add_media_type("text/csv")

   # Create API (MANDATORY for HVD)
   api = DataService(id="stats-api")
   api.add_title("Statistics API", lang="en")
   api.make_hvd_compliant(HVDCategory.STATISTICS)
   api.add_endpoint_url("https://api.example.org/statistics")
   api.add_contact_point("http://example.org/contact")

   # Create API distribution
   api_dist = Distribution(id="api-json")
   api_dist.make_hvd_compliant()
   api_dist.add_access_url("https://api.example.org/statistics")
   api_dist.add_license(HVDLicence.CC0_1_0)
   api_dist.add_media_type("application/json")
   api_dist.add_access_service(api)

   # Link everything
   dataset.add_distribution(bulk)
   dataset.add_distribution(api_dist)
   catalog.add_dataset(dataset)
   catalog.add_service(api)

   # Verify HVD compliance
   assert dataset.is_hvd_compliant()  # ✅
   assert bulk.is_hvd_compliant()     # ✅
   assert api_dist.is_hvd_compliant() # ✅
   assert api.is_hvd_compliant()      # ✅

   # Serialize to RDF
   turtle = catalog.to_rdf(format='turtle')

HVD Regulation Requirements
----------------------------

Article 3: Licensing
~~~~~~~~~~~~~~~~~~~~

- ✅ Datasets must be available under CC-BY 4.0 or more permissive
- ✅ Implemented via ``HVDLicence`` class

Article 4: APIs
~~~~~~~~~~~~~~~

- ✅ APIs are **mandatory** for HVD datasets
- ✅ Implemented via ``DataService`` class with ``hvdCategory``

Article 5: Reporting
~~~~~~~~~~~~~~~~~~~~~

- ✅ Persistent identifiers for datasets, APIs, and licences
- ✅ Metadata must include HVD category
- ✅ Implemented via ``applicableLegislation`` and ``hvdCategory``

Testing
-------

The DCAT-AP HVD implementation includes 26 comprehensive tests:

.. code-block:: bash

   # Run all HVD tests
   pytest tests/test_dcat_ap_hvd.py -v

   # Run specific test class
   pytest tests/test_dcat_ap_hvd.py::TestCompleteHVDExample -v

   # Run with coverage
   pytest tests/test_dcat_ap_hvd.py --cov=dartfx.dcat.dcat_ap_hvd

Compliance
----------

This implementation is fully compliant with:

- ✅ DCAT-AP HVD Version 3.0.0
- ✅ DCAT-AP Version 3.0.1
- ✅ DCAT Version 3
- ✅ EU HVD Regulation (EU) 2023/138
- ✅ EU Vocabularies

See Also
--------

- :doc:`../api/dcat_ap_hvd` - API Reference
- :doc:`dcat_ap` - DCAT-AP Implementation
- `DCAT_AP_HVD_IMPLEMENTATION.md <../../DCAT_AP_HVD_IMPLEMENTATION.md>`_ - Complete implementation guide
