1) Registrar usuarios (supplier o persona normal)

/api/users

User POST
{ "username": "pablo52",
  "firstName": "Pablo",
  "lastName": "Rodriguez",
  "email": "pablo.rodriguez@g.com",
  "phone": "7874479978",
  "password": "dbmaster",
  "address": {
      "address1": "calle 367, km 1.6",
      "address2": "",
      "city": "Sabana Grande",
      "country": "Puerto Rico",
      "region": "Mayaguez",
      "zipcode": "00637"
  }
  }

/api/users

Supplier POST

{
  "uid":4
}

2) Añadir recursos

{
	"rname":"Huggies",
	"catId":2
}

3) Anunciar Recursos

/api/suppliers/2/announcements

Announcement Post

{
  "rid":1,
  "qty":4,
  "priceattime":50
}
{
  "rname":"medalla",
  "qty":30,
  "priceattime":3.00,
  "catid":2
}

4) Solicitar Recursos

/api/requesters/2/requests

Announcement POST

{
  "rid":1,
  "qty":4
}
{
  "rname":"medalla",
  "qty":30,
  "catid":2
}

5) Comprar recursos


/api/transactions
{
  "piId": 4,
  "transactions": [
    {
      "sid": 4,
      "rid": 20,
      "qty": 30
    }
  ]
}

6) Recibir recuros q son gratis

/api/transactions

{
  "piId": 4,
  "transactions": [
    {
      "sid": 4,
      "rid": 20,
      "qty": 30
    }
  ]
}

7) Ver transaccion de compra de un recurso

/api/users/2/purchases

/api/suppliers/2/transactions

/api/transactions


8) Añadir metodo de pago para un client

/api/users/2/paymentinfo

{
  "ccNum": "1234567810101010",
  "expirationDate": "2018-02-02",
  "address": {
      "address1": "calle 367, km 1.6",
      "address2": null,
      "city": "Sabana Grande",
      "country": "Puerto Rico",
      "region": "Mayaguez",
      "zipcode": "00637"
      }
}

9) Cambiar la informacion de un producto


/api/resources/1

{
  "rname":"medalla",
  "catid":2
}

10) Actualizar la informacion de Tarjeta de Credito

/api/users/2/paymentinfo


{
  "ccNum": "1234567810101010",
  "expirationDate": "2018-02-02",
  "address": {
      "address1": "calle 367, km 1.6",
      "address2": null,
      "city": "Sabana Grande",
      "country": "Puerto Rico",
      "region": "Mayaguez",
      "zipcode": "00637"
      }
}
