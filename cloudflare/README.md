Regular update of domain names for servers running on dynamic IP addresses
--------------------------------------------------------------------------

If you are managing a domain with Cloudflare, and you have servers running on dynamic IP addresses (e.g. a home Internet connection),
you can update the DNS records of a domain on Cloudflare via API. To do so:

1. Install `jq`: `$ sudo apt instlal jq`

2. Click on the icon on the top right of your dashboard, and then on  `My Profile` -> `API Tokens`.

3. Click on `Create Token`, and then on `Use template` for `Edit zone DNS`.

4. In `Zone Resources` **include** the domain that you want to manage.

5. Click on `Continue to summary` -> `Create Token`.

6. Save [this script](https://github.com/luiscarlosgph/cloudflare-stuff/blob/main/src/cloudflare_dns_update.sh) in your favourite location, and edit it accordingly (i.e. write your Cloudflare account and domain details).

7. Add script to crontab so that it runs every 10 minutes:

```
TODO
```


