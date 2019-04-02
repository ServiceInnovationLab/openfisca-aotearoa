# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Person


class acc__part_3__has_lodged_claim(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Has lodged a claim with the Corporation"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM100910.html"

