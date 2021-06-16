#!/usr/bin/env bash

curl -i -X POST -H "Content-Type: application/json" -d '{"company":"evo","username":"samu","password":"1234abc"}' http://127.0.0.1:5000/api/signup >> /dev/null
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"no_acount":"341412022993",names":"Felipe","forenames":"Sierra","c_type":"Prestacion de Servicios","id":"101","position":"ps","eps":"Famisanar"}' http://127.0.0.1:5000/api/employees >> /dev/null
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"no_acount":"341412022113","names":"Samuel","forenames":"Correa","c_type":"Termino Indefinido","id":"100","position":"oficina","eps":"Famisanar"}' http://127.0.0.1:5000/api/employees >> /dev/null
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"no_acount":"341412001223","names":"Jesus","forenames":"Correa","c_type":"Termino Indefinido","id":"102","position":"algo","eps":"Famisanar"}' http://127.0.0.1:5000/api/employees >> /dev/null
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"no_acount":"341414120223","name":"item 1","description":"Lorem ipsump","unit_value":2000000}' http://127.0.0.1:5000/api/100/items >> /dev/null
curl -i -u samu:1234abc -X POST -H "Content-Type: application/json" -d '{"type":"Horas extra","description":"Horas extra","value":300000}' http://127.0.0.1:5000/api/100/bonuses >> /dev/null
curl -i -u samu:1234abc -X GET http://127.0.0.1:5000/api/employees
