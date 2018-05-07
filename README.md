# TOTP integration

## What does TOTP stand for?
TOTP is the acronym for Time-Based One-Time Password. A typical
2 factor auth implementation as a RSA token is.

## And what does this program do?
This a easy and visual way to test how does this TOTP thing works.
Just install an app which could let you add TOTP services (Google,Latch)
in your smartphone, execute the python program on your computer
and read the QR code with Latch (any other app is valid tho')
And see how it works.

## Requirements
pytop (in order to generate the token)
```
pip install pyotp

```
pyqrcode (in order to generate the QR)
```
pip install pyqrcode
```
