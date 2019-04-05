import psycopg2

def get_substituts(cat_id):
    try:
        connection = psycopg2.connect(user = "maxence",
                                      password = "maxence",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "purbeurre")
        cursor = connection.cursor()
        query = (("SELECT * FROM myapp_product WHERE category_id = {};".format(cat_id)))
        cursor.execute(str(query))
        record = cursor.fetchall()
        record.sort(key = lambda x: x[2])
        count = 0
        substituts = []
        for product in record:
            if count <= 5:
                try:
                    idd = product[0]
                    name = product[1]
                    nut_grade = product[2]
                    url = product[3]
                    img_url = product[4]
                    nut_url = product[5]
                    substituts.append((idd, name, nut_grade, url, img_url, nut_url))  
                except KeyError:
                    idd = product[0]
                    name = product[1]
                    nut_grade = product[2]
                    url = product[3]
                    img_url = product[4]
                    substituts.append((idd, name, nut_grade, url, img_url))        
            count += 1          
        print(substituts) 
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

get_stbstituts(200)