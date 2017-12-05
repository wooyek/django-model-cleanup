# coding=utf-8
import inspect

from django.core.exceptions import ValidationError
from django.utils.functional import cached_property


class CleanMixin(object):
    @cached_property
    def validations(self):
        return ValidationManager(self)

    def clean(self):
        self.validations()


class ValidationManager(object):
    def __init__(self, model, clean_methods=None) -> None:
        self.errors = []
        self.model = model
        self.clean_methods = clean_methods or [method for method in dir(model) if method.startswith('clean_') and callable(getattr(model, method))]

    def __call__(self):
        self.full_clean()

    def full_clean(self):
        self.errors = []
        self.collect_validation_errors()
        if self.errors:
            raise ValidationError(self.errors)

    def collect_validation_errors(self):
        for name in self.clean_methods:
            method = getattr(name, self.model)
            try:
                if inspect.isgeneratorfunction(method):
                    self.errors.extend(method())
                else:
                    error = method()
                    if isinstance(error, ValidationError):
                        self.errors.append(error)
            except ValidationError as ex:
                self.errors.append(ex)
