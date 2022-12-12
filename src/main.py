import random
from command import CommandFactory, Worker


# Faking a job queue
def get_job_from_pseudoqueue():
    params = [
        {"command": "get icecream",
         "scoops": 3,
         "flavors": ["strawberry", "chocolate", "caramel"]
         },
        {"command": "build house",
         "scoops": 3,
         "flavors": ["strawberry", "chocolate", "caramel"],
         "material": "wood",
         "size": 10000
         }

    ]
    random_idx = random.randint(0, len(params) -1)
    return params[random_idx]


def client_code():
    command_mapper = CommandFactory()
    worker = Worker()
    while True:
        print("get work (1)     done (2)")
        c = input("choice: ")
        if c != "1":
            return None
        job = get_job_from_pseudoqueue()
        job = command_mapper.create(job)
        worker.set_job(job)
        worker.run()


if __name__ == '__main__':
   client_code()