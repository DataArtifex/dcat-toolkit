Quick Start
===========

This guide will help you get started with the DCAT Toolkit.

Basic Example
-------------

Create a simple data catalog:

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

Choose Your Profile
-------------------

The DCAT Toolkit provides four implementations. Choose the one that fits your needs:

DCAT 3.0 (Core)
~~~~~~~~~~~~~~~

For general data catalogs following the W3C standard:

.. code-block:: python

   from dartfx.dcat import DcatDataset, DcatDistribution

DCAT-US 3.0
~~~~~~~~~~~

For US Government data portals:

.. code-block:: python

   from dartfx.dcat import dcat_us

   access = dcat_us.AccessRestriction(id="access-1")
   access.set_restriction_status("http://example.org/status/restricted")

DCAT-AP 3.0.1
~~~~~~~~~~~~~

For European data portals:

.. code-block:: python

   from dartfx.dcat import DcatAPDataset

   dataset = DcatAPDataset(id="eu-dataset")
   dataset.add_theme(
       "http://publications.europa.eu/resource/authority/data-theme/ECON"
   )

DCAT-AP HVD 3.0.0 (Default)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For High Value Datasets (most specific):

.. code-block:: python

   from dartfx.dcat import Dataset, HVDCategory

   dataset = Dataset(id="hvd-dataset")
   dataset.make_hvd_compliant(HVDCategory.GEOSPATIAL)

Next Steps
----------

- Read the :doc:`user_guide/index` for detailed information
- Explore :doc:`implementations/dcat` for DCAT core
- Check :doc:`implementations/dcat_ap_hvd` for HVD datasets
- View :doc:`examples` for more examples
