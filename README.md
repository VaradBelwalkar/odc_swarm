# odc_swarm
************** CURRENTLY NOT SUPPORTING **************
IF YOU WANT WORKING SWARM IMAGE FOR ON-DEMAND-CONTAINERS mail me at belwalkarvarad@gmail.com
***********Prerequisites***********
 You must have docker-engine installed where you want to run server and the user added to docker group, if not do following
 
    #for ubuntu based distros
      sudo apt-get install openssh-server (on server side:odc_swarm_server)
      sudo apt-get install openssh-client (on client side:odc_client)
      sudo usermod -aG docker <username> (on server side: odc_swarm_server)
    
    #for arch-based distros
      sudo pacman -S openssh (on both sides)
      sudo usermod -aG docker <username> (on server side)

HOW TO RUN 

You can run the server and client independently on any systems meeting requirements

TO RUN SERVER DO FOLLOWING :
  1.Initilize the swarm cluster (command): docker swarm init --advertise-addr 127.0.0.1:2377 
  1.Download or clone the odc_swarm_server into your system\
  2.Just cd into the odc_swarm_server and run source bin/activate (Run exactly what specified from the same directory)\
  3.Now run python3 manage.py runserver \
Your server should have now be started

TO RUN CLIENT DO FOLLOWING :

  1.Download or clone the odc_client into your system\
  2.cd into teh odc_client and run source bin/activate (Run exactlt what specified from the same directory)\
  3. cd into bin and run "./termium start" (termium was our old project name might change,refer to this README again for changes)

Now create your credentials by running "config_edit"\
then run "set_url" and set the url for the server\
Now run signup to signup to the service\
Now the client is ready!\
Run "help" to see what you can do

Creadentials in django
by default a user with (for testing),\
username = "termium_user"\
email = "termium_user@example.com"\
password = "termium"

has been created so you can directly login from client without signing in (make sure to update the user credentials in client)
