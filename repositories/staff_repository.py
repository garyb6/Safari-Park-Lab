from db.run_sql import run_sql

from models.staff import Staff
from models.animal import Animal 

def save(staff):
    sql = "INSERT INTO staff_list (name, start_date, department, rating) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [staff.name, staff.start_date, staff.department, staff.rating]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff.id = id
    return staff 

def select_all():
    staff_list = []
    sql = "SELECT * FROM staff_list"
    results = run_sql(sql)

    for row in results:
        staff = Staff(row['name'], row['start_date'], row['department'], row['rating'], row['id'])
        staff_list.append(staff)
    return staff_list

def select(id):
    staff = None
    sql = "SELECT * FROM staff_list WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        staff = Staff(result['name'], result['start_date'], result['department'], result['rating'], result[id])
        return staff 

def delete(id):
    sql = "DELETE FROM staff_list WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(staff):
    sql = "UPDATE staff_list SET (name, start_date, department, rating) = (%s, %s, %s, %s) WHERE id = %s"
    values = [staff.name, staff.start_date, staff.department, staff.rating]
    run_sql(sql, values)

def keeper(staff):
    animals = []

    sql = "SELECT * FROM tasks WHERE staff_id = %s"
    values = [staff.id]
    results = run_sql(sql, values)

    for row in results:
        animal = Animal(row['name'], row['type'], staff, row['id'])
        animals.append(animal)
    return animals 

def delete_all():
    sql = "DELETE FROM staff_list"
    run_sql(sql)
    