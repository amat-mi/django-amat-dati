# django-amat-dati

Progetto Django per il server da installare come "dati.amat-mi.it" e che raggruppa ed espone diverse App Django.

# Installazione

## Pillow

### Windows

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
	    
Installare il tool virtualenv:
		
		TBD
		
Creare virtual env per il progetto:
	
    virtualenv /var/www/django/venv/django-amat-dati
		
Clonare i repository necessari:

    cd /var/www/django/projects
    git clone https://github.com/amat-mi/django-amat-dati.git
    
__ATTENZIONE!!!__ Se necessario fare git switchout sul branch opportuno!!!

Attivare il virtualenv ed installare i requirements:

    source /var/www/django/venv/django-amat-dati/bin/activate
    cd /var/www/django/projects/django-amat-dati
    pip install -r requirements.txt
    deactivate

__ATTENZIONE!!!__ Se qualcuna delle App contenute ha ulteriori requirements, bisogna fare il pip install -r requirements.txt
di ognuna, prima di fare deactivate!!!
    
Aggiungere nel virtualenv i file di puntamento alle App che dovranno essere servite

    echo "/var/www/django/projects/atm-tweet-server/" > /var/www/django/venv/django-amat-dati/lib/python2.7/site-packages/tweet.pth
    
    echo "/var/www/django/projects/park_server/" > /var/www/django/venv/django-amat-dati/lib/python2.7/site-packages/park_server_core.pth
            
ISTRUZIONI INCOMPLETE, DA CONTINUARE!!!

## Database

Se non ancora presente, creare Utente PostgreSQL "django" con le stesse credenziali usate in settings.py.

Creare database:

    CREATE DATABASE django_amatdati
    WITH OWNER = django
        TEMPLATE = template0
        ENCODING = 'UTF8'
        TABLESPACE = pg_default
        LC_COLLATE = 'C'
        LC_CTYPE = 'C'
        CONNECTION LIMIT = -1;

If PostGIS is installed and needed, login to the newly created database and do:
	          
    CREATE EXTENSION postgis;
       
Creare le tabelle per South e per le altre App che non usano South stesso (solo per Django<1.7):

    python manage.py syncdb
    
Se viene richiesto, creare un superutente per Django, usando un indirizzo EMail vero.

Applicare le migration per tutte le App:

    python manage.py migrate
    
## Apache

Installare Apache:

    sudo apt-get install apache2

ATTENZIONE!!! Se c'è già un server in ascolto sulla porta 80, 
	l'installazione andrà a buon fine, ma il server non potrà essere avviato!!!
	Modificare quindi la porta di ascolto di Apache:
	
    sudo pico /etc/apache2/ports.conf
 
Disabilitare il virtual host di default (a seconda della versione di Apache):

    sudo a2dissite 000-default
    sudo a2dissite default

Installare mod_wsgi:

    sudo apt-get install libapache2-mod-wsgi

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

# Tips & Tricks

## Git

Se non si riesce a fare il pull perché ci sono file locali modificati, che si possono sovrascrivere
perché si tratta di prove, o altro, usare il comando:

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
