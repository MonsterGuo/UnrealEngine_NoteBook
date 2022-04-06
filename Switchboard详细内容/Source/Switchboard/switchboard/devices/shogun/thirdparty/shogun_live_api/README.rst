Shogun Live API
===============

This module provides the services that are used to access application functionality.
    
Services functions and callbacks made available by the host application to Vicon Core API users. Services are 
responsible for serializing user data into JSON for transmission to the Vicon Core API server, and deserializing the replies 
back into user data.

Services are automatically generated for each version of the Vicon host application. It is possible to connect a particular 
version of services to a different version of host application, but some functionality may not be supported.
