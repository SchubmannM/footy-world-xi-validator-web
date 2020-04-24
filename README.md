# Footy World XI Validator - Web version

The intention of this app is to be a validator for a little game that was started on Twitter: https://twitter.com/MundialMag/status/1250080258122022915

```
Pick the greatest World XI under these the rules:
 
- No two players from the same country
- No two can have played for the same club
- All eleven have to have played in your lifetime
```

The app asks you to enter 11 different footballer names and then runs a validation to check if any of the above stated rules were broken or not.

Version 1 does not include the "played in your lifetime" rule as that's still a bit vague to be defined in code.

This is the web version of the program which is live here: https://footy.schubmann.dev/. 
A python CLI version is also available here: https://github.com/SchubmannM/footy-world-xi-validator

Currently this web version is hosted on Heroku. In the future I want to move this to Amazon AWS as I was working on docker files on purpose to deploy it there. I decided to go for Heroku as it was too time intensive to get the production version with nginx, ssl certificate and correct dns settings to work on AWS EC2. 
