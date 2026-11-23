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

The DCAT-US implementation includes 5 specialized extension classes plus profile subclasses for core DCAT resources:

1. **AccessRestriction** - NARA access restriction information
2. **UseRestriction** - Usage limitation information
3. **CuiRestriction** - CUI handling requirements
4. **GeographicBoundingBox** - Precise geographic coverage
5. **LiabilityStatement** - Legal liability disclaimers
6. **Dataset / Distribution / Catalog** - DCAT-US profile extensions of core DCAT classes (`DcatUSDataset`, `DcatUSDistribution`, `DcatUSCatalog`)

Quick Example
-------------

.. code-block:: python

   from decimal import Decimal
   from dartfx.dcat import dcat_us

   # Create access restriction
   access = dcat_us.AccessRestriction(
       id="access-1",
       restrictionStatus="http://example.org/status/restricted",
       specificRestriction="http://example.org/restriction/foia-exempt",
       restrictionNote="Exempt under FOIA 5 USC 552(b)(6)",
   )

   # Create CUI restriction
   cui = dcat_us.CuiRestriction(
       id="cui-1",
       cuiBannerMarking="CUI//SP-PRVCY",
       designationIndicator="CUI",
   )

   # Create geographic bounding box
   bbox = dcat_us.GeographicBoundingBox(
       id="bbox-1",
       westBoundingLongitude=Decimal("-125.0"),
       eastBoundingLongitude=Decimal("-65.0"),
       southBoundingLatitude=Decimal("24.0"),
       northBoundingLatitude=Decimal("49.0"),
   )

   # Create liability statement
   liability = dcat_us.LiabilityStatement(id="liability-1")
   liability.add_label("Data provided as-is without warranty")

Access Restrictions
-------------------

NARA access restriction codes:

.. code-block:: python

   from dartfx.dcat import dcat_us

   access = dcat_us.AccessRestriction(
       id="access-1",
       # Mandatory
       restrictionStatus="http://example.org/status/restricted",
       # Optional
       specificRestriction="http://example.org/restriction/foia-exempt",
       restrictionNote="Exempt under FOIA 5 USC 552(b)(6) - Privacy",
   )

CUI Restrictions
----------------

Controlled Unclassified Information handling:

.. code-block:: python

   cui = dcat_us.CuiRestriction(
       id="cui-1",
       # Mandatory
       cuiBannerMarking="CUI//SP-PRVCY",
       designationIndicator="CUI",
       # Optional
       requiredIndicatorPerAuthority="Privacy Act",
   )

Geographic Bounding Box
-----------------------

Precise geographic coverage using decimal degrees:

.. code-block:: python

   from decimal import Decimal

   bbox = dcat_us.GeographicBoundingBox(
       id="bbox-1",
       westBoundingLongitude=Decimal("-125.0"),   # Western boundary
       eastBoundingLongitude=Decimal("-65.0"),    # Eastern boundary
       southBoundingLatitude=Decimal("24.0"),     # Southern boundary
       northBoundingLatitude=Decimal("49.0"),     # Northern boundary
   )

Use Restrictions
----------------

Usage limitation information:

.. code-block:: python

   use = dcat_us.UseRestriction(
       id="use-1",
       # Mandatory
       restrictionStatus="http://example.org/status/restricted",
       # Recommended
       specificRestriction="http://example.org/restriction/attribution-required",
       # Optional
       restrictionNote="Attribution required for all uses",
   )

Liability Statement
-------------------

Legal disclaimers:

.. code-block:: python

   liability = dcat_us.LiabilityStatement(id="liability-1")

   # Add liability text (can be multilingual)
   liability.add_label(
       "Data provided as-is without warranty of any kind",
       lang="en",
   )
   liability.add_label(
       "Données fournies telles quelles sans garantie",
       lang="fr",
   )

Complete Example
----------------

.. code-block:: python

   from decimal import Decimal
   from dartfx.dcat import DcatUSDataset, DcatUSDistribution, dcat_us

   # Create dataset
   dataset = DcatUSDataset(id="federal-dataset")
   dataset.add_title("Federal Dataset with Restrictions")

   # Add access restriction
   access = dcat_us.AccessRestriction(
       id="access-1",
       restrictionStatus="http://example.org/status/restricted",
       specificRestriction="http://example.org/restriction/foia",
   )
   dataset.add_access_restriction(access)

   # Add CUI restriction
   cui = dcat_us.CuiRestriction(
       id="cui-1",
       cuiBannerMarking="CUI//SP-PRVCY",
       designationIndicator="CUI",
   )
   dataset.set_cui_restriction(cui)

   # Add geographic coverage
   bbox = dcat_us.GeographicBoundingBox(
       id="bbox-1",
       westBoundingLongitude=Decimal("-125.0"),
       eastBoundingLongitude=Decimal("-65.0"),
       southBoundingLatitude=Decimal("24.0"),
       northBoundingLatitude=Decimal("49.0"),
   )
   dataset.add_geographic_bounding_box(bbox)

   # Create distribution with liability statement
   distribution = DcatUSDistribution(id="dist-1")
   distribution.add_download_url("http://example.org/data.csv")

   liability = dcat_us.LiabilityStatement(id="liability-1")
   liability.add_label("Data provided as-is without warranty")
   distribution.set_liability_statement(liability)

   dataset.add_distribution(distribution)

Testing
-------

The DCAT-US implementation includes 21 comprehensive tests:

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
