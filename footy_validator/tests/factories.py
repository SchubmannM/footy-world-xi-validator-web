import factory
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class NationalTeamFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())

    class Meta:
        model = "footy_validator.NationalTeam"


class ClubTeamFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())

    class Meta:
        model = "footy_validator.ClubTeam"


class FootballPlayerFactory(factory.django.DjangoModelFactory):
    full_name = factory.LazyAttribute(lambda x: faker.name())
    profile_picture_url = factory.LazyAttribute(lambda x: faker.image_url())
    profile_url = factory.LazyAttribute(lambda x: faker.url())

    class Meta:
        model = "footy_validator.FootballPlayer"

    @factory.post_generation
    def clubs(self, create, extracted, size=0, **kwargs):
        if extracted:
            self.clubs.add(*extracted)
        if size:
            ClubTeamFactory.simple_generate_batch(create, size, order=self, **kwargs)

    @factory.post_generation
    def national_teams(self, create, extracted, size=0, **kwargs):
        if extracted:
            self.national_teams.add(*extracted)
        if size:
            NationalTeamFactory.simple_generate_batch(
                create, size, order=self, **kwargs
            )


class UserSubmissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "footy_validator.UserSubmission"

    @factory.post_generation
    def players(self, create, extracted, size=0, **kwargs):
        if extracted:
            self.players.add(*extracted)
        if size:
            FootballPlayerFactory.simple_generate_batch(
                create, size, order=self, **kwargs
            )
