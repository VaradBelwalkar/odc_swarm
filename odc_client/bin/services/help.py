help = '''
NAME
       Termium : Client to access microservices

DESCRIPTION
Termium :
         Termium is a way to access secure personal storage at the server with ability to access various runtimes 
         the server provides with access to some services

TERMIUM STARTUP 
       To get into termium environment, just type,

       $termium start

TERMIUM COMMANDS

       termium $ config

               Displays the configured URL, username, and password of the client

       termium $ config edit

              Edits configuration and saves the changes
	   
	termium $ version

               Shows the version number of the project

       termium $ server

               Shows information about the server

       termium $ signup

              Creates an account with given username and password

       termium $ view
      
              lists all the files in the cloud

       termium $ uploadfile <file-path>

              uploads the specified file into the cloud

       termium $ uploaddir <dir-path>

              uploads the specified directory to the cloud

       termium $ download <filename> <filepath>

              downloads the specified file from the cloud

       termium $ delete <filepath>+'/'+<filename>

              deletes the specified file in the cloud

       termium $ sync <dirpath>

              sync the specified directory with the cloud



TERMIUM COMMANDS TO ACCESS RUNTIMES

  (CURRENTLY AVAILABLE RUNTIMES : "ubuntu" , "development_server")

  (You can own maximum of 5 containers at a time)


       termium $ container  run <runtime_name> 
             
              get a new specifed container

       termium $ container list images

              get available os images

       termium $ container list containers

              get the list of containers that you own (useful for which container to resume)

       termium $ container remove <container_name>

              remove the specified container from the server

'''       
print(help)