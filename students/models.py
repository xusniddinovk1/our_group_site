from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}',
    message="Telefon raqam quyidagicha bo'lishi kerak:" "+998xxxxxxxxx"
)


class Subject(models.Model):
    objects = None
    name = models.CharField(max_length=50, blank=False, null=False)
    total_credit = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    objects = None
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(validators=[phone_regex], blank=True, null=True)
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    objects = None
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(validators=[phone_regex], blank=True, null=True)
    image = models.ImageField(upload_to='students/')
    failed_subjects = models.ManyToManyField(Subject, through='StudentSubjectFailure')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class StudentSubjectFailure(models.Model):
    objects = None
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    failed_credits = models.IntegerField()

    class Meta:
        unique_together = ('student', 'subject')  # Har bir talaba har bir fandan faqat 1 marta qoladi

    def __str__(self):
        return f"{self.student.first_name} - {self.subject.name} - {self.failed_credits} kredit"
