# Budget + Register Project

I wanted an app to manage my personal budget and related documents, data.

At its core, a budget can be implemented as a glorified spreadsheet. Some clever Excel
scripting (or LibreOffice or other software), and you can build a _really nice_ budget
solution. A few steps further and apps like YNAB, Mint, EveryDollar, etc. overlay a 
nice UI/UX on top of this data.

However, it breaks down at integration. Nearly every budgeting application requires at
least a $50-$120/yr subscription for bank transaction(s) integration. (Diving into this,
it's due to integration permissions, SDKs, libraries, etc. ultimately driven by the banks
providing the access and data. So, the apps are charging a premium, but justifiably so.)

In addition, with the rising amount of consumer payment integrations and subscription 
services...your checking account register can have payments "_hidden behind_" the names
of a payment integrator on the banking register.

> Ex: Paying for things via Paypal. 
> --> Using the Starbucks app, an easy way to configure payment information is via Paypal,
especially if you're already using it for other services. The entry on the check. acct. 
will say "Paypal..." instead of "Starbucks".
> --> It's the same scenario for Apple services (i.e. iCloud storage)
> --> Paying for services, ...via Apple ...via Paypal
>   - This is where it gets hairy.
>   - Checking account register says: "Paypal"
>   - Paypal history says: "Apple Services"
>   - Apple payment history gives the actual detail of what was paid

_*So!*_ this left with me with each time I sat down to 


## References

Ref: [https://www.geeksforgeeks.org/python-fetch-your-gmail-emails-from-a-particular-user/](https://www.geeksforgeeks.org/python-fetch-your-gmail-emails-from-a-particular-user/)

I started with this article + snippet, and then quickly moved onto an example using `imap_tools`. 
Keeping this around for reference.