### CryptoInvest

This program is intended to deposit a set amount into my Coinbase Pro account and purchase designated crypto assets using the deposited funds. It's my understanding that this feature only exists in Coinbase (regular) and is not available in Coinbase Pro. Given that Coinbase Pro has lower transaction fees, it makes sense to have this process on Coinbase Pro.

I wanted to have the code set up to 1) make recurring deposits to Coinbase Pro and 2) use the deposited funds to purchase a designated allocation of BTC and ETH. After doing some research, I learned that this is possible by using AWS Lambda to deploy the code as a 'function' and then use CloudWatch's cron scheduling to run the code at set intervals. My code is currently set up to run at 9:00 am EST on the last day of each month. Think of this as an automatic withdrawal and investment, similar to how a company 401(k) or 403(b) would work each pay period but instead on a post-tax basis. I already had a similar, albeit not as automated, structure set up for my Roth IRA, but was interested in dollar cost averaging (DCA) crypto.

The program uses the Coinbase Pro API via the Coinbase Pro wrapper. The link can be found below.

Packages: [cbpro](https://github.com/danpaquin/coinbasepro-python), json

Thanks to [Rhett Reisman](https://rhett.blog/2021/02/05/buy-bitcoin-everyday-2/) for the layer assistance.

🚀

---
[![image](https://img.shields.io/badge/Personal%20Site-%20-informational?style=flat-square&logo=appveyor)](https://www.jedraynes.com/)
[![image](https://img.shields.io/badge/LinkedIn-%20-informational?style=flat-square&logo=appveyor)](https://www.linkedin.com/in/jedraynes/)

jedraynes
