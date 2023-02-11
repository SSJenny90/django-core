<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from licensing.fields import License

=======
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.text import slugify
>>>>>>> eaf3bc81ec67bc1f14b05409ec99330724a6e1fc
from .choices import ProjectStatus


class ProjectQuerySet(models.query.QuerySet):
    """Query set with convenience functions for retrieving projects by status"""

    def active(self):
<<<<<<< HEAD
        """Return active projects"""
        return self.filter(status=AbstractProject.ACTIVE)

    def inactive(self):
        """Return inactive projects"""
=======
        """ Return active projects """
        return self.filter(status=AbstractProject.ACTIVE)

    def inactive(self):
        """ Return inactive projects """
>>>>>>> eaf3bc81ec67bc1f14b05409ec99330724a6e1fc
        return self.filter(status=AbstractProject.INACTIVE)


class AbstractProject(models.Model):
    """An abstract base class for research projects. If you do not want the overhead
    resulting from inner joins caused by using regular inheritance, exclude
    `research_project` from your installed apps and use this abstract class in
    your own custom Project model."""
<<<<<<< HEAD

=======
>>>>>>> eaf3bc81ec67bc1f14b05409ec99330724a6e1fc
    objects = ProjectQuerySet.as_manager()

    STATUS_CHOICES = ProjectStatus

    title = models.CharField(
<<<<<<< HEAD
        _("title"), help_text=_("The project title."), max_length=255
    )
    description = models.TextField(
        _("description"),
        help_text=_("A description of the project and expected outcomes."),
        blank=True,
        null=True,
    )
    status = models.IntegerField(
        _("status"), choices=STATUS_CHOICES.choices, default=STATUS_CHOICES.ACTIVE
    )
    lead = models.ForeignKey(
        get_user_model(),
        verbose_name=_("project lead"),
        help_text=_("This person will be acknowledged as the project leader."),
        related_name="%(class)s_as_lead",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    start_date = models.DateTimeField(
        _("start date"),
        help_text=_(
            "Start date of the survey. If this is a project proposal, enter the proposed start date."
        ),
    )
    end_date = models.DateTimeField(
        _("end date"), help_text=_("End date of the survey."), blank=True, null=True
    )

    license = License(
        help_text=_("Choose an open source license for your project."),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    inherit_license = models.BooleanField(
        _("inherit license"),
        help_text=_(
            "Related datasets must inherit the license set at the project level."
        ),
        default=True,
    )

    funding = models.JSONField(
        verbose_name=_("funding"),
        help_text=_("Include details of any funding recieved for this project."),
        null=True,
        blank=True,
    )
=======
        _('title'),
        help_text=_("The project title."),
        max_length=255)
    description = models.TextField(
        _('description'),
        help_text=_(
            "A description of the project and expected outcomes."),
        blank=True, null=True)
    status = models.IntegerField(
        _('status'),
        choices=STATUS_CHOICES.choices,
        default=STATUS_CHOICES.ACTIVE)
    lead = models.ForeignKey(
        get_user_model(),
        verbose_name=_('project lead'),
        help_text=_(
            'This person will be acknowledged as the project leader.'),
        related_name="%(class)s_as_lead",
        null=True, blank=True,
        on_delete=models.SET_NULL)
    start_date = models.DateTimeField(
        _("start date"),
        help_text=_(
            "Start date of the survey. If this is a project proposal, enter the proposed start date."),
    )
    end_date = models.DateTimeField(
        _("end date"),
        help_text=_("End date of the survey."),
        blank=True, null=True)

    license = models.ForeignKey(
        "django_licensing.License",
        verbose_name=_("license"),
        help_text=_('Choose an open source license for your project.'),
        blank=True, null=True,
        on_delete=models.SET_NULL)
    funding = models.JSONField(
        verbose_name=_('funding'),
        help_text=_(
            'Include details of any funding recieved for this project.'),
        null=True, blank=True)
>>>>>>> eaf3bc81ec67bc1f14b05409ec99330724a6e1fc

    # META
    created_by = models.ForeignKey(
        get_user_model(),
<<<<<<< HEAD
        null=True,
        blank=True,
        related_name="submitted_%(class)ss",
        on_delete=models.SET_NULL,
    )
    created = models.DateTimeField(_("date created"), auto_now_add=True)
    modified = models.DateTimeField(_("date modified"), auto_now=True)

    class Meta:
        ordering = (
            "status",
            "-start_date",
        )
        abstract = True
        verbose_name = _("project")
        verbose_name_plural = _("projects")
=======
        null=True, blank=True,
        related_name="submitted_%(class)ss",
        on_delete=models.SET_NULL)
    created = models.DateTimeField(
        _('date created'), auto_now_add=True)
    modified = models.DateTimeField(
        _('date modified'), auto_now=True)

    class Meta:
        ordering = ('status', '-start_date',)
        abstract = True
        verbose_name = _('project')
        verbose_name_plural = _('projects')
>>>>>>> eaf3bc81ec67bc1f14b05409ec99330724a6e1fc

    def get_contributors(self):
        """Returns all contributors of the project"""
        return None


<<<<<<< HEAD
class AbstractDataset(models.Model):
    doi = models.CharField(
        max_length=255, verbose_name="DOI", blank=True, null=True, unique=True
    )
    license = License(
        help_text=_("Choose an open source license for your project."),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        abstract = True


=======
>>>>>>> eaf3bc81ec67bc1f14b05409ec99330724a6e1fc
class AbstractContributor(models.Model):
    """An abstract base class for contributors to your projects. If you do
    not want the overhead resulting from inner joins caused by using regular
    inheritance, exclude `research_project` from your installed apps and
    inherit this abstract class in your own custom Contributor model.
    """
<<<<<<< HEAD

    type = models.CharField(
        max_length=255,
        verbose_name=_("name type"),
        help_text=_("Name type specification from Datacite."),
    )

    name = models.CharField(
        max_length=512,
        verbose_name=_("name"),
        help_text=_(
            "Name of the contributor. Will be automatically populated from given name and family name if left blank."
        ),
        blank=True,
    )

    given = models.CharField(
        max_length=255,
        verbose_name=_("given name"),
        help_text=_("Given name of the contributor."),
    )

    family = models.CharField(
        max_length=255,
        verbose_name=_("family name"),
        help_text=_("Family name of the contributor."),
    )
=======
    name = models.CharField(max_length=512,
                            verbose_name=_('name'),
                            help_text=_(
                                'Name of the contributor. Will be automatically populated from given name and family name if left blank.'),
                            blank=True
                            )

    nameType = models.CharField(max_length=255,
                                verbose_name=_('name type'),
                                help_text=_("Name type specification from Datacite."))

    givenName = models.CharField(max_length=255,
                                 verbose_name=_('given name'),
                                 help_text=_("Given name of the contributor."))

    familyName = models.CharField(max_length=255,
                                  verbose_name=_('family name'),
                                  help_text=_("Family name of the contributor."))
>>>>>>> eaf3bc81ec67bc1f14b05409ec99330724a6e1fc

    # "nameIdentifiers": {"$ref": "#/definitions/nameIdentifiers"},
    # "affiliation": {"$ref": "#/definitions/affiliations"},
    # "lang": {"type": "string"}

    class Meta:
        abstract = True

    def as_datacite(self):
<<<<<<< HEAD
        return {}
=======
        return {

        }


class AbstractDataset(models.Model):

    class Meta:
        abstract = True
>>>>>>> eaf3bc81ec67bc1f14b05409ec99330724a6e1fc
