# import the function that will return an instance of a connection
from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

        # ninja = []
        # print('000000000000000000000')
        # print(result)
        # ninja.append(cls(result[0]))

        # return ninja

    @classmethod
    def ninjas_in_dojo(cls, data):
        query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(dojo_id)s"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        
        return results

    
    @classmethod
    def get_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(dojo_id)s"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

