def check_not_russian_ip(verbose=False):
    import requests

    response = requests.get('https://ifconfig.me')
    response.raise_for_status()  
    ip = response.text.strip()

    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    country = data.get('country', '')
    
    if country == 'RU':
        raise Exception('Current ip is russian!')

    if verbose:
        return f'Current ip location: {country}'

check_not_russian_ip(verbose=True)