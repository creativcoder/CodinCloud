## CodinCloud

CodinCloud is an Compiler As a Service Platform

The website uses Flask Microframework as the backend, and MaterializeCSS on the Frontend.

CodinCloud is being updated for now, for better code organization.

The older version of this app is hosted @[flaskcompiler](https://flaskcompiler.herokuapp.com)

### Build Instructions:

Its recommended to use virtualenv for a standalone developemnt environment for CodinCloud.

We have a shell script, which sets up everything that is needed to run CodinCloud. If you are not into a virtualenv environment, the script will setup one for you, then install all dependencies of Flask and then serve it on default port `5000`. You can override the port by passing it as an argument to script.

cmod the script `boostrap.sh` : `sudo chmod +x ./bootstrap.sh`

and then run it: `./boostrap.sh [port]`


TODO

--Add Support for multiple languages

--User Registration through Github
