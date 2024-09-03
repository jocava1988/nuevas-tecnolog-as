#datos para la conexion a base de datos

databaseName="gestorbd"
userName="root"
userPassword=""
connectionPort="3306"
server="localhost"



#creando la conexion 
databaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{databaseName}"



print(databaseConnection)

