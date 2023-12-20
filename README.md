# GXNitro
Discord nitro link generator using opera gx big brain move

Taking into account the exploit it will be probably patched soon, but while it isn't here you have a nice script that gives you redeem links

Just do `python nitro.py` and that's it (you need requests module installed)

Also all tokens for redeems contain this header
```
{
  "alg": "dir",
  "enc": "A256GCM"
}
```
But it never matches any signature so i don't know, it's a weird jwt or i'm dumb
