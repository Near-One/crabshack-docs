User Management
===============

.. _register:

Register
--------

.. code-block:: text

   POST /auth/register

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Field
     - Type
     - Required
     - Description
   * - ``auth_secret``
     - string
     - yes
     - 64 hex characters. Used to derive your user ID.
   * - ``backup_passphrase``
     - string
     - yes
     - Passphrase for encrypting/decrypting backups.
   * - ``ssh_pubkey``
     - string
     - no
     - SSH public key (e.g. ``ssh-ed25519 AAAA...``)
   * - ``display_name``
     - string
     - no
     - Display name

**Response** ``201``:

.. code-block:: json

   {
     "user_id": "abc123...",
     "session_token": "eyJ..."
   }

.. _login:

Login
-----

.. code-block:: text

   POST /auth/login

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Field
     - Type
     - Required
   * - ``auth_secret``
     - string
     - yes
   * - ``backup_passphrase``
     - string
     - yes

**Response** ``200``:

.. code-block:: json

   {
     "user_id": "abc123...",
     "session_token": "eyJ..."
   }

Login also unlocks the encryption vault, enabling backup and restore operations.

Logout
------

.. code-block:: text

   POST /auth/logout

**Response** ``200``:

.. code-block:: json

   { "ok": true }

Get Profile
-----------

.. code-block:: text

   GET /auth/me

**Response** ``200``:

.. code-block:: json

   {
     "user_id": "abc123...",
     "ssh_pubkey": "ssh-ed25519 AAAA...",
     "display_name": "Alice",
     "vault_unlocked": true,
     "created_at": "2026-03-20T12:00:00.000Z"
   }

Update Profile
--------------

.. code-block:: text

   PATCH /auth/me

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Field
     - Type
     - Required
   * - ``display_name``
     - string
     - no
   * - ``ssh_pubkey``
     - string
     - no

**Response** ``200``:

.. code-block:: json

   {
     "user_id": "abc123...",
     "ssh_pubkey": "ssh-ed25519 AAAA...",
     "display_name": "Alice"
   }
