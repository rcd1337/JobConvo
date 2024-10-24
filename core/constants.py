from django.db.models import TextChoices

class EducationChoices(TextChoices):
    ELEMENTARY = "elementary", "Ensino Fundamental"
    HIGH_SCHOOL = "high_school", "Ensino médio"
    TECHNOGIST = "technologist", "Tecnólogo"
    BACHELORS = "bachelors", "Ensino Superior"
    POSTGRADUATE = "postgraduate", "Pós / MBA / Mestrado"
    DOCTORATE = "doctorate", "Doutorado"
    
class SalaryRangeChoices(TextChoices):
    UP_TO_1000 = "up_to_1000", "Up to 1000"
    FROM_1001_TO_2000 = "from_1001_to_2000", "From 1001 to 2000"
    FROM_2001_TO_3000 = "from_2001_to_3000", "From 2001 to 3000"
    ABOVE_3000 = "above_3000", "Above 3000"
