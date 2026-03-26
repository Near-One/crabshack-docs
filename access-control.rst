Access Control
==============

Instance owners can grant other users access.

List Access
-----------

.. code-block:: text

   GET /instances/{name}/access

**Response** ``200``:

.. code-block:: json

   [
     { "user_id": "abc123", "role": "owner",  "granted_at": "2026-03-20T12:00:00Z" },
     { "user_id": "def456", "role": "member", "granted_at": "2026-03-20T13:00:00Z" }
   ]

Grant Access
------------

.. code-block:: text

   POST /instances/{name}/access

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Field
     - Type
     - Required
     - Default
   * - ``user_id``
     - string
     - yes
     - --
   * - ``role``
     - string
     - no
     - ``member``

**Response** ``200``:

.. code-block:: json

   { "ok": true, "instance": "bafom-kidux", "user_id": "def456", "role": "member" }

Revoke Access
-------------

.. code-block:: text

   DELETE /instances/{name}/access/{user_id}

**Response** ``200``:

.. code-block:: json

   { "ok": true }

Permissions by Role
-------------------

.. list-table::
   :header-rows: 1
   :widths: 50 25 25

   * - Action
     - Owner
     - Member
   * - View instance, logs, stats, SSH info
     - Yes
     - Yes
   * - Stop / start / restart
     - Yes
     - Yes
   * - Create backup
     - Yes
     - Yes
   * - Restore from backup
     - Yes
     - No
   * - Delete instance
     - Yes
     - No
   * - Manage access
     - Yes
     - No
