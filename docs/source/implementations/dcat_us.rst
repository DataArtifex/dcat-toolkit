DCAT-US 3.0
===========

DCAT-US is the US Government's application profile of DCAT, providing extensions for federal data management requirements including NARA records management and CUI (Controlled Unclassified Information) handling.

Overview
--------

DCAT-US extends DCAT with US-specific requirements:

- **Access Restrictions** - NARA access restriction codes
- **Use Restrictions** - Usage limitation codes
- **CUI Restrictions** - Controlled Unclassified Information handling
- **Geographic Bounding Boxes** - Precise spatial coverage
- **Liability Statements** - Legal disclaimers

**Official Specification:** https://doi-do.github.io/dcat-us/

DCAT-US Classes
---------------

The DCAT-US implementation includes 5 specialized classes:

1. **AccessRestriction** - NARA access restriction information
2. **UseRestriction** - Usage limitation information
3. **CuiRestriction** - CUI handling requirements
4. **GeographicBoundingBox** - Precise geographic coverage
5. **LiabilityStatement** - Legal liability disclaimers

Quick Example
-------------

.. code-block:: python

   from dartfx.dcat import dcat_us

   # Create access restriction
   access = dcat_us.AccessRestriction(id="access-1")
   access.set_restriction_status("http://example.org/status/restricted")
   access.set_specific_restriction("http://example.org/restriction/foia-exempt")
   access.set_restriction_note("Exempt under FOIA 5 USC 552(b)(6)")

   # Create CUI restriction
   cui = dcat_us.CuiRestriction(id="cui-1")
   cui.set_cui_banner_marking("CUI//SP-PRVCY")
   cui.set_designation_indicator("CUI")

   # Create geographic bounding box
   bbox = dcat_us.GeographicBoundingBox(id="bbox-1")
   bbox.set_west_bounding_longitude(-125.0)
   bbox.set_east_bounding_longitude(-65.0)
   bbox.set_south_bounding_latitude(24.0)
   bbox.set_north_bounding_latitude(49.0)

   # Create liability statement
   liability = dcat_us.LiabilityStatement(id="liability-1")
   liability.add_label("Data provided as-is without warranty")

Access Restrictions
-------------------

NARA access restriction codes:

.. code-block:: python

   from dartfx.dcat import dcat_us

   access = dcat_us.AccessRestriction(id="access-1")

   # Set restriction status (mandatory)
   access.set_restriction_status(
       "http://example.org/status/restricted"
   )

   # Set specific restriction (recommended)
   access.set_specific_restriction(
       "http://example.org/restriction/foia-exempt"
   )

   # Add restriction note (optional)
   access.set_restriction_note(
       "Exempt under FOIA 5 USC 552(b)(6) - Privacy"
   )

CUI Restrictions
----------------

Controlled Unclassified Information handling:

.. code-block:: python

   cui = dcat_us.CuiRestriction(id="cui-1")

   # Set CUI banner marking (mandatory)
   cui.set_cui_banner_marking("CUI//SP-PRVCY")

   # Set designation indicator (mandatory)
   cui.set_designation_indicator("CUI")

   # Set required indicator per authority (optional)
   cui.set_required_indicator_per_authority("Privacy Act")

Geographic Bounding Box
-----------------------

Precise geographic coverage using decimal degrees:

.. code-block:: python

   bbox = dcat_us.GeographicBoundingBox(id="bbox-1")

   # Set bounding coordinates (all mandatory)
   bbox.set_west_bounding_longitude(-125.0)   # Western boundary
   bbox.set_east_bounding_longitude(-65.0)    # Eastern boundary
   bbox.set_south_bounding_latitude(24.0)     # Southern boundary
   bbox.set_north_bounding_latitude(49.0)     # Northern boundary

Use Restrictions
----------------

Usage limitation information:

.. code-block:: python

   use = dcat_us.UseRestriction(id="use-1")

   # Set restriction status (mandatory)
   use.set_restriction_status(
       "http://example.org/status/restricted"
   )

   # Set specific restriction (recommended)
   use.set_specific_restriction(
       "http://example.org/restriction/attribution-required"
   )

   # Add restriction note (optional)
   use.set_restriction_note(
       "Attribution required for all uses"
   )

Liability Statement
-------------------

Legal disclaimers:

.. code-block:: python

   liability = dcat_us.LiabilityStatement(id="liability-1")

   # Add liability text (can be multilingual)
   liability.add_label(
       "Data provided as-is without warranty of any kind",
       lang="en"
   )
   liability.add_label(
       "Données fournies telles quelles sans garantie",
       lang="fr"
   )

Complete Example
----------------

.. code-block:: python

   from dartfx.dcat import Dataset, Distribution
   from dartfx.dcat import dcat_us

   # Create dataset
   dataset = Dataset(id="federal-dataset")
   dataset.add_title("Federal Dataset with Restrictions")

   # Add access restriction
   access = dcat_us.AccessRestriction(id="access-1")
   access.set_restriction_status("http://example.org/status/restricted")
   access.set_specific_restriction("http://example.org/restriction/foia")

   # Add CUI restriction
   cui = dcat_us.CuiRestriction(id="cui-1")
   cui.set_cui_banner_marking("CUI//SP-PRVCY")
   cui.set_designation_indicator("CUI")

   # Add geographic coverage
   bbox = dcat_us.GeographicBoundingBox(id="bbox-1")
   bbox.set_west_bounding_longitude(-125.0)
   bbox.set_east_bounding_longitude(-65.0)
   bbox.set_south_bounding_latitude(24.0)
   bbox.set_north_bounding_latitude(49.0)

   # Create distribution with liability statement
   distribution = Distribution(id="dist-1")
   distribution.add_download_url("http://example.org/data.csv")

   liability = dcat_us.LiabilityStatement(id="liability-1")
   liability.add_label("Data provided as-is without warranty")

   dataset.add_distribution(distribution)

Testing
-------

The DCAT-US implementation includes 19 comprehensive tests:

.. code-block:: bash

   # Run all DCAT-US tests
   pytest tests/test_dcat_us.py -v

   # Run with coverage
   pytest tests/test_dcat_us.py --cov=dartfx.dcat.dcat_us

Compliance
----------

This implementation is fully compliant with:

- ✅ DCAT-US Version 3.0
- ✅ NARA records management requirements
- ✅ CUI handling requirements
- ✅ Federal data management standards

See Also
--------

- :doc:`dcat` - DCAT Core Implementation
- `DCAT_US_IMPLEMENTATION.md <../../DCAT_US_IMPLEMENTATION.md>`_ - Complete implementation guide
