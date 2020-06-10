# Netivid
Powerful script for network recon

## How it works?
- You make a script
- You put it in the scripts folder

Your script will receive a target variable, which is the input. Your script will have to return: `error`, `warnings`, `statuscode` and `out`

## How to use?
  `-h, --help`       show this help message and exit

  `--script SCRIPT`  Path to script. (must have: name, description and main)
  
  `--target TARGET`  Target, can be domain, IP, or subnet
  
  `--type TYPE`      Can be: i4 (for IPv4), i6 (for IPv6) or dn (for Domain Name)

## Default scripts:
- `dns_queries`: makes few dns queries and returns the responses.
```bash
>>> python .\source\main.py --script dns_querier --target google.com --type dn
Netivid v0.12
| dns_queries:
|     A         google.com              172.217.20.14
|     AAAA      google.com              2a00:1450:400d:805::200e
|     MX        google.com              30 alt2.aspmx.l.google.com.
|     MX        google.com              20 alt1.aspmx.l.google.com.
|     MX        google.com              10 aspmx.l.google.com.
|     MX        google.com              40 alt3.aspmx.l.google.com.
|     MX        google.com              50 alt4.aspmx.l.google.com.
|     NS        google.com              ns1.google.com.
|     NS        google.com              ns2.google.com.
|     NS        google.com              ns4.google.com.
|     NS        google.com              ns3.google.com.
|     TXT       google.com              "facebook-domain-verification=22rm551cu4k0ab0bxsw536tlds4h95"
|     TXT       google.com              "docusign=1b0a6754-49b1-4db5-8540-d2c12664b289"
|     TXT       google.com              "docusign=05958488-4752-4ef2-95eb-aa7ba8a3bd0e"
|     TXT       google.com              "v=spf1 include:_spf.google.com ~all"
|     TXT       google.com              "globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8="
| E/W Script finished successfully.
```
- Example uasge: python .\source\main.py --script dns_querier --target google.com --type dn