import os 

port = None
root_dir = None

apache_conf = f"""
<VirtualHost *:{port}>
    ServerAdmin webmaster@localhost
    DocumentRoot {root_dir}

    ErrorLog ${{APACHE_LOG_DIR}}/error.log
    CustomLog ${{APACHE_LOG_DIR}}/access.log combined

    <Directory {root_dir}>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>
"""
def rootDir():
    return os.path.dirname(os.path.realpath(__file__))