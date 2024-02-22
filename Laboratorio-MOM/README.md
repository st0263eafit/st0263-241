lanzar un servidor RabbitMQ en docker para estos ejemplos:

tutorial de: https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668

    docker run -d --hostname my-rabbit -p 15672:15672 -p 5672:5672 --name rabbit-server -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-management


Nota: recuerde abrir los puertos 5672 y 15672 en el Security Group de la máquina virtual.

# Recuerde tener previamente instalado python3 o verifique que ya este:

    si versión 3:

        python3 -V      (versión 3.x)

    sino, instalar:

        sudo apt install python3 -y

    sudo apt install python3-pip -y
    sudo pip3 install pika

# revisar todos estos tutoriales:

    https://www.rabbitmq.com/getstarted.html

# ejecutar programas python:

## COLAS: Cualquiera puede enviar, pero solo uno de los consumidores puede recibir

    //console1:
    python3 consumerQueue.py 
    
    //console2:
    python3 consumerQueue.py 
    
    //console3: (ejecuta varias veces este comando, y notará que las recepciones por los consumidores es alternada)
    python3 producerQueue.py

## TOPICOS con clave (key): Cualquiera puede enviar, todos los consumidores de un tópico reciben.

    //console1:
    python3 receive_logs_topic.py key1
    
    //console2:
    python3 receive_logs_topic.py key1
    
    //console3: (ejecuta varias veces este comando, y notará que las recepciones por los consumidores es alternada)
    python3 emit_logs_topic.py key1 hola mundo cruel

## TOPICOS sin clave (key) - FANOUT: Cualquiera puede enviar, todos los consumidores de un tópico reciben sin necesidad de especificar una clave de filtrado de mensajes

    //console1:
    python3 receive_logs_fanout.py
    
    //console2:
    python3 receive_logs_fanout.py
    
    //console3: (ejecuta varias veces este comando, y notará que las recepciones por los consumidores es alternada)
    python3 emit_logs_fanout.py hola mundo cruel
    