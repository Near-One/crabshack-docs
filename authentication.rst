Authentication
==============

All endpoints (except the :doc:`gateway proxy <gateway-proxy>`) require a bearer
token:

.. code-block:: text

   Authorization: Bearer <token>

Token Types
-----------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Type
     - Description
   * - **Admin token**
     - Full access to all resources. Provided during onboarding.
   * - **Session token**
     - Scoped to a single user's resources. Obtained via :ref:`login <login>`.

.. _errors:

Errors
------

All errors return JSON:

.. code-block:: json

   { "error": "Human-readable message" }

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Status
     - Meaning
   * - ``400``
     - Invalid request (missing fields, validation failure)
   * - ``401``
     - Missing or invalid token
   * - ``403``
     - Insufficient permissions
   * - ``404``
     - Resource not found
   * - ``409``
     - Conflict (e.g. backup not ready for download)
   * - ``501``
     - Feature not configured (e.g. S3 for backups)
