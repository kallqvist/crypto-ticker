# crypto-ticker

Docker image and compose stack for tracking crypto currency values over time.

The stack is:
- flask api for reading exchange rates from cryptocompare.com and converting to prometheus format
- prometheus as data store
- grafana for ui and dashboarding

Select currencies using environment variables for crypto-ticker as in docker-compose.yml example.

```
FROM_CURRENCIES: 'BTC,ETH,BCH,DASH,XRP,XMR,STRAT,LTC,DASH'
TO_CURRENCIES: 'SEK,EUR,USD'
```

docker-compose: https://github.com/kallqvist/crypto-ticker/blob/master/docker-compose.yml
