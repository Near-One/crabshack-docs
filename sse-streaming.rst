SSE Streaming
=============

Lifecycle operations (create, stop, start, restart, delete, backup, restore)
return **Server-Sent Events** streams:

.. code-block:: text

   Content-Type: text/event-stream

Each event has a name and JSON data. The stream always ends with a terminal
event -- either a success event (e.g. ``ready``, ``stopped``, ``deleted``) or
``error``. Keepalive comments (``: keepalive``) are sent every 3 seconds.

If the client disconnects mid-stream, the operation continues server-side. Poll
:ref:`GET /instances/{name} <get-instance>` to check the final state.
