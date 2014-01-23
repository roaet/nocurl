Why nocurl?
==========
We have supernova. Why this?

When you need to test out parts of an API that aren't available to
supernova, you can use nocurl. Or you could just use curl. It's your life.

Nocurl is 120 lines of code and only needs the requests library,
so it's easier to modify than supernova, too.

nocurl
============
Instead of using curl and copypasta, put your commonly-used API data into
payloads.conf and run it with a CLI menu. The output json is pretty-printed.
You can change payloads on-the-fly without restarting nocurl.

This tool is specifically for OpenStack development, hence the "X-Auth-Token"
header. 

Obviously requires more development. Pull requests always welcome.

screenshots
===========
Dem fancy unicodes...

![ScreenShot](http://i.imgur.com/lt2FfFP.png)




![ScreenShot](http://i.imgur.com/9K2DKOM.png)

todo
====

1. Make token= and data= optional in payloads.conf.
2. Enable logging.
3. Move url, port and token in payloads.conf to an [endpoints] section and get rid of tokens.conf
4. Option to move data automatically from result of one call to data/route of another.
5. Ability to chain multiple payloads.
6. Better CLI menu with user-defined formatting.

