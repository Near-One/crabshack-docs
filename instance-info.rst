Instance Information
====================

Logs
----

.. code-block:: text

   GET /instances/{name}/logs?tail=100
   GET /instances/{name}/logs?follow=true

Non-streaming response:

.. code-block:: json

   {
     "name": "bafom-kidux",
     "logs": "2026-03-20 Starting agent...\n..."
   }

With ``follow=true``, returns an SSE stream of live log lines.

Stats
-----

.. code-block:: text

   GET /instances/{name}/stats

.. code-block:: json

   {
     "name": "bafom-kidux",
     "stats": {
       "CPUPerc": "0.50%",
       "MemUsage": "128MiB / 4GiB",
       "NetIO": "1.2kB / 3.4kB"
     }
   }

SSH Connection Info
-------------------

.. code-block:: text

   GET /instances/{name}/ssh

.. code-block:: json

   {
     "host": "203.0.113.10",
     "port": 19002,
     "user": "agent",
     "command": "ssh -p 19002 agent@203.0.113.10"
   }
