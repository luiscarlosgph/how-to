Regular update of domain names for servers running on dynamic IP addresses
--------------------------------------------------------------------------

If you are managing a domain with Cloudflare, and you have servers running on dynamic IP addresses (e.g. a home Internet connection),
you can update the DNS records of a domain on Cloudflare via API. To do so:

1. Click on the icon on the top right of your dashboard, and then on  `My Profile` -> `API Tokens`.

2. Click on `Create Token`, and then on `Use template` for `Edit zone DNS`.

3. In `Zone Resources` **include** the domain that you want to manage.

4. Click on `Continue to summary` -> `Create Token`.

5. Save [this script](cloudflare_dns_update.sh) in your favourite location and add it to crontab: 

```
TODO
```


