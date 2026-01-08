class ResumeParserError(Exception):
    """
    Base exception for all resume parser errors.
    """
    pass


class UnsupportedFileFormatError(ResumeParserError):
    """
    Raised when an unsupported resume file format is provided.
    """
    pass


class ResumeLoadError(ResumeParserError):
    """
    Raised when the resume file cannot be read or parsed.
    """
    pass


class SectionParseError(ResumeParserError):
    """
    Raised when expected sections cannot be detected.
    """
    pass
