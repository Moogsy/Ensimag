Liste interfaces réseau: "ifconfig"
Trouver addresse ips: "nslookup [nom domaine]"
Trouver serveurs mail: "nslookup -type=MX [nom domaine]"
Trouver serveurs de noms: "dig [nom domaine]"
Trouver nom DNS (dns inversé): "nslookup -type=ptr [ip]" ou "dig -x [ip]"
Enregistrement CNAMe: "dig CNAME [nom domaine]"

Enregistrement de type X: "nslookup -type=X [...]" ou "dig X [...]"

Connexion mail avec un serveur "openssl s_client -quiet -connect [domaine]:[port]"

