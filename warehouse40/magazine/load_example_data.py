from magazine.models import Worker, WarehouseZone
import csv


def load_warehouse_zones(zones):
    WarehouseZone.objects.all().delete()
    for zone in zones:
        zone_to_add = WarehouseZone(name=zone)
        zone_to_add.save()


def load_workers(filename):
    Worker.objects.all().delete()
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name, surname, phone = row['name'], row['surname'], row['phone_number']
            worker = Worker(name=name, surname=surname, phone_number=phone)
            worker.save()



def load_example_data():
    workers_filename = 'example_data/workers.csv'
    zones = ["A", "B", "C", "D", "E", "F", "G", "H"]
    # load_workers(workers_filename)
    print(Worker.objects.all().values_list())
    #load_warehouse_zones(zones)
    print(WarehouseZone.objects.all().values_list())
    #load_
