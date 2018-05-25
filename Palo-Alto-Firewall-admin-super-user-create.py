import requests
import urllib
import urllib3
#import pan.xapi
import xml.etree.ElementTree as ET
import ssl
import boto3
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

context = ssl._create_unverified_context()

pan_api_key_3 = os.environ.get('PAN_API_KEY_GP3')
pan_api_key_2 = os.environ.get('PAN_API_KEY_GP2')
#firewall_base_url_2 = "https://"+gpx_version_2+"-ops.salesforceiq.com/api/"


#resp=requests.get('https://usw2a-gp3-ops.salesforceiq.com/api/?type=config&action=set&key="+pan_api_key_3+"&xpath=/config/mgt-config/users&element=<entry%20name="user"><permissions><role-based><superuser>yes</superuser></role-based></permissions></entry>')
resp=requests.get('https://usw2b-gp2-ops.salesforceiq.com/api/?type=config&action=set&key='+pan_api_key_2+'&xpath=/config/mgt-config/users&element=<entry%20name="user"><permissions><role-based><superuser>yes</superuser></role-based></permissions></entry>')

