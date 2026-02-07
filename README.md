# DCAT

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/DataArtifex/dcat-toolkit)
[![PyPI - Version](https://img.shields.io/pypi/v/dartfx-dcat.svg)](https://pypi.org/project/dartfx-dcat)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dartfx-dcat.svg)](https://pypi.org/project/dartfx-dcat)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)

**This project is in its early development stages, so stability is not guaranteed, and documentation is limited. We welcome your feedback and contributions as we refine and expand this project together!**

## Overview

This project provides a Python toolkit for working with DCAT (Data Catalog Vocabulary), an RDF vocabulary designed for interoperability between data catalogs published on the Web. The toolkit implements the W3C DCAT standard using **Pydantic models** and provides utilities for creating, manipulating, and serializing DCAT metadata.

**Key Features:**
- **Pydantic-based models** with full validation and type safety
- Python implementation of DCAT classes (Catalog, Dataset, Distribution, DataService, etc.)
- Support for DCAT 3.0 specification
- **RDF serialization/deserialization** support via rdflib (Turtle, RDF/XML, JSON-LD, N-Triples)
- **Round-trip conversion** between Python objects and RDF
- Type-safe API with comprehensive type hints
- Support for DCAT Application Profiles (DCAT-AP, DCAT-US, DCAT-AP-HVD)


## Installation

### PyPI Release

Once stable, this package will be officially released and distributed through [PyPI](https://pypi.org/). Stay tuned for updates!

### Local Installation

In the meantime, you can install the package locally by following these steps:

1. **Clone the Repository:**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/DataArtifex/dcat-toolkit.git
   cd dcat-toolkit
   ```

2. **Install the Package:**

   From the project's home directory, run the following command to install the package:

   ```bash
   pip install -e .
   ```

### Installing Dependencies

To install the required dependencies, execute the following command:

```bash
pip install -r requirements.txt
```

Make sure you are in the project's root directory when running these commands.

Feel free to replace `<repository-url>` and `<repository-directory>` with the actual URL and directory name of your project. This enhanced version provides clear instructions and formatting to guide users through the installation process effectively.

 
## Usage

Here's a quick example of how to create a DCAT catalog with a dataset:

```python
from dartfx.dcat import dcat

# Create a catalog
catalog = dcat.Catalog(id="my-catalog")
catalog.add_title("My Data Catalog", lang="en")
catalog.add_description("A catalog of open datasets", lang="en")

# Create a dataset
dataset = dcat.Dataset(id="dataset-1")
dataset.add_title("Population Statistics", lang="en")
dataset.add_description("Annual population statistics by region", lang="en")
dataset.add_keyword("population")
dataset.add_keyword("statistics")
dataset.add_theme("http://example.org/themes/demographics")

# Create a distribution
distribution = dcat.Distribution(id="dist-1")
distribution.title.append("CSV Distribution")
distribution.add_download_url("http://example.org/data/population.csv")
distribution.add_media_type("text/csv")

# Link them together
dataset.add_distribution(distribution)
catalog.add_dataset(dataset)

# Serialize to RDF Turtle format
turtle = catalog.to_rdf(format='turtle')
print(turtle)

# Serialize to RDF/XML
xml = catalog.to_rdf(format='xml')

# Get the RDF graph directly
graph = catalog.to_rdf_graph()

# Deserialize from RDF
from rdflib import URIRef
subject = URIRef("http://www.w3.org/ns/dcat#my-catalog")
restored_catalog = dcat.Catalog.from_rdf(turtle, format='turtle', subject=subject)
```

### Key Features

- **Pydantic-based Models**: Full validation and type safety
- **RDF Serialization**: Convert to Turtle, RDF/XML, JSON-LD, N-Triples
- **RDF Deserialization**: Load DCAT metadata from RDF formats
- **Round-trip Support**: Lossless conversion between Python objects and RDF
- **Type Hints**: Complete type annotations for better IDE support

For more examples and detailed documentation, see the [documentation](https://github.com/DataArtifex/dcat-toolkit#readme).

## Roadmap

...

## Contributing
 
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

 
## License
 
The MIT License (MIT)

Copyright (c) 2024 Pascal L.G.A. Heus

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


