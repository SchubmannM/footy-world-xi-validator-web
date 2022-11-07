from pytest_factoryboy import register  # noqa

from footy_validator.tests import factories  # noqa
from footy_validator.tests.fixtures import *  # noqa

register(factories.NationalTeamFactory)
register(factories.ClubTeamFactory)
register(factories.FootballPlayerFactory)
register(factories.UserSubmissionFactory)
