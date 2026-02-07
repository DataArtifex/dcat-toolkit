DCAT-AP 3.0.1
=============

DCAT Application Profile for data portals in Europe (DCAT-AP) extends DCAT with European-specific requirements and controlled vocabularies.

Overview
--------

DCAT-AP provides a minimal common basis within Europe to share Datasets and Data Services cross-border and cross-domain.

Key features:

- **EU Controlled Vocabularies** - Mandatory and recommended vocabularies
- **Multilingual Support** - Language-tagged literals for all EU languages
- **HVD Support** - High Value Datasets regulation compliance
- **Legal Metadata** - Applicable legislation tracking

**Official Specification:** https://semiceu.github.io/DCAT-AP/releases/3.0.1/

DCAT-AP Classes
---------------

DCAT-AP extends 6 core DCAT classes:

1. **Catalog** - Extended with applicable legislation, geographical/temporal coverage
2. **Dataset** - Extended with HVD support, access rights, provenance
3. **Distribution** - Extended with availability, ODRL policies, status
4. **DataService** - Extended with applicable legislation
5. **DatasetSeries** - Extended with applicable legislation, access rights
6. **CatalogRecord** - Extended with applicable legislation

Quick Example
-------------

.. code-block:: python

   from dartfx.dcat import dcat_ap

   # Create European catalog
   catalog = dcat_ap.Catalog(id="eu-portal")
   catalog.add_title("European Open Data Portal", lang="en")
   catalog.add_title("Portail européen de données ouvertes", lang="fr")
   catalog.add_geographical_coverage(
       "http://publications.europa.eu/resource/authority/continent/EUROPE"
   )

   # Create dataset with EU vocabularies
   dataset = dcat_ap.Dataset(id="population-stats")
   dataset.add_title("European Population Statistics", lang="en")
   
   # Add theme using EU Data Theme vocabulary (mandatory)
   dataset.add_theme(
       "http://publications.europa.eu/resource/authority/data-theme/SOCI"
   )
   
   # Set access rights using EU vocabulary (recommended)
   dataset.set_access_rights(
       "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
   )
   
   # Add frequency using EU vocabulary
   dataset.add_frequency(
       "http://publications.europa.eu/resource/authority/frequency/ANNUAL"
   )

   # Create distribution
   distribution = dcat_ap.Distribution(id="csv-dist")
   distribution.add_download_url("http://example.org/data.csv")
   distribution.add_media_type("text/csv")
   
   # Set availability using EU vocabulary
   distribution.set_availability(
       "http://publications.europa.eu/resource/authority/planned-availability/AVAILABLE"
   )

   dataset.add_distribution(distribution)
   catalog.add_dataset(dataset)

Controlled Vocabularies
------------------------

DCAT-AP defines specific controlled vocabularies that MUST, SHOULD, or MAY be used:

Mandatory Vocabularies
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Property
     - Vocabulary
   * - Media Type
     - IANA Media Types
   * - Frequency
     - EU Frequency
   * - File Type
     - EU File Type
   * - Language
     - EU Languages
   * - Distribution Status
     - EU Distribution Status
   * - Availability
     - EU Planned Availability

Recommended Vocabularies
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Property
     - Vocabulary
   * - Access Rights
     - EU Access Rights
   * - Publisher Type
     - ADMS Publisher Type
   * - Licence Type
     - ADMS Licence Type

Using Controlled Vocabularies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from dartfx.dcat import dcat_ap

   dataset = dcat_ap.Dataset(id="dataset-1")
   
   # Use EU Data Theme (at least 1 required)
   dataset.add_theme(
       "http://publications.europa.eu/resource/authority/data-theme/ECON"
   )
   
   # Use EU Access Rights (recommended)
   dataset.set_access_rights(
       "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
   )
   
   # Use EU Frequency (mandatory if present)
   dataset.add_frequency(
       "http://publications.europa.eu/resource/authority/frequency/MONTHLY"
   )

Multilingual Support
--------------------

DCAT-AP emphasizes multilingual metadata:

.. code-block:: python

   dataset = dcat_ap.Dataset(id="multilingual-dataset")
   
   # Add titles in multiple EU languages
   dataset.add_title("Population Data", lang="en")
   dataset.add_title("Données de population", lang="fr")
   dataset.add_title("Bevölkerungsdaten", lang="de")
   dataset.add_title("Datos de población", lang="es")
   dataset.add_title("Dati sulla popolazione", lang="it")
   
   # Add descriptions in multiple languages
   dataset.add_description("Annual population statistics", lang="en")
   dataset.add_description("Statistiques annuelles de population", lang="fr")
   dataset.add_description("Jährliche Bevölkerungsstatistiken", lang="de")

Provenance and Attribution
---------------------------

DCAT-AP supports detailed provenance information:

.. code-block:: python

   dataset = dcat_ap.Dataset(id="dataset-1")
   
   # Add provenance statement
   dataset.add_provenance("http://example.org/provenance/statement-1")
   
   # Add qualified attribution
   dataset.add_qualified_attribution("http://example.org/attribution/1")
   
   # Add source dataset
   dataset.add_source("http://example.org/source-dataset")
   
   # Add activity that generated this dataset
   dataset.add_was_generated_by("http://example.org/activity/1")

ODRL Policies
-------------

DCAT-AP supports ODRL (Open Digital Rights Language) policies:

.. code-block:: python

   distribution = dcat_ap.Distribution(id="dist-1")
   distribution.add_download_url("http://example.org/data.csv")
   
   # Add ODRL policy
   distribution.add_policy("http://example.org/policy/open-data")
   distribution.add_policy("http://example.org/policy/attribution-required")

Complete Example
----------------

.. code-block:: python

   from dartfx.dcat import dcat_ap

   # Create catalog
   catalog = dcat_ap.Catalog(id="eu-catalog")
   catalog.add_title("European Data Catalog", lang="en")
   catalog.add_description("Catalog of European datasets", lang="en")
   catalog.add_publisher(
       "http://publications.europa.eu/resource/authority/corporate-body/PUBL"
   )

   # Create dataset
   dataset = dcat_ap.Dataset(id="economic-data")
   dataset.add_title("European Economic Data", lang="en")
   dataset.add_description("Economic indicators for EU member states", lang="en")
   
   # Add EU vocabularies
   dataset.add_theme(
       "http://publications.europa.eu/resource/authority/data-theme/ECON"
   )
   dataset.set_access_rights(
       "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
   )
   dataset.add_frequency(
       "http://publications.europa.eu/resource/authority/frequency/QUARTERLY"
   )
   
   # Add spatial coverage
   dataset.add_spatial(
       "http://publications.europa.eu/resource/authority/continent/EUROPE"
   )
   
   # Create distribution
   distribution = dcat_ap.Distribution(id="csv-dist")
   distribution.add_download_url("http://example.org/economic-data.csv")
   distribution.add_media_type("text/csv")
   distribution.set_availability(
       "http://publications.europa.eu/resource/authority/planned-availability/AVAILABLE"
   )
   distribution.set_status(
       "http://publications.europa.eu/resource/authority/distribution-status/COMPLETED"
   )
   
   dataset.add_distribution(distribution)
   catalog.add_dataset(dataset)
   
   # Serialize to RDF
   turtle = catalog.to_rdf(format='turtle')

Testing
-------

The DCAT-AP implementation includes 32 comprehensive tests:

.. code-block:: bash

   # Run all DCAT-AP tests
   pytest tests/test_dcat_ap.py -v

   # Run with coverage
   pytest tests/test_dcat_ap.py --cov=dartfx.dcat.dcat_ap

Compliance
----------

This implementation is fully compliant with:

- ✅ DCAT-AP Version 3.0.1
- ✅ DCAT Version 3
- ✅ EU Controlled Vocabularies
- ✅ SEMIC Standards

See Also
--------

- :doc:`../api/dcat_ap` - API Reference
- :doc:`dcat_ap_hvd` - DCAT-AP HVD Implementation
- :doc:`dcat` - DCAT Core Implementation
- `DCAT_AP_IMPLEMENTATION.md <../../DCAT_AP_IMPLEMENTATION.md>`_ - Complete implementation guide
