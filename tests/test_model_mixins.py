# coding=utf-8

from tests.app import models


def test_model_inintialization(settings):
    item = models.SomeModel()
    assert hasattr(item, "validations")
