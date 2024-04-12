# 1. en una máquina AWS EC2 nueva y con la dirección IP Elastica de esa máquina, cree las entradas en el DNS:

    sudominio.com -> IP Elastica
    www.sudominio.com -> misma IP Elastica

# 2. instale certbot:

    sudo amazon-linux-extras install epel -y
    sudo yum install certbot-nginx -y
    sudo yum install nginx -y

# 3.0 generar sus propios certificados SSL sin una CA:

    sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ssl/nginx.key -out ssl/nginx.crt
    
        Renombre los archivos: nginx.key y nginx.crt a los correspondientes privkey.pem y fullchain.pem en el directorio: /home/ec2-user/wordpress/ssl/

# 3.1 Ejecute certbot para pedir certificado SSL para registros especificos:

    sudo certbot --nginx certonly -d www.sudominio.com -d sudominio.com

# 3.2  Ejecute certbot para pedir certificado SSL para todo el dominio (wildcard):

ref: https://medium.com/@utkarsh_verma/how-to-obtain-a-wildcard-ssl-certificate-from-lets-encrypt-and-setup-nginx-to-use-wildcard-cfb050c8b33f

    sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.sudominio.com --manual --preferred-challenges dns-01 certonly

Este comando queda pausado indicando que debe crear un registro TXT en su dominio, una vez lo cree y verifique, dele ENTER para Continuar. Debe terminar con éxito.

# 4. cree el los archivos docker-compose

    mkdir /home/ec2-user/wordpress
    mkdir /home/ec2-user/wordpress/ssl
    sudo su

### comando para registros especificos (ej: www):
    cp /etc/letsencrypt/live/www.sudominio.com/* /home/ec2-user/wordpress/ssl/

### comando para wildcard (*.sudominio.com):
    cp /etc/letsencrypt/live/sudominio.com/* /home/ec2-user/wordpress/ssl/

    cp /etc/letsencrypt/options-ssl-nginx.conf /home/ec2-user/wordpress/ssl/
    cp /etc/letsencrypt/ssl-dhparams.pem /home/ec2-user/wordpress/ssl/
    exit

###     Nota: estas instrucciones son para nginx, pero si se requiere para haproxy:

        DOMAIN='sudominio.com' bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/letsencrypt/$DOMAIN.pem'

        cp /etc/letsencrypt/live/sudominio.com/* /home/ec2-user/wordpress/ssl/

        exit

# 5. instalar docker y docker-compose en AMI Ubuntu:22.04

    sudo apt install docker.io -y
    sudo apt install docker-compose -y
    sudo apt install git -y

    sudo systemctl enable docker
    sudo systemctl start docker
    sudo usermod -a -G docker ubuntu

# 6. copie los archivos del docker al sitio propio e inicie

despues de clonar este repositorio en el destino:

    git clone https://github.com/st0263eafit/st0263-232.git

    cd st0263-2023-2/docker-nginx-wordpress-ssl-letsencrypt
    sudo cp docker-compose.yml /home/ec2-user/wordpress
    sudo cp nginx.conf /home/ec2-user/wordpress
    sudo cp ssl.conf /home/ec2-user/wordpress

# 7. inicie el servidor de wordpress en docker.

VERIFIQUE QUE NO ESTE CORRIENDO nginx NATIVO EN LA MÁQUINA, detengalo!!!!

    ps ax | grep nginx
    netstat -an | grep 80

    sudo reboot

vuelve y se conecta a la máquina para que ese proceso no esté corriendo.

UNA VEZ DETENIDO:

    cd /home/ec2-user/wordpress
    docker-compose up --build -d

# 8. pruebe desde un browser:

    https://sudominio.com o https://www.sudominio.com

# 9.  FELICITACIONES, lo logro!!!!!
