from db.run_sql import run_sql
from models.animal import Animal 
from models.staff import Staff
import repositories.staff_repository as staff_repository 

def save(animal):
    sql = "INSERT INTO animals (name, type, staff_id) VALUES (%s, %s, %s) RETURNING *"
    values = [animal.name, animal.type, animal.staff.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        animal = Animal(row['name'], row['type'], staff, row['id'])
        animals.append(animal)
    return animals 

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal = Animal(result['name'], result['type'], staff, result['id'])
        return animal

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)