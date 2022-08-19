from django.db import models

# Create your models here.


# class movie_company(models.Model):
#     company_id=models.IntegerField(help_text="movie_id",primary_key=True)
#     Movie_id=models.IntegerField(help_text="movie_id")
#     company_name=models.CharField(help_text="Company Name",max_length=500)
#     def __str__(self):
#       return self.company_name
#
# class gender(models.Model):
#     gender_id=models.IntegerField(help_text="gender id",primary_key=True)
#     gender_name=models.CharField(help_text="gender name",max_length=500)
#     def __str__(self):
#       return self.gender_name

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])
class movie(models.Model):
    movie_id=models.IntegerField(primary_key=True,help_text="Movie Id")
    movie_title=models.CharField(help_text="Movie Title",max_length=500,null=False)
    movie_budget=models.IntegerField(help_text="Movie Budget")
    movie_homepage=models.URLField(help_text="Movie Home Page")
    movie_overview = models.CharField(help_text="Movie overview", max_length=500, null=False)
    movie_votes_avg = models.DecimalField(help_text="Movie Budget",max_digits=8,decimal_places=2)
    movie_votes_count = models.IntegerField(help_text="Movie Budget",)
    movie_release_date = models.DateTimeField(help_text="Movie Budget")
    movie_poster = models.ImageField(help_text="Movie poster",upload_to="movie_poster",blank=True)

    def __str__(self):
        return  self.movie_title
