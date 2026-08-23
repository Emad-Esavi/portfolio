from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import resume_extension_validator, validate_resume_file_size

# Create your models here.


class Profile(models.Model):
    
    full_name = models.CharField(max_length=150)
    job_title = models.CharField()
    short_bio = models.TextField()
    about = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True,
    )
    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True,
        validators=[resume_extension_validator, validate_resume_file_size],
        help_text="PDF or Word document, max 5 MB.",
    )
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50,blank=True)
    location = models.CharField(max_length=150,blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    x = models.URLField(blank=True,verbose_name="X (Twitter)")
    seo_title = models.CharField(max_length=70,blank=True)
    seo_description = models.CharField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.full_name
    
    
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    
    
class Project(models.Model):
    STATUS_CHOICES = [
        ("completed", _("Completed")),
        ("in_progress", _("In Progress")),
        ("planned", _("Planned")),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
    )
    skills = models.ManyToManyField(
        Skill,
        blank=True,
        related_name="projects",
    )
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="completed",
    )
    is_featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateField(blank=True, null=True)


    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.title
    
    
    
class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(upload_to="projects/gallery/")
    caption = models.CharField(max_length=200,blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return f"{self.project.title} - Image {self.id}"
    
    


class Experience(models.Model):
    EMPLOYMENT_TYPES = [
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
        ("contract", "Contract"),
        ("freelance", "Freelance"),
        ("internship", "Internship"),
        ("volunteer", "Volunteer"),
    ]
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    location = models.CharField(max_length=150,blank=True)
    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPES,
        default="full_time",
    )
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField()
    company_website = models.URLField(blank=True)
    company_logo = models.ImageField(
        upload_to="experience/",
        blank=True,
        null=True,
    )
    display_order = models.PositiveIntegerField(default=0)
    achievements = models.TextField(
        blank=True,
        help_text="Major accomplishments during this role."
    )
    
    
    class Meta:
        ordering = ["display_order", "-start_date"]

    def __str__(self):
        return f"{self.position} @ {self.company}"
    
    def clean(self):
        super().clean()

        if self.currently_working and self.end_date:
            raise ValidationError({
                "end_date": "Current positions cannot have an end date."
            })

        if not self.currently_working and not self.end_date:
            raise ValidationError({
                "end_date": "Please provide an end date or mark this as your current position."
            })

        if self.end_date and self.start_date > self.end_date:
            raise ValidationError({
                "end_date": "End date cannot be earlier than the start date."
            })
            
            
            
class Service(models.Model):
    ICON_CHOICES = [
        ("", "Default (check)"),
        ("check", "Check"),
        ("code", "Code"),
        ("server", "Server"),
        ("database", "Database"),
        ("terminal", "Terminal"),
        ("folder", "Folder"),
        ("globe", "Globe"),
        ("external", "External link"),
        ("python", "Python"),
        ("javascript", "JavaScript"),
        ("php", "PHP"),
        ("django", "Django"),
        ("laravel", "Laravel"),
        ("wordpress", "WordPress"),
        ("github", "GitHub"),
    ]

    title = models.CharField(max_length=150)
    short_description = models.CharField(
        max_length=255,
        help_text="A short description shown on service cards."
    )
    description = models.TextField(
        blank=True,
        help_text="Optional detailed description."
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        choices=ICON_CHOICES,
        help_text="SVG icon name from the site icon set (e.g. django, server, code).",
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True,
    )
    
    skills = models.ManyToManyField(
        Skill,
        blank=True,
        related_name="services"
    )
    

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title
    
    
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(
        max_length=150,
        help_text="Organization that issued the certificate (e.g. Harvard / CS50).",
    )
    image = models.ImageField(
        upload_to="certificates/",
        help_text="Certificate thumbnail or preview image.",
    )
    credential_url = models.URLField(
        help_text="Public verification / certificate link.",
    )
    credential_id = models.CharField(
        max_length=120,
        blank=True,
        help_text="Optional credential ID shown on the certificate.",
    )
    issued_on = models.DateField(
        blank=True,
        null=True,
        help_text="Date the certificate was issued.",
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional short description shown on the card.",
    )
    display_order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(
        default=True,
        help_text="Show this certificate on the home page.",
    )

    class Meta:
        ordering = ["display_order", "-issued_on", "title"]

    def __str__(self):
        return f"{self.title} — {self.issuer}"
    
    
class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("read", "Read"),
        ("replied", "Replied"),
        ("archived", "Archived"),
    ]
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200,blank=True)
    message = models.TextField()
    company = models.CharField(max_length=150,blank=True)
    phone = models.CharField(max_length=30,blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(blank=True,null=True)
    ip_address = models.GenericIPAddressField(blank=True,null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject or 'No Subject'}"
    
    

