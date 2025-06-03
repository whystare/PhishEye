import ssl
import socket
from urllib.parse import urlparse
from datetime import datetime

def check_ssl_certificate(url):
    try:
        hostname = urlparse(url).hostname
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                # Получаем дату окончания действия сертификата
                expire_date_str = cert['notAfter']
                expire_date = datetime.strptime(expire_date_str, '%b %d %H:%M:%S %Y %Z')
                return True, expire_date.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        return False, str(e)
