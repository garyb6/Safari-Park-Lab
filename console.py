from models import staff
from models.staff import Staff 

import repositories.staff_repository as staff_repository 

staff1 = Staff("Ant McPartlin", "Jan20", "Big Cats", 3)
staff_repository.save(staff1)

staff2 = Staff("Dec Donnelly", "Dec19", "Reptiles", 4)
staff_repository.save(staff2)

staff_repository.select_all()
