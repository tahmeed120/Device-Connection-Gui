# ERPNext related configs
ERPNEXT_API_KEY = '0d037bd6b1f76f7'
ERPNEXT_API_SECRET = '8d6ab05bd884d96'
ERPNEXT_URL = 'http://qstml.lithe-tech.com'


# operational configs
PULL_FREQUENCY = 1 or 60 # in minutes
LOGS_DIRECTORY = 'logs' # logs of this script is stored in this directory
IMPORT_START_DATE = '20121112' or None # format: '20190501'

# Biometric device configs (all keys mandatory)
    #- device_id - must be unique, strictly alphanumerical chars only. no space allowed.
    #- ip - device IP Address
    #- punch_direction - 'IN'/'OUT'/'AUTO'/None
    #- clear_from_device_on_fetch: if set to true then attendance is deleted after fetch is successful.
    #(Caution: this feature can lead to data loss if used carelessly.)
devices = [{"device_id": "2", "ip": "192.168.0.5", "punch_direction": "", "clear_from_device_on_fetch": ""}]

# Configs updating sync timestamp in the Shift Type DocType
shift_type_device_mapping = [{"shift_type_name": "", "related_device_id": ["2"]}]
