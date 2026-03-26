Gateway Proxy
=============

.. code-block:: text

   GET /agents/{name}/gateway/
   GET /agents/{name}/gateway/{path}

No authentication required on the proxy path itself -- the agent gateway
validates access using its instance token.

Proxies HTTP and WebSocket traffic to the agent's built-in web interface.

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Status
     - Meaning
   * - ``200``
     - Proxied response from agent
   * - ``404``
     - Instance not found
   * - ``502``
     - Agent gateway unreachable
   * - ``503``
     - Instance not running (includes ``Retry-After: 30`` header)
