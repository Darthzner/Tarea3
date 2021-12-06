# Tarea3: Sistemas Distribuidos
## Integrantes:
  - Miguel Contreras
  - Lester Carrasco
  - Nicolas Poza

## Descripcion
En este proyecto se implementa un balanceador de carga, el cual distribuye la carga entrante en un endpoint entre tres endpoints utilizando:
  - Nginx
  - Flask
Los endpoints escriben/leen data desde una base de datos utilizando **Postgres** replicadas, de modo que las operaciones CUD se realicen sobre una base de datos
master y la lectura se realice sobre una base de atos slave, quedando configurada de la siguiente forma:

![image](https://user-images.githubusercontent.com/32967596/144809010-f90b2322-fc88-4afc-9f68-687a4e08c28c.png)

## Technical
  - Nginx actua como servicio exponiendo el puerto 8080 para realizar consultas
  - El trafico desde Nginx es redirigido a endpoints utilizando el puerto 3050
  - Las APIs realizan CUD en la base de datos utilinzando el puerto 5432
  - Las APIs realizan Read en la base de datos utilinzando el puerto 5432
## Uso
Primero, clonamos el proyecto y lo alojamos en una carpeta:
```
git clone https://github.com/Darthzner/Tarea3-SistDist.git
mv nginx-go-postgres-loadbalancer sist3
cd sist3
docker-compose up
```
Una vez terminada la configuracion, tenemos un endpoint disponible en ```http://localhost:8080/``` sobre el cual podemos realizar dos operaciones:
### [GET] /api/getprod/pname
Retorna la informacion de un producto _pname_

### [POST] /api/addprod
Inserts un producto de la forma:
```
{
    "name": "Tutorial del pasito de Marcianeke",
    "precio": "69420",
}

```
