# ez-webhook-catcher
*Warning: You can give attackers shell access to your host if you write your scripts wrong or implement this in any way.

Python flask app that catches webhooks and triggers shell scripts. Does not support params or json body or https or shell script arguments (for now).

## How this works
  1. Place shell scripts in a folder.
  2. When you run this script, it will listen at a port.
  3. When it receives a POST where the endpoint ends in .sh, it will check if a shell script exists in that location. 
  4. If it exists, it will run it and return 200 regardless of what the script does, if not, it will return 404.

The lack of features is a feature.
