from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

RESUME_ALLOWED_EXTENSIONS = ("pdf", "doc", "docx")
RESUME_MAX_SIZE_BYTES = 5 * 1024 * 1024  # 5 MB

resume_extension_validator = FileExtensionValidator(
    allowed_extensions=RESUME_ALLOWED_EXTENSIONS,
    message=_("Resume must be a PDF or Word document (.pdf, .doc, .docx)."),
)


def validate_resume_file_size(value):
    if value.size > RESUME_MAX_SIZE_BYTES:
        raise ValidationError(
            _("Resume file size must not exceed %(max_mb)s MB."),
            params={"max_mb": RESUME_MAX_SIZE_BYTES // (1024 * 1024)},
        )
