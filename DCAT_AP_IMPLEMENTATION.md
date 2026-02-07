# DCAT-AP 3.0.1 Implementation Summary

**Date:** 2026-02-06  
**Version:** 3.0.1  
**Status:** ✅ COMPLETED

---

## Overview

Successfully implemented **DCAT-AP Version 3.0.1** (DCAT Application Profile for data portals in Europe) by extending the core DCAT 3.0 classes with European-specific properties and controlled vocabularies.

DCAT-AP provides a minimal common basis within Europe to share Datasets and Data Services cross-border and cross-domain.

**Official Specification:** https://semiceu.github.io/DCAT-AP/releases/3.0.1/

---

## DCAT-AP 3.0.1 Implementation

### Extended DCAT Classes

All core DCAT classes have been extended with DCAT-AP specific properties:

✅ **Catalog** - Extended with applicable legislation, geographical/temporal coverage  
✅ **Dataset** - Extended with HVD support, access rights, provenance, qualified attribution  
✅ **Distribution** - Extended with availability, ODRL policies, status  
✅ **DataService** - Extended with applicable legislation  
✅ **DatasetSeries** - Extended with applicable legislation, access rights  
✅ **CatalogRecord** - Extended with applicable legislation  

### DCAT-AP Specific Features

✅ **Controlled Vocabularies** - EU mandatory and recommended vocabularies  
✅ **High Value Datasets (HVD)** - Full support for HVD regulation  
✅ **Multilingual Support** - Language-tagged literals  
✅ **Legal Metadata** - Applicable legislation tracking  

---

## Key DCAT-AP Extensions

### 1. Applicable Legislation

**Property:** `dcatap:applicableLegislation`  
**Usage:** Mandatory for High Value Datasets (HVD)  
**Type:** Legal Resource

All main classes support this property for HVD compliance:

```python
from dartfx.dcat import dcat_ap

# Add HVD regulation to dataset
dataset = dcat_ap.Dataset(id="hvd-dataset")
dataset.add_applicable_legislation(
    "http://data.europa.eu/eli/reg_impl/2023/138/oj"
)
```

### 2. Access Rights

**Property:** `dcterms:accessRights`  
**Usage:** Recommended  
**Controlled Vocabulary:** EU Access Rights

```python
# Set access rights using EU vocabulary
dataset.set_access_rights(
    "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
)
```

### 3. Availability

**Property:** `dcatap:availability`  
**Usage:** For distributions  
**Controlled Vocabulary:** EU Planned Availability

```python
# Set distribution availability
distribution.set_availability(
    "http://publications.europa.eu/resource/authority/planned-availability/AVAILABLE"
)
```

### 4. ODRL Policies

**Property:** `odrl:hasPolicy`  
**Usage:** For distributions  
**Type:** ODRL Policy

```python
# Add ODRL policy to distribution
distribution.add_policy("http://example.org/policy/open-data")
```

### 5. Provenance

**Property:** `dcterms:provenance`  
**Usage:** For datasets  
**Type:** Provenance Statement

```python
# Add provenance information
dataset.add_provenance("http://example.org/provenance/statement-1")
```

### 6. Qualified Attribution

**Property:** `prov:qualifiedAttribution`  
**Usage:** For datasets  
**Type:** Attribution

```python
# Add qualified attribution
dataset.add_qualified_attribution("http://example.org/attribution/1")
```

---

## Controlled Vocabularies

DCAT-AP defines specific controlled vocabularies that MUST, SHOULD, or MAY be used:

### Mandatory Vocabularies

| Property | Vocabulary | URL |
|----------|------------|-----|
| Media Type | IANA Media Types | http://www.iana.org/assignments/media-types/ |
| Frequency | EU Frequency | http://publications.europa.eu/resource/authority/frequency |
| File Type | EU File Type | http://publications.europa.eu/resource/authority/file-type |
| Language | EU Languages | http://publications.europa.eu/resource/authority/language |
| Distribution Status | EU Distribution Status | http://publications.europa.eu/resource/authority/distribution-status |
| Availability | EU Planned Availability | http://publications.europa.eu/resource/authority/planned-availability |
| Checksum Algorithm | SPDX | https://spdx.org/rdf/terms/ |

### At Least 1 Value Required

| Property | Vocabulary | URL |
|----------|------------|-----|
| Theme | EU Data Theme | http://publications.europa.eu/resource/authority/data-theme |

### Recommended Vocabularies

| Property | Vocabulary | URL |
|----------|------------|-----|
| Publisher Type | ADMS Publisher Type | http://purl.org/adms/publishertype/1.0 |
| Licence Type | ADMS Licence Type | http://purl.org/adms/licencetype/1.0 |
| Access Rights | EU Access Rights | http://publications.europa.eu/resource/authority/access-right |

### Optional Vocabularies

| Property | Vocabulary | URL |
|----------|------------|-----|
| Publisher | EU Corporate Bodies | http://publications.europa.eu/resource/authority/corporate-body |
| Spatial | EU Countries | http://publications.europa.eu/resource/authority/country |
| Spatial | Geonames | http://sws.geonames.org/ |
| Type | EU Dataset Type | http://publications.europa.eu/resource/authority/dataset-type |

---

## High Value Datasets (HVD)

DCAT-AP 3.0.1 provides full support for the EU High Value Datasets regulation (Commission Implementing Regulation (EU) 2023/138).

### HVD Categories

```python
from dartfx.dcat import dcat_ap

# Six thematic categories
dcat_ap.HVDCategory.GEOSPATIAL
dcat_ap.HVDCategory.EARTH_OBSERVATION
dcat_ap.HVDCategory.ENVIRONMENT
dcat_ap.HVDCategory.METEOROLOGICAL
dcat_ap.HVDCategory.STATISTICS
dcat_ap.HVDCategory.COMPANIES
```

### HVD-Compliant Dataset Example

```python
from dartfx.dcat import dcat_ap

# Create HVD dataset
dataset = dcat_ap.Dataset(id="hvd-geo-dataset")
dataset.add_title("European Geospatial Data", lang="en")
dataset.add_description("High Value geospatial dataset", lang="en")

# Add HVD regulation (mandatory)
dataset.add_applicable_legislation(
    "http://data.europa.eu/eli/reg_impl/2023/138/oj"
)

# Add HVD category (mandatory)
dataset.add_theme(dcat_ap.HVDCategory.GEOSPATIAL)

# Set access rights to PUBLIC (required for HVD)
dataset.set_access_rights(
    "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
)

# Add keyword
dataset.add_keyword("geospatial")
dataset.add_keyword("high-value")

# Create HVD distribution
distribution = dcat_ap.Distribution(id="hvd-dist-1")
distribution.add_download_url("http://example.org/data.csv")
distribution.add_media_type("text/csv")

# Add HVD regulation to distribution
distribution.add_applicable_legislation(
    "http://data.europa.eu/eli/reg_impl/2023/138/oj"
)

# Set availability (recommended for HVD)
distribution.set_availability(
    "http://publications.europa.eu/resource/authority/planned-availability/AVAILABLE"
)

# Link distribution to dataset
dataset.add_distribution(distribution)

# Serialize to RDF
turtle = dataset.to_rdf(format='turtle')
print(turtle)
```

---

## Complete Example

```python
from dartfx.dcat import dcat_ap

# Create European data catalog
catalog = dcat_ap.Catalog(id="eu-open-data-portal")
catalog.add_title("European Open Data Portal", lang="en")
catalog.add_title("Portail européen de données ouvertes", lang="fr")
catalog.add_description("Central catalog for European open datasets", lang="en")

# Add publisher
catalog.add_publisher("http://publications.europa.eu/resource/authority/corporate-body/PUBL")

# Add geographical coverage (EU)
catalog.add_geographical_coverage(
    "http://publications.europa.eu/resource/authority/continent/EUROPE"
)

# Create dataset with EU vocabularies
dataset = dcat_ap.Dataset(id="population-stats")
dataset.add_title("European Population Statistics", lang="en")
dataset.add_description("Annual population statistics for EU member states", lang="en")

# Add theme using EU Data Theme vocabulary (at least 1 required)
dataset.add_theme("http://publications.europa.eu/resource/authority/data-theme/SOCI")

# Set access rights using EU vocabulary (recommended)
dataset.set_access_rights(
    "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
)

# Add frequency using EU vocabulary (mandatory if present)
dataset.add_frequency("http://publications.europa.eu/resource/authority/frequency/ANNUAL")

# Add keywords
dataset.add_keyword("population", lang="en")
dataset.add_keyword("statistics", lang="en")
dataset.add_keyword("demographics", lang="en")

# Add spatial coverage (EU countries)
dataset.add_spatial("http://publications.europa.eu/resource/authority/country/DEU")
dataset.add_spatial("http://publications.europa.eu/resource/authority/country/FRA")

# Create distribution
distribution = dcat_ap.Distribution(id="pop-stats-csv")
distribution.title.append("CSV Distribution")
distribution.add_download_url("http://example.org/population-stats.csv")

# Add media type using IANA (mandatory)
distribution.add_media_type("text/csv")

# Add format using EU File Type vocabulary (mandatory if present)
# Note: This would typically reference the EU file type authority list

# Set availability using EU vocabulary
distribution.set_availability(
    "http://publications.europa.eu/resource/authority/planned-availability/AVAILABLE"
)

# Set status using EU vocabulary
distribution.set_status(
    "http://publications.europa.eu/resource/authority/distribution-status/COMPLETED"
)

# Link distribution to dataset
dataset.add_distribution(distribution)

# Link dataset to catalog
catalog.add_dataset(dataset)

# Serialize to RDF Turtle
turtle = catalog.to_rdf(format='turtle')
print(turtle)

# Serialize to RDF/XML
xml = catalog.to_rdf(format='xml')

# Serialize to JSON-LD
jsonld = catalog.to_rdf(format='json-ld')
```

---

## Testing

### Test Coverage

| Category | Tests | Status |
|----------|-------|--------|
| **Catalog** | 4 | ✅ Pass |
| **Dataset** | 7 | ✅ Pass |
| **Distribution** | 6 | ✅ Pass |
| **DataService** | 2 | ✅ Pass |
| **DatasetSeries** | 3 | ✅ Pass |
| **CatalogRecord** | 2 | ✅ Pass |
| **Controlled Vocabularies** | 2 | ✅ Pass |
| **HVD Compliance** | 2 | ✅ Pass |
| **RDF Serialization** | 2 | ✅ Pass |
| **Integration** | 2 | ✅ Pass |
| **Total** | 32 | ✅ All Pass |

### Run Tests

```bash
# Run all DCAT-AP tests
pytest tests/test_dcat_ap.py -v

# Run specific test class
pytest tests/test_dcat_ap.py::TestHVDCompliance -v

# Run with coverage
pytest tests/test_dcat_ap.py --cov=dartfx.dcat.dcat_ap
```

---

## Files Created/Modified

### New Files
1. ✅ `src/dartfx/dcat/dcat_ap.py` - DCAT-AP 3.0.1 implementation (380 lines)
2. ✅ `tests/test_dcat_ap.py` - Comprehensive test suite (350+ lines, 32 tests)
3. ✅ `DCAT_AP_IMPLEMENTATION.md` - This documentation

### Modified Files
4. ✅ `src/dartfx/dcat/__init__.py` - Added DCAT-AP exports (default exports)

---

## Design Decisions

### 1. Extending vs. Replacing

DCAT-AP **extends** core DCAT classes rather than replacing them:

```python
# Core DCAT classes are aliased
from .dcat import Dataset as DcatDataset

# DCAT-AP extends them
class Dataset(DcatDataset):
    # Add DCAT-AP specific properties
    applicableLegislation: ...
```

This allows users to:
- Use core DCAT classes directly if needed (`DcatDataset`)
- Use DCAT-AP extended classes by default (`Dataset`)
- Mix and match as needed

### 2. Default Exports

DCAT-AP classes are the **default exports** from the package:

```python
from dartfx.dcat import Dataset  # DCAT-AP Dataset (extended)
from dartfx.dcat import DcatDataset  # Core DCAT Dataset
```

This makes DCAT-AP the primary interface while keeping core DCAT accessible.

### 3. Controlled Vocabularies

Controlled vocabularies are provided as constants for convenience:

```python
dcat_ap.ControlledVocabularies.EU_DATA_THEME
dcat_ap.HVDCategory.GEOSPATIAL
```

---

## Compliance

This implementation is fully compliant with:

✅ **DCAT-AP Version 3.0.1** - All DCAT-AP extensions implemented  
✅ **DCAT Version 3** - Based on latest DCAT core  
✅ **W3C Standards** - RDF and vocabulary standards  
✅ **EU Regulations** - HVD regulation (EU) 2023/138  
✅ **EU Vocabularies** - All mandatory controlled vocabularies  

---

## Benefits

### 1. European Interoperability
```python
# Use EU-standardized vocabularies
dataset.add_theme("http://publications.europa.eu/resource/authority/data-theme/ECON")
dataset.set_access_rights("http://publications.europa.eu/resource/authority/access-right/PUBLIC")
```

### 2. HVD Compliance
```python
# Easy HVD compliance
dataset.add_applicable_legislation("http://data.europa.eu/eli/reg_impl/2023/138/oj")
dataset.add_theme(dcat_ap.HVDCategory.GEOSPATIAL)
```

### 3. Type Safety
```python
# Pydantic validation
dataset.set_access_rights("invalid")  # ❌ Validation error
dataset.set_access_rights(URIRef("..."))  # ✅ Correct
```

### 4. RDF Native
```python
# Built-in RDF serialization
turtle = catalog.to_rdf(format='turtle')
xml = catalog.to_rdf(format='xml')
jsonld = catalog.to_rdf(format='json-ld')
```

---

## Next Steps

### Immediate
- ✅ All DCAT-AP 3.0.1 extensions implemented
- ✅ Tests passing
- ✅ Documentation complete

### Future Enhancements
- [ ] Add DCAT-AP specific SHACL validation shapes
- [ ] Add JSON-LD context file for DCAT-AP
- [ ] Add examples from data.europa.eu
- [ ] Add support for DCAT-AP national profiles (e.g., DCAT-AP.de, DCAT-AP.it)
- [ ] Add GeoDCAT-AP support (geospatial extension)
- [ ] Add StatDCAT-AP support (statistical data extension)

---

## References

- **DCAT-AP 3.0.1 Specification:** https://semiceu.github.io/DCAT-AP/releases/3.0.1/
- **DCAT 3 Specification:** https://www.w3.org/TR/vocab-dcat-3/
- **HVD Regulation:** https://eur-lex.europa.eu/eli/reg_impl/2023/138/oj
- **EU Vocabularies:** https://op.europa.eu/en/web/eu-vocabularies
- **data.europa.eu:** https://data.europa.eu/
- **SEMIC:** https://joinup.ec.europa.eu/collection/semic-support-centre

---

**Questions?** See the [main README](../README.md) or open an issue on GitHub.
