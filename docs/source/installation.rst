Installation
============

Requirements
------------

- Python 3.12 or higher
- pip package manager

Install from PyPI
-----------------

.. code-block:: bash

   pip install dartfx-dcat

Install from Source
-------------------

.. code-block:: bash

   git clone https://github.com/DataArtifex/dcat-toolkit.git
   cd dcat-toolkit
   pip install -e .

Development Installation
------------------------

For development, use ``uv`` with the ``dev`` dependency group:

.. code-block:: bash

   uv sync --group dev
   uv run --with pre-commit pre-commit install

Run all hooks locally before committing:

.. code-block:: bash

   uv run --with pre-commit pre-commit run --all-files

The development setup includes:

- pytest
- ruff (linting)
- mypy (type checking)
- pre-commit hooks

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
