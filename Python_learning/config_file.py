
import configparser # inorder to access confif_file there is inbuilt calss 

config = configparser.ConfigParser # small letter configparser is file name and capital one is class here

config.read(r"C:\Users\70q9136\OneDrive - Panasonic Europe\Documents\Python\config_file.ini")

brick_cost = config["raw_materials"]["brick_cost"]
print(f"{brick_cost}")