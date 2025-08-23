from app.database import SessionLocal, engine
from app.models import Base, School, Standard, Student

def seed_database():
    # Connect to the database
    db = SessionLocal()

    # Drop all existing tables and recreate them to start fresh
    print("Dropping and recreating database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # --- Create Schools ---
    school_names = ["SAIVIJETHA", "PADMAVANI", "Viswabharathi High School"]
    schools = {}
    for name in school_names:
        school = School(name=name, location="Nellore")
        db.add(school)
        db.commit()
        db.refresh(school)
        schools[name] = school
        print(f"Created school: {school.name}")

    # --- Create Standards for each school ---
    standards = {}
    for school_name, school_obj in schools.items():
        standards[school_obj.id] = {}
        for i in range(1, 11):
            for sec in ["A", "B", "C"]:
                std = Standard(name=i, section=sec, school_id=school_obj.id)
                db.add(std)
                db.flush()  # Use flush to get the ID before committing
                standards[school_obj.id][(i, sec)] = std
    db.commit()
    print("Created standards 1-10 for each school.")

    # --- Create Students ---
    # The student data is now directly instantiated as Student objects.
    students_to_add = [
        Student(name='SIVA', gender='MALE', age=20, roll_no=15, phone='9491989611', marks=100, standard_id=standards[schools['Viswabharathi High School'].id][(9,'A')].id),
        Student(name='VENKAT', gender='MALE', age=20, roll_no=50, phone='8331877611', marks=99, standard_id=standards[schools['Viswabharathi High School'].id][(10,'A')].id),
        Student(name='PAVAN', gender='MALE', age=20, roll_no=17, phone='7989829361', marks=100, standard_id=standards[schools['Viswabharathi High School'].id][(8,'B')].id),
        Student(name='SRAVANI', gender='FEMALE', age=19, roll_no=1, phone='8247857395', marks=98, standard_id=standards[schools['Viswabharathi High School'].id][(9,'B')].id),
        Student(name='SYAMALA', gender='FEMALE', age=20, roll_no=2, phone='6303660676', marks=87, standard_id=standards[schools['Viswabharathi High School'].id][(10,'C')].id),
        Student(name='SAI', gender='MALE', age=19, roll_no=3, phone='8247687885', marks=88, standard_id=standards[schools['SAIVIJETHA'].id][(9,'B')].id),
        Student(name='KEERTHANA', gender='FEMALE', age=19, roll_no=30, phone='8253457595', marks=80, standard_id=standards[schools['SAIVIJETHA'].id][(10,'A')].id),
        Student(name='KARUNA', gender='MALE', age=19, roll_no=4, phone='9465454865', marks=78, standard_id=standards[schools['SAIVIJETHA'].id][(9,'A')].id),
        Student(name='KEVIN', gender='MALE', age=19, roll_no=19, phone='7346287685', marks=68, standard_id=standards[schools['SAIVIJETHA'].id][(9,'B')].id),
        Student(name='MARY', gender='FEMALE', age=19, roll_no=20, phone='6245565467', marks=79, standard_id=standards[schools['PADMAVANI'].id][(9,'A')].id),
        Student(name='KAIRA', gender='FEMALE', age=19, roll_no=13, phone='8763657565', marks=75, standard_id=standards[schools['SAIVIJETHA'].id][(9,'B')].id),
        Student(name='VARUN', gender='MALE', age=19, roll_no=40, phone='7458546894', marks=66, standard_id=standards[schools['SAIVIJETHA'].id][(8,'A')].id),
        Student(name='SIVARAJ', gender='MALE', age=20, roll_no=14, phone='9491989612', marks=100, standard_id=standards[schools['PADMAVANI'].id][(8,'A')].id),
        Student(name='VENKATESHWAR', gender='MALE', age=20, roll_no=18, phone='8331877612', marks=99, standard_id=standards[schools['PADMAVANI'].id][(10,'A')].id),
        Student(name='PAVANA VEER', gender='MALE', age=20, roll_no=29, phone='7989829362', marks=100, standard_id=standards[schools['PADMAVANI'].id][(8,'B')].id),
        Student(name='SRAVANI DEVI', gender='FEMALE', age=19, roll_no=34, phone='8247857396', marks=98, standard_id=standards[schools['SAIVIJETHA'].id][(7,'B')].id),
        Student(name='SYAMALA DEVI', gender='FEMALE', age=20, roll_no=24, phone='6303660675', marks=87, standard_id=standards[schools['PADMAVANI'].id][(9,'C')].id),
        Student(name='SAI KUMAR', gender='MALE', age=19, roll_no=5, phone='8247687884', marks=88, standard_id=standards[schools['PADMAVANI'].id][(8,'B')].id),
        Student(name='THANAMAI', gender='FEMALE', age=19, roll_no=6, phone='8253457594', marks=80, standard_id=standards[schools['SAIVIJETHA'].id][(8,'A')].id),
        Student(name='KARUNAKAR', gender='MALE', age=19, roll_no=21, phone='9465454867', marks=78, standard_id=standards[schools['PADMAVANI'].id][(8,'A')].id),
        Student(name='KEVIN ROY', gender='MALE', age=19, roll_no=11, phone='7346287688', marks=68, standard_id=standards[schools['PADMAVANI'].id][(10,'B')].id),
        Student(name='MARY JON', gender='FEMALE', age=19, roll_no=12, phone='6245565469', marks=79, standard_id=standards[schools['PADMAVANI'].id][(10,'A')].id),
        Student(name='KAIRASA', gender='FEMALE', age=19, roll_no=31, phone='8763657562', marks=75, standard_id=standards[schools['PADMAVANI'].id][(10,'B')].id),
        Student(name='VARUN DHAWAN', gender='MALE', age=19, roll_no=42, phone='7458546898', marks=66, standard_id=standards[schools['SAIVIJETHA'].id][(10,'A')].id),
        Student(name='DHAWAN', gender='MALE', age=19, roll_no=46, phone='7458546890', marks=66, standard_id=standards[schools['PADMAVANI'].id][(7,'A')].id),
        Student(name='DHANUSH', gender='MALE', age=19, roll_no=44, phone='7458546891', marks=66, standard_id=standards[schools['PADMAVANI'].id][(4,'A')].id),
        Student(name='ASHWIN', gender='MALE', age=20, roll_no=23, phone='9491989615', marks=90, standard_id=standards[schools['PADMAVANI'].id][(8,'A')].id),
        Student(name='ASH', gender='MALE', age=20, roll_no=33, phone='9491989617', marks=90, standard_id=standards[schools['SAIVIJETHA'].id][(8,'A')].id),
        Student(name='WIN', gender='MALE', age=20, roll_no=43, phone='9491989618', marks=90, standard_id=standards[schools['SAIVIJETHA'].id][(8,'A')].id),
        Student(name='SHIN', gender='MALE', age=20, roll_no=53, phone='9491989619', marks=90, standard_id=standards[schools['SAIVIJETHA'].id][(8,'A')].id),
    ]

    db.add_all(students_to_add)
    db.commit()
    print(f"✅ Database seeded successfully with {len(students_to_add)} students.")

    # Close the session
    db.close()

if __name__ == "__main__":
    seed_database()
