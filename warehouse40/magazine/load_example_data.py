from magazine.models import Worker


def load_example_data():
    Worker.objects.all()
    member = Worker(name='Emil', surname='Refsnes', phone_number="777888555")
    member.save()
    member = Worker(name='Pawek', surname='Refsnes', phone_number="777888555")
    member.save()
    member = Worker(name='Piotr', surname='Refsnes', phone_number="777888555")
    member.save()
    print(Worker.objects.all().values())
