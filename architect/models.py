from django.db import models
import literals

class Architect(models.Model):
    firstname_e = models.CharField( 'first name', max_length = 40 )
    firstname_h = models.CharField( literals.first_name, max_length = 40 )
    lastname_e = models.CharField( 'last name', max_length = 40 )
    lastname_h = models.CharField( literals.last_name, max_length = 40 )
    email = models.EmailField()
    portrait = models.ImageField( upload_to = 'portrait' )

    def __unicode__(self):
        return '%s %s' % (self.firstname_e, self.lastname_e)
    
class Classification(models.Model):
    title_e = models.CharField( 'title', max_length = 20 )
    title_h = models.CharField( literals.title, max_length = 20 )
    
    def __unicode__(self):
        return self.title_e

class Project(models.Model):
    title_e = models.CharField(
        max_length = 120, 
        verbose_name = 'title',
        help_text = 'A short title of this project in English' )
    title_h = models.CharField(
        max_length = 120,
        verbose_name = literals.title,
        help_text = 'A short title of this project in English' )
    address_e = models.CharField(
        max_length = 120,
        verbose_name = 'address',
        help_text = 'City or very short location information in English' )
    address_h = models.CharField( 
        max_length = 120,
        verbose_name = literals.address )
    year = models.IntegerField( )
    description_e = models.CharField(
        max_length = 400,
        verbose_name = 'description' )    
    description_h = models.CharField( 
        max_length = 400,
        verbose_name = literals.description )
    architect = models.ForeignKey( 'Architect' )
    status = models.CharField(
        max_length = 2, 
        choices = (
            ( 'PL', 'Planned' ), ( 'CX', 'Complete' ) ) )
    plot_area = models.IntegerField( )
    built_area = models.IntegerField( )
    classification = models.ForeignKey( 'Classification' )
    
    def __unicode__(self):
        return self.title_e

