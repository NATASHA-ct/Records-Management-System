import os
import django
from faker import Faker
from datetime import timedelta
from django.utils import timezone
from website.models import Record

# Set the Django settings module for the 'dcrm' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcrm.settings')

# Setup Django
django.setup()

# Function to seed records
def seed_records(num_records=10):
    fake = Faker()
    now = timezone.now()
    for i in range(num_records):
        # Generate a random timedelta to vary the created_at time
        delta_minutes = fake.random_int(min=-1440, max=0)  # Vary within last 24 hours
        record_time = now + timedelta(minutes=delta_minutes)
        
        record = Record(
            created_at=record_time,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number()[:15],  # Limit to 15 characters
            address=fake.street_address(),
            city=fake.city(),
            state=fake.state(),
            zipcode=fake.zipcode()
        )
        record.save()

# Run the seeder function
if __name__ == "__main__":
    seed_records(num_records=10)  # Adjust num_records as needed
    print("Seeder script completed.")
