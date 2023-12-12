from app.models import *

# exec(open(r'D:\Python Practice\Django_Practice\first_project\app\db_shell.py').read())

# Aggregate function
# from django.db.models import Sum, Avg

# # Get the total count of objects
# total_count = Employee.objects.count()
# print(total_count)

# # Get the sum of a numeric field
# total_sum = Employee.objects.aggregate(Sum('salary'))
# print(total_sum)

# # Get the average of a numeric field
# average_value = Employee.objects.aggregate(Avg('salary'))
# print(average_value)

# Ordering
# data = Employee.objects.order_by('-salary')  #---- '-' it gives descending order 
# print(data)

# Chained queries
# filtered_and_ordered = Employee.objects.filter(mob_number__startswith=91).order_by('id')
# print(filtered_and_ordered)

# CRUD operations

# create
# Way 1st
# emp = Employee(first_name="Kedar", last_name="Keskar", email="kk@gmail.com", mob_number=983451872) 
# emp.save()

# way 2nd
# emp = Employee.objects.create(first_name="Kedar", last_name="Keskar", email="kk@gmail.com", mob_number=983451872) 

# Delete record
# Employee.objects.get(id=3).delete()

# filter().delete() #-------- this delets all data

# Update
# emp_obj = Employee.objects.get(id=2)
# emp_obj.first_name = "Reshma"
# emp_obj.last_name = "Patil"
# emp_obj.save()


# all_emps = Employee.objects.all()
# # print(all_emps)
# for emp in all_emps:
#     print(emp.last_name)

# try:
#     emp = Employee.objects.get(last_name__startswith= "S")
#     print(emp)
    
# except Employee.DoesNotExist as msg:
#     print(msg)

# emps = Employee.objects.filter(first_name__startswith = "S")
# print(emps)

# emps = Employee.objects.filter(first_name__in=["Radhika", "Rajesh"])
# print(emps)


# emps = Employee.objects.filter(first_name__contains="R").first()
# print(emps)


from datetime import datetime

# p1 = Person.objects.create(first_name = "Prashant", last_name = "Ghadge")

# Profile.objects.create(bio="student", birthdate=datetime(1993, 1, 14), person=p1)
# Profile.objects.create(bio="student1", birthdate=datetime(1993, 1, 14), person_id=1)

# # p3 = Person.objects.create(first_name = "Smita", last_name = "Patil")
# p3 = Person.objects.get(id=3)
# Profile.objects.create(bio="student3", birthdate=datetime(1993, 1, 14), person_id=3)

# p1 = Person.objects.get(id=1) 
# p1 = Person.objects.get(id=2) # ---- p1 delete kelyamule new record p2 sathi create hoil tyamule aapan id=2 dila aahe.
# p1.delete()
# Address.objects.create(street= "Nagar MAnmad road", city="Shirdi", state="MH", postal_code=423109, person=p1)
# Address.objects.create(street= "Nashik Road", city="Moshi", state="MH", postal_code=412105, person=p1)

# p1 = Person.objects.create(first_name="Pranit", last_name="Purkar")

# # Address.objects.filter(id__in=[1,2]).update(person=p1)
# # Address.objects.get(id=1)
# # Address.objects.get(id=2)
