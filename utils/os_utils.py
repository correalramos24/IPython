
#Env variables
from os import getenv
existEnv    = lambda env_var : (getenv(env_var) != None)
getEnvVar   = lambda env_var : getenv(env_var)

#File management
from os.path import isfile, join
fileExist   = lambda fName : isfile(fName)
pathAndFile = lambda p, fName : join(p,fName)
