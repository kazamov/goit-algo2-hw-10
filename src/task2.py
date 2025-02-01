# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    uncovered = set(subjects)
    schedule = []
    remaining_teachers = teachers.copy()
    while uncovered:
        candidate = None
        best_cover = 0
        for teacher in remaining_teachers:
            cover = teacher.can_teach_subjects & uncovered
            cover_count = len(cover)
            if cover_count > best_cover:
                candidate = teacher
                best_cover = cover_count
            elif cover_count == best_cover and cover_count > 0:
                if candidate and teacher.age < candidate.age:
                    candidate = teacher
        if candidate is None:
            return None
        candidate.assigned_subjects = candidate.can_teach_subjects & uncovered
        uncovered -= candidate.assigned_subjects
        schedule.append(candidate)
        remaining_teachers.remove(candidate)
    return schedule

def run_task2():
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"})
    ]

    schedule = create_schedule(subjects, teachers)
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")

if __name__ == "__main__":
    run_task2()