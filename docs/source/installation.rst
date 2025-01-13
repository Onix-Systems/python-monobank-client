Installation
=============
**This framework is published at the PyPI, install it with pip:**

1. This package makes it possible to use module methods in synchronous frameworks:

   .. code-block:: bash

      pip install monobank-api-client[http]

2. This package makes it possible to use module methods in asynchronous frameworks:

   .. code-block:: bash

      pip install monobank-api-client[aio]

3. This package makes it possible to use ready-made views with a synchronous script based on the Django Rest framework:

   .. code-block:: bash

      pip install monobank-api-client[drf]

To get started, add the following packages to ``INSTALLED_APPS``:

   .. code-block:: python

      INSTALLED_APPS = [
      ...
      'rest_framework',
      'drf_mono',
      ]

Include ``drf_mono`` urls to your ``urls.py``:

   .. code-block:: python

      urlpatterns = [
          ...
          path('mono/', include('drf_mono.urls', namespace='drf_mono')),
      ]

4. This package makes it possible to use ready-made routers with an asynchronous script based on the FastAPI framework:

   .. code-block:: python

      pip install monobank-api-client[fastapi]

5. To install all packages at once:

   .. code-block:: python

      pip install monobank-api-client[all]
