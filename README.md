# django-amat-dati

Progetto Django per il server da installare come "dati.amat-mi.it" e che raggruppa ed espone diverse App Django.

# Installazione

## Lxml

### Windows

### Ubuntu

If an error arise while installing this package, try doing this:

    sudo apt-get build-dep python-lxml
    
before the usual:

    pip install lxml

## Pillow

### Windows

Se Ë necessario usare manage-py da linea di comando (Es: per eseguire "createsuperuser"), 
conviene farlo dalla Git Bash.

Bisogna perÚ aggiungere davanti il comando "winpty", per esempio:
     
    cd /c/Users/Paolo/git/amat/django-amat-dati
    winpty python manage.py createsuperuser
    
dopo aver attivato il virtualenv, usando la sintassi Linux, per esempio:

    . /c/Users/Paolo/venv/django-amat-dati/Scripts/activate
    
E' perÚ prima necessario creare anche i file di puntamento alle App contenute, come per Linux, per esempio:

    echo "/var/www/django/projects/atm-tweet-server/" > /c/Users/Paolo/venv/django-amat-dati/Lib/site-packages/tweet.pth

    echo "C:\Users\Paolo\git\AMAT\park_server" > /c/Users/Paolo/venv/django-amat-dati/Lib/site-packages/park_server_core.pth
 
### Ubuntu

To have support for JPEG, and other formats, a few dependencies must be installed BEFORE Pillow.

sudo apt-get install libjpeg8-dev
sudo apt-get install libfreetype6-dev
sudo apt-get install zlib1g-dev

(following lines are maybe not needed)
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

(following lines must be used only if Pillow was already installed)
pip uninstall Pillow
pip install Pillow

## Ambiente

Creare directory per ospitare i progetti Django e il necessario a farli girare:

    sudo mkdir /var/www/django
    sudo chown <utente>.www-data /var/www/django 
    cd /var/www/django    
    mkdir projects
    mkdir venv
    mkdir mnt
	  
Installare pip per python3:

    sudo apt install python3-pip
      
ATTENZIONE!!! Se appare un messaggio del tipo:

    You are using pip version 8.1.1, however version 10.0.0 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.
    
Ë importante __NON__ eseguire l'aggiornamento consigliato, che potrebbe corrompere il comando pip!!!    

In caso di problemi, provare ad effettuare un downgrade ad una versione funzionante, per esempio:

    sudo python3 -m pip install pip==9.0.1
     
Installare il tool virtualenv:
		
		sudo pip install virtualenv
		
Creare virtual env per il progetto:
	
    virtualenv /var/www/django/venv/django-amat-dati

Creare directory di mount per il progetto:

    mkdir -p /var/www/django/mnt/django-amat-dati
		
Clonare i repository necessari:

    cd /var/www/django/projects
    git clone https://github.com/amat-mi/django-amat-dati.git
    git clone https://github.com/amat-mi/atm-tweet-server.git
    git clone https://github.com/amat-mi/park_server.git
    git clone https://github.com/amat-mi/atm-tweet-client.git
    
__ATTENZIONE!!!__ Se necessario fare git switchout sul branch opportuno!!!

Attivare il virtualenv ed installare i requirements:

    . /var/www/django/venv/django-amat-dati/bin/activate
    cd /var/www/django/projects/django-amat-dati
    pip install -r requirements.txt
    deactivate

__ATTENZIONE!!!__ Se qualcuna delle App contenute ha ulteriori requirements, bisogna fare il pip install -r requirements.txt
di ognuna, prima di fare deactivate!!!
    
Aggiungere nel virtualenv i file di puntamento alle App che dovranno essere servite

    echo "/var/www/django/projects/atm-tweet-server/" > /var/www/django/venv/django-amat-dati/lib/python3.5/site-packages/tweet.pth
    
    echo "/var/www/django/projects/park_server/" > /var/www/django/venv/django-amat-dati/lib/python3.5/site-packages/park_server_core.pth
            
Se non gi‡ presenti, copiare gli script di gestione Django dal repository del progetto principale
e impostare i diritti opportuni:

    cp /var/www/django/projects/django-amat-dati/docs/scripts/*.sh /var/www/django/
    chmod ug+x /var/www/django/*.sh

Preparare l'ambiente di runtime Django:

    sudo /var/www/django/django-prepare.sh django-amat-dati
              
## Database

Installare PostgreSQL con PostGIS, nelle versioni desiderate, per esempio:

    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >> /etc/apt/sources.list.d/postgresql.list'
    sudo apt-get update
    sudo apt-get install postgresql-9.6-postgis-2.4
    
Se non ancora presente, creare Utente PostgreSQL "django" con le stesse credenziali usate in settings.py, per esempio:

    sudo -u postgres psql
    CREATE ROLE django LOGIN UNENCRYPTED PASSWORD '<PASSWORD>' NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
    \q

Creare database and install PostGIS extension (only if needed):

    sudo -u postgres psql
    CREATE DATABASE django_amatdati
    WITH OWNER = django
        TEMPLATE = template0
        ENCODING = 'UTF8'
        TABLESPACE = pg_default
        LC_COLLATE = 'C'
        LC_CTYPE = 'C'
        CONNECTION LIMIT = -1;
    \c django_amatdati
    CREATE EXTENSION postgis;
    \q

### Se non si intende ripristinare il contenuto del database da un salvataggio

Applicare le migration per tutte le App:

    /var/www/django/django-manage.sh django-amat-dati migrate

Creare un superutente per Django, usando un indirizzo EMail vero:

    /var/www/django/django-manage.sh django-amat-dati createsuperuser

## Apache

Installare Apache:

    sudo apt-get install apache2

ATTENZIONE!!! Se c'√® gi√† un server in ascolto sulla porta 80, 
	l'installazione andr√† a buon fine, ma il server non potr√† essere avviato!!!
	Modificare quindi la porta di ascolto di Apache:
	
    sudo pico /etc/apache2/ports.conf
 
Disabilitare il virtual host di default (a seconda della versione di Apache):

    sudo a2dissite 000-default
    sudo a2dissite default

Installare mod_wsgi:

    sudo apt-get install libapache2-mod-wsgi
    sudo apt-get install libapache2-mod-wsgi-py3

ATTENZIONE!!! Solo uno tra i due moduli wsgi puÚ essere installato!!!

Attivare i moduli necessari:

    sudo a2enmod wsgi rewrite
    
Avviare o riavviare Apache:

    sudo service apache2 restart

Copiare i file di configurazione Apache:

    sudo cp /var/www/django/projects/django-amat-dati/docs/apache/*.* /etc/apache2/sites-available/
    
impostare i diritti opportuni:

    sudo chmod u=rw,go=r /etc/apache2/sites-available/*.*
    sudo chown root.root /etc/apache2/sites-available/*.*
    
e attivarli:
	
    sudo a2ensite django-amat-dati.conf

Ricaricare la configurazione di Apache:

    sudo service apache2 reload
    
## Utenti e sistema

### Server esterno per accettare dati dal server interno
 
Creare uno user per l'invio dei dati dal server interno, necessariamente con una password:

    sudo adduser doit

__ATTENZIONE!!!__ Usare proprio __ADD__user!!!

### Server interno per inviare dati al server esterno

Vedere anche:

    http://askubuntu.com/questions/46930/how-can-i-set-up-password-less-ssh-login

Creare uno user, senza password:
    
    sudo /usr/sbin/useradd doit

Creare la directory home per il nuovo utente (vedere anche: http://serverfault.com/questions/63764/create-home-directories-after-create-users):

    sudo /sbin/mkhomedir_helper doit

Impersonare l'utente appena creato:

    sudo su doit

Creare chiavi pubblica/privata (senza passphrase):

    ssh-keygen

Copiare la chiave pubblica sul server esterno (richiede la password sul server esterno):

    ssh-copy-id doit@<server_esterno>

Uscire dall'utente doit:

    exit

# Tips & Tricks

## Git

Se non si riesce a fare il pull perch√© ci sono file locali modificati, che si possono sovrascrivere
perch√© si tratta di prove, o altro, usare il comando:

    git checkout -- .

In case of error:

    error: server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt 
    CRLfile: none while accessing https://github.com/...
    fatal: HTTP request failed

change global Git configuration:

    sudo git config --global --edit

and add following lines:

  [http]

	sslVerify = false

  [https]

	verify = false

## License

TBD
This is a private project...
