from django.db import models

class VisaType(models.Model):
    visa_type = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Visa Type"
        verbose_name_plural = "Visa Types"

    def __str__(self):
        return f"{self.id}: {self.visa_type}"

class Division(models.Model):
    division = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Division"
        verbose_name_plural = "Divisions"

    def __str__(self):
        return f"{self.id}: {self.division}"

class SalaryGrade(models.Model):
    salary_grade = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Salary Grade"
        verbose_name_plural = "Salary Grades"

    def __str__(self):
        return f"{self.id}: {self.salary_grade}"

class JobType(models.Model):
    job_type = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Job Type"
        verbose_name_plural = "Job Types"

    def __str__(self):
        return f"{self.id}: {self.job_type}"

class CostCenter(models.Model):
    cost_type = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Cost Center"
        verbose_name_plural = "Cost Centers"

    def __str__(self):
        return f"{self.id}: {self.cost_type}"

class Status(models.Model):
    statusType = models.TextChoices(
        'status', 'Active Transferred Contract Ended Resigned Terminated')
    medal = models.CharField(
        blank=True, choices=statusType.choices, max_length=100)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __str__(self):
        return f"{self.medal}"
    
class Project(models.Model):
    project = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.project

class EmployDetails(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    cost_center = models.ForeignKey(
        CostCenter, on_delete=models.CASCADE, verbose_name='Cost Center')
    job_type = models.ForeignKey(
        JobType, on_delete=models.CASCADE, verbose_name='Job Type')
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE, verbose_name='Division')
    salary = models.ForeignKey(
        SalaryGrade, on_delete=models.CASCADE, verbose_name='Salary Grade')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name='Project', blank=True,null=True)
    visa = models.ForeignKey(
        VisaType, on_delete=models.CASCADE, verbose_name='Visa')
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, verbose_name='Status')
    comments = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Employ Profile"

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name} - Cost Center: {self.cost_center}, Job Type: {self.job_type}, Division: {self.division}, Salary Grade: {self.salary}, Project: {self.project}, Visa: {self.visa}, Status: {self.status}, Comments: {self.comments}"
