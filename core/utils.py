from .constants import SalaryRangeChoices, EducationChoices


def count_montly_entries(model, year=None, month=None):
    """
    Counts the etotal number of entries in a given month of a specified model.
    
    If either year or month are not provided, counts all entries.
    
    Args:
        model (Model): The model to count entries from.
        year (int): The year to filter the entries by.
        month (int): The month to filter the entries by.
    
    Returns:
        int: The number of entries created in the period.
    """
    if not year or not month:
        return model.objects.all().count()
    return model.objects.filter(created_at__year=year, created_at__month=month).count()


def calculate_applicant_ranking(
    applicant_educational_level,
    applicant_salary_range_expectation, 
    job_listing_min_educational_level,
    job_listing_salary_range,
    ):
    """
    Calculates the applicant's ranking comparing their educational level and salary expectations
    with the job listing's minimum educational level and salary range.

    Args:
        applicant_educational_level (str): The applicant's educational level.
        applicant_salary_range_expectation (str): The salary range the applicant expects.
        job_listing_min_educational_level (str): The minimum educational level required for the job listing.
        job_listing_salary_range (str): The salary range offered by the job listing..

    Returns:
        int: A ranking score between 0 and 2, where:
            - 1 point is added if the applicant's educational level meets or exceeds the job's requirement.
            - 1 point is added if the applicant's salary expectation is equal to or below the job's salary range.
    """
    min_educational_level = {
        EducationChoices.ELEMENTARY : 0,
        EducationChoices.HIGH_SCHOOL : 1,
        EducationChoices.TECHNOGIST : 2,
        EducationChoices.BACHELORS : 3,
        EducationChoices.POSTGRADUATE : 4,
        EducationChoices.DOCTORATE : 5,
    }
    salary_range_dict = {
        SalaryRangeChoices.UP_TO_1000 : 0,
        SalaryRangeChoices.FROM_1001_TO_2000 : 1,
        SalaryRangeChoices.FROM_2001_TO_3000 : 2,
        SalaryRangeChoices.ABOVE_3000 : 3,
    }
    applicant_education_value = min_educational_level.get(applicant_educational_level)
    applicant_salary_value = salary_range_dict.get(applicant_salary_range_expectation)
    job_listing_education_value = min_educational_level.get(job_listing_min_educational_level)
    job_listing_salary_value = salary_range_dict.get(job_listing_salary_range)
    ranking = 0
    if applicant_education_value >= job_listing_education_value:
        ranking +=1
    if applicant_salary_value <= job_listing_salary_value:
        ranking += 1
    return ranking
