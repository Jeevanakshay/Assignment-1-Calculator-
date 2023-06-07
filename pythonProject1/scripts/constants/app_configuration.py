import configparser

config_obj = configparser.ConfigParser()
config_obj.read("configuration/application.conf")

# Service details,
SERVICE_HOST = config_obj.get("SERVICE", "HOST")
SERVICE_PORT = config_obj.get("SERVICE", "PORT")


URI = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
