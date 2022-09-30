# TwettsGraph

:construction: En desarrollo :construction:

TwettsGraph de modelar, simular y monitorio en el cual de centar en una tematica en especifico, en busca de generar conocimiento en base a la opinion de las personas sobre un tema en espceifico en la red solcial twitter, en nuestro caso nos enfocamos en la opinion de las sobre el nuevo iphone 14, con el cual poder ver que tan aceptado u odiado es el producto y cuantas personas estan hablando al respecto, ademas `#TwettsGraph` ofreve un cuadro de mando integral o _Dashboard_ donde incluimos la opcion de ver la _Red de seguidores de un usuario_, _Ver la pocision grografica de donde fue publicado un Twett_ y  _Ver las zonas donde mas se ha twetteado_ sobre el tema en cuestion esto gracias a un mapa de calor.


# Pre-requisistos

Antes de poder descargar e inicializar este repositorio es necesario que verifiquemos si tenemos de `#python` instalado correcctamente en nuestro pc y con el gestor de paquetes de python `Pip`


# Iniciando el proyecto

Luego de haber descargado el repositorio es necesario que creeemos un entorno o _environment_ virtual lo cual es necesario para porder arrancar el proyecto, lo hacemos con el siguiente comando: 

```
python -m venv .venv
```

Luego de ya tener nuestro entorno virtual creado y activado, podemos instalar todas las dependencias en nuestro entorno virtual para evitar conflictos, dado el caso que no se halla configurado bien el entorno virtual, los paquetes o recursos se instalaran en la maquina o pc por defecto

```
pip install -r requirements.txt
```

Ya con esto podemos hacer migraciones previas a la base de datos (Por el momento se usa sqlLite) y se usa el siguiente comando:  

```
python manage.py migrate authApp
```

Y ejecutamos o levantamos nuestra app: 

```
python manage.py runserver
```




