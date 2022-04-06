1.1.4
=====

C#
* No changes.

Python
* Added implementation of __repr__ to Result.


1.1.3 (2019-04-17)
==================

C#
* Fixed ClientProvider sending two disconnection events when the server closes a connection, and creating an extra client connection on retry.

Python
* No changes.


1.1.2 (2018-11-15)
==================

C#
* Changed callback registration to avoid a deadlock occurring when a callback is triggered on one thread while registering for a callback on another thread.

Python
* No changes.


1.1.1 (2018-10-24)
==================

C#
* Disabled warning in Client.InitialiseConnectionAsync.

Python
* Added method to de-register a schema type to SchemaServices.


1.1.0 (2018-07-23)
==================

C#
* Fixed NullReferenceException if Client.ErrorEvent is not subscribed when an error occurs.
* ClientProvider will reconnect if network cable is unplugged and plugged back in.

Python
* No changes


1.0.0 (2018-06-13)
==================

* Initial release of Vicon Core API.
