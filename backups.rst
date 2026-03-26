Backups
=======

.. admonition:: Under Development

   Backup and restore is under active development. The API contract below is
   stable and not expected to change, but the feature may not be available in all
   environments yet.

Create Backup (SSE)
-------------------

.. code-block:: text

   POST /instances/{name}/backup

Requires vault to be unlocked (login with ``backup_passphrase``).

**SSE events**:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Event
     - Data
   * - ``backup_started``
     - ``{backup_id, instance}``
   * - ``status``
     - ``{step: "preparing_encryption"}``
   * - ``status``
     - ``{step: "encrypting_uploading"}``
   * - ``backup_complete``
     - ``{backup_id, size_bytes, s3_key, encrypted: true}``
   * - ``error``
     - ``{message}``

List Backups
------------

.. code-block:: text

   GET /instances/{name}/backups

.. code-block:: json

   [
     {
       "id": "01JQXYZ...",
       "instance_name": "bafom-kidux",
       "status": "ready",
       "size_bytes": 1048576,
       "created_at": "2026-03-20T14:00:00Z"
     }
   ]

Download Backup
---------------

.. code-block:: text

   GET /instances/{name}/backups/{id}/download

Returns ``409`` if backup is not ``ready``.

.. code-block:: json

   {
     "url": "https://s3.example.com/...",
     "expires_in": 3600
   }

Delete Backup
-------------

.. code-block:: text

   DELETE /instances/{name}/backups/{id}

.. code-block:: json

   { "deleted": "01JQXYZ..." }

Restore Backup (SSE)
--------------------

.. code-block:: text

   POST /instances/{name}/restore/{backupId}

Owner only. Requires vault unlocked.

**SSE events**:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Event
     - Data
   * - ``restore_started``
     - ``{backup_id, instance}``
   * - ``status``
     - ``{step: "stopping_container"}``
   * - ``status``
     - ``{step: "preparing_decryption"}``
   * - ``status``
     - ``{step: "decrypting_extracting"}``
   * - ``status``
     - ``{step: "starting_container"}``
   * - ``restore_complete``
     - ``{backup_id, instance}``
   * - ``error``
     - ``{message}``
