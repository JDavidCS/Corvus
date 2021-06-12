#!/usr/bin/env bash

curl -i -X POST -H "Content-Type: application/json" -d '{"company":"evo","username":"samu","password":"1234abc"}' http://127.0.0.1:5000/api/signup
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"names":"Felipe","forenames":"Sierra","contract_type":"Prestacion de Servicios","dni":"101","position":"ps"}' http://127.0.0.1:5000/api/employees
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"names":"Samuel","forenames":"Correa","contract_type":"Termino Indefinido","dni":"100","position":"oficina"}' http://127.0.0.1:5000/api/employees
