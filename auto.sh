#!/usr/bin/env bash

curl -i -X POST -H "Content-Type: application/json" -d '{"company":"evo","username":"samu","password":"1234abc"}' http://127.0.0.1:5000/api/signup >> /dev/null
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"names":"Felipe","forenames":"Sierra","contract_type":"Prestacion de Servicios","dni":"101","position":"ps"}' http://127.0.0.1:5000/api/employees >> /dev/null
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"names":"Samuel","forenames":"Correa","contract_type":"Termino Indefinido","dni":"100","position":"oficina"}' http://127.0.0.1:5000/api/employees >> /dev/null
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"names":"Jesus","forenames":"Correa","contract_type":"Termino Indefinido","dni":"102","position":"algo"}' http://127.0.0.1:5000/api/employees >> /dev/null
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"name":"item 1","description":"Lorem ipsump","unit_value":2000000}' http://127.0.0.1:5000/api/100/items >> /dev/null
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"type":"Horas extra","description":"Horas extra","value":300000}' http://127.0.0.1:5000/api/100/bonuses >> /dev/null
curl -i -u samu:1234abc -X GET http://127.0.0.1:5000/api/employees
