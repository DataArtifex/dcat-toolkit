Installation
============

Requirements
------------

- Python 3.12 or higher
- pip package manager

Install from PyPI
-----------------

.. code-block:: bash

   pip install dcat-toolkit

Install from Source
-------------------

.. code-block:: bash

   git clone https://github.com/yourusername/dcat-toolkit.git
   cd dcat-toolkit
   pip install -e .

Development Installation
------------------------

For development, install with test dependencies:

.. code-block:: bash

   pip install -e ".[dev]"

This installs additional packages for testing and development:

- pytest
- pytest-cov
- ruff (linting)
- mypy (type checking)

Verify Installation
-------------------

.. code-block:: python

   import dartfx.dcat
   print(dartfx.dcat.__version__)

Dependencies
------------

The DCAT Toolkit requires the following packages:

- **rdflib** - RDF library for Python
- **pydantic** - Data validation using Python type hints
- **python-dateutil** - Extensions to the standard datetime module

All dependencies are automatically installed with the package.
