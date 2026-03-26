Instances
=========

.. _create-instance:

Create Instance (SSE)
---------------------

.. code-block:: text

   POST /instances

.. list-table::
   :header-rows: 1
   :widths: 20 10 10 60

   * - Field
     - Type
     - Required
     - Description
   * - ``nearai_api_key``
     - string
     - yes
     - API key passed to the agent
   * - ``nearai_api_url``
     - string
     - yes
     - API URL passed to the agent
   * - ``image``
     - string
     - yes
     - Container image reference
   * - ``service_type``
     - string
     - yes
     - ``openclaw`` or ``ironclaw-dind``
   * - ``mem_limit``
     - string
     - yes
     - Memory limit (e.g. ``4g``)
   * - ``cpus``
     - string
     - yes
     - CPU allocation (e.g. ``1``)
   * - ``storage_size``
     - string
     - yes
     - Disk allocation (e.g. ``10G``)
   * - ``ssh_pubkey``
     - string
     - yes
     - SSH public key for agent access
   * - ``node_id``
     - string
     - no
     - Pin to a specific node
   * - ``backup_passphrase``
     - string
     - no
     - Unlock vault on creation

**SSE events** (in order):

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Event
     - Data
     - Description
   * - ``created``
     - ``{name, node, gatewayPort, sshPort, wsPort}``
     - Instance allocated
   * - ``container_starting``
     - ``{name, image}``
     - Container deploying
   * - ``healthy``
     - ``{name}``
     - Health check passed
   * - ``egress_applied``
     - ``{name}``
     - Network rules applied
   * - ``ready``
     - ``{name}``
     - Instance is running
   * - ``error``
     - ``{message}``
     - Creation failed

The creating user automatically becomes the instance **owner**.

List Instances
--------------

.. code-block:: text

   GET /instances

Returns instances the authenticated user has access to. Admin token returns all
instances.

**Response** ``200``:

.. code-block:: json

   [
     {
       "name": "bafom-kidux",
       "status": "running",
       "image": "ironclaw-dind:latest",
       "service_type": "ironclaw-dind",
       "node_id": "node-1",
       "gateway_port": 19001,
       "ssh_port": 19002,
       "ws_port": 19003,
       "mem_limit": "4g",
       "cpus": "1",
       "storage_size": "10G",
       "created_at": "2026-03-20T12:00:00.000Z"
     }
   ]

.. _get-instance:

Get Instance
------------

.. code-block:: text

   GET /instances/{name}

**Response** ``200``: Same shape as list item, with all fields.

Stop Instance (SSE)
-------------------

.. code-block:: text

   POST /instances/{name}/stop

**SSE events**: ``stopped`` → terminal. Or ``error``.

Start Instance (SSE)
--------------------

.. code-block:: text

   POST /instances/{name}/start

Optional body: ``{"backup_passphrase": "..."}`` to re-unlock vault.

**SSE events**: ``container_starting`` → ``egress_applied`` → ``ready``. Or
``error``.

Restart Instance (SSE)
----------------------

.. code-block:: text

   POST /instances/{name}/restart

Optional body: ``{"image": "new-image:tag"}`` to upgrade the image.

**SSE events**: ``restarting`` → ``stopped`` → ``container_starting`` →
``healthy`` → ``egress_applied`` → ``ready``. Or ``error``.

Delete Instance (SSE)
---------------------

.. code-block:: text

   DELETE /instances/{name}
   DELETE /instances/{name}?purge=false

Default ``purge=true`` removes all persistent data. Set ``purge=false`` to keep
volumes.

**SSE events**: ``deleted`` with ``{name, purge}``. Or ``error``.
