from app import app, api
from models import *

from flask import jsonify, url_for, request, abort
from flask_restx import Resource, fields
import sqlite3




@api.route('/clients/<idclient>')
class ClientId(Resource):
    @api.doc(model = clientget)
    def get(self,idclient):
        """
        
        Retourne le détail d'un client
        
        """
        
        connection = sqlite3.connect('video1.db')
        cursor = connection.cursor()
        cursor.execute('SELECT id_client FROM client ')
        last_id = len(cursor.fetchall())
        if int(idclient) > last_id or int(idclient)==0:
            connection.close()
            abort(404)
        
        id = (idclient,)
        cursor.execute('SELECT * FROM Client WHERE id_client = ?',id)
        req = cursor.fetchone()

        client = {
            'id':req[0],
            'Nom':req[1],
            'Prenom':req[2],
            'Adress mail':req[3],
            'Age':req[4]
        }

        connection.close()

        response=jsonify(client)
        response.status=200
        return response

    @api.doc(body=clientpost, model=clientget)
    def put(self,idclient):
        """
        Modifie les détails d'un client (Nom, Prenom, )
        """
        if request.json:
            intid = int(idclient)
            connection = sqlite3.connect("video1.db")
            cursor = connection.cursor()

            cursor.execute('SELECT id_client FROM client')
            client_id = []
            client = {}
            for i in cursor.fetchall():
                client_id.append(int(i[0]))
            
            if intid not in client_id:
                abort(404)

            try:
                update_client = (request.json['nom'],request.json['prenom'],request.json['email'],request.json['age'],intid)
                cursor.execute('UPDATE client SET nom_client = ?, prenom = ?, email = ?, age = ?  WHERE id_client = ?',update_client)
                connection.commit()

                client['nom']=request.json['nom']
                client['prenom']=request.json['prenom']
                client['email']=request.json['email']
                client['age']=request.json['age']

            except(TypeError, ValueError):
                abort(400)
                connection.rollback()
            finally:
                connection.close()


            response = jsonify(client)
            response.status_code=200
            response.headers['location'] = '/clients'+str(intid)
            return response

        else:
            abort(415)

    @api.doc()
    def delete(self,idclient):
        """
        Supprimer un client
        """
        intid = int(idclient)

        connection = sqlite3.connect("video1.db")
        cursor = connection.cursor()

        cursor.execute('SELECT id_client FROM client')
        client_id = []
        for i in cursor.fetchall():
            client_id.append(int(i[0]))
        
        if intid not in client_id:
            abort(404)
        
        try:
            client_delete = (intid,)
            cursor.execute('DELETE FROM client WHERE id_client = ?',client_delete)
            connection.commit()
        except sqlite3.Error as e:
            print("Erreur lors de la suppression du client ",e)
            connection.rollback()
        
        connection.close()

        response = jsonify({})
        response.status_code == 200
        return response



@api.route('/clients/<idclient>/film')
class ClientFilmAll(Resource):
    api.doc(model=get_allfilm)
    def get(self,idclient):
        """
        Retourne le titre et la location de tout les films compris dans 
        cette catégorie 
        """
        locations = []
        try:
            connection = sqlite3.connect('video1.db')
            cursor = connection.cursor()
            id = (int(idclient),)
            sql = "SELECT film.titre_film FROM film JOIN film_client ON film.id_film = film_client.film_id JOIN client ON film_client.client_id = client.id_client WHERE client.id_client = ?"
            
            cursor.execute(sql,id)
            films = cursor.fetchall()
            print(films)
            for i in films:
                titre = i[0]
                locations.append({'titre':titre})
            print(locations)
        except sqlite3.Error as e:
            print("Erreur",e)
            connection.rollback()
        finally:
            connection.close()
            return(jsonify(locations))

    @api.doc(body=film_clientpost, model=film_clientpost)
    def post(self,idclient):
        """
        Ajout d'une location de film pour un client
        """
        filmclient={}
        id_film=request.json['idFilm']
        intid = int(idclient)
        if request.json :
            try:
                connection = sqlite3.Connection("video1.db")
                cursor = connection.cursor()

                idfilm=(id_film,)
                cursor.execute('SELECT film.age_min FROM film WHERE film.id_film= ?', idfilm)
                age_min= cursor.fetchone()

                id=(intid,)
                cursor.execute('SELECT client.age from client WHERE client.id_client = ?', id)
                age_client=cursor.fetchone()

                if age_client>=age_min:
                    film_client = (id_film,intid)
                    cursor.execute('INSERT INTO film_client VALUES (?,?)',film_client)
                               

                connection.commit()

                filmclient['film']=request.json['film']
                filmclient['client']=request.json['client']
                
            except Exception as e:
                print("[Erreur]",e)
                connection.rollback()
            
            finally:
                connection.close()

            response = jsonify(filmclient)
            response.status_code = 201
            response.headers['location'] = 'clients/'+idclient+'/film/'+str(id_film)
            return response

        else:
            abort(415)

