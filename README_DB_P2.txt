---------------------------------------------------------------------------
In order to access this system go to:
localhost:5000/api/
---------------------------------------------------------------------------
An example of different things to ask the database

localhost:5000/api/resources
localhost:5000/api/resources?rname='panadol'

----------------------------------------------------------------------------
In order to test different aspects asked for this phase, we can use
these queries:
----------------------------------------------------------------------------
1.     Register as a system administrator.

http://localhost:5000/api/users?isAdmin=true

2.     Register as a person in need of resources.

http://localhost:5000/api/requesters

3.     Register as a person that supplies resources.

http://localhost:5000/api/suppliers

4.     Add a request for a given resource

http://localhost:5000/api/requests?rname=

5.     Announce the availability of a resource.

http://localhost:5000/api/announcements?rname=

6.     Reserve or purchase a resource. Free resources are reserved.  Otherwise, they are purchased.

http://localhost:5000/api/purchases?isReserved=

7.     Browse resources being requested

http://localhost:5000/api/requests


8.     Browse resources available

http://localhost:5000/api/stocks/inStock='true'

9.     Keyword search resources being requested, with sorting by resource name

http://localhost:5000/api/requests?{"rid", "rname", "catname", "catid"}

10.  Keyword search resources available, with sorting by resource name

http://localhost:5000/api/stocks?rname=panadol&min-qtysum=1

14. Encontrar productos de un suplidor

http://localhost:5000/api/suppliers/1/stocks

15. Encontrar suplidores para un producto dado (e.g., diesel)

http://localhost:5000/api/suppliers?rname=

16. Encontar un producto especifico en una zona (e.g., pampers en San Juan)

http://localhost:5000/api/resources?region=
http://localhost:5000/api/stocks?region=

17. Encontrar las ordenes de una persona (compras o productos gratis)

http://localhost:5000/api/users/6/purchases


18. Encontrar las ordenes servidas por un suplidor.

http://localhost:5000/api/suppliers/1/transactions


-------------------------------------------------------------------------------
project is availble in heroku in :

https://hurricanereliefbe.herokuapp.com/api
