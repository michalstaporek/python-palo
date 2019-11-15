import re
import requests

api_key = "==============replace_with_api_key=============="
payload = {"key" : api_key}
fw_ip = "x.x.x.x"
file = open("url_cat.txt", "w")

for line in open("url_list.txt"):
  line = line.strip()
  cmd = "<test><url>{0}</url></test>".format(line)
  URL = "https://{0}/api/?type=op&cmd={1}".format(fw_ip, cmd)
  result = requests.get(url = URL, params = payload, verify = False, timeout = 40)
  decoded_result = result.text
  decoded_result = re.search ('\\n(.*)\(Cloud' , decoded_result )
  file.write(decoded_result.group(1) + '\n')

# close file
file.close()
