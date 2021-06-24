from locust import HttpUser, TaskSet, task


class UserBehavior(TaskSet):

    @task(1)
    def check_api(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f'Status Code: {response.status_code}')


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 2000

