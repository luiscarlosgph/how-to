1. Copy (and edit appropriately) this into `/usr/local/sbin/gd-dyndns`:

```
#!/bin/bash

mydomain="sos-obx.us"
myhostname="gateway"
gdapikey="api_key:key_secret"
logdest="local7.info"

myip=`curl -s "https://api.ipify.org"`
dnsdata=`curl -s -X GET -H "Authorization: sso-key ${gdapikey}" "https://api.godaddy.com/v1/domains/${mydomain}/records/A/${myhostname}"`
gdip=`echo $dnsdata | cut -d ',' -f 1 | tr -d '"' | cut -d ":" -f 2`
echo "`date '+%Y-%m-%d %H:%M:%S'` - Current External IP is $myip, GoDaddy DNS IP is $gdip"

if [ "$gdip" != "$myip" -a "$myip" != "" ]; then
  echo "IP has changed!! Updating on GoDaddy"
  curl -s -X PUT "https://api.godaddy.com/v1/domains/${mydomain}/records/A/${myhostname}" -H "Authorization: sso-key ${gdapikey}" -H "Content-Type: application/json" -d "[{\"data\": \"${myip}\"}]"
  logger -p $logdest "Changed IP on ${hostname}.${mydomain} from ${gdip} to ${myip}"
fi
```
2. Set ownership and permissions for the script: 

```
$ chown root:root /usr/local/sbin/gd-dyndns
$ chmod +x /usr/local/sbin/gd-dyndns
```

3. Edit crontab (`crontab -e` as root) and call the script every `10` minutes:

```
*/10 * * * *    /usr/local/sbin/gd-dyndns > /dev/null
```
