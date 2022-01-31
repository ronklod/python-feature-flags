from UnleashClient import UnleashClient
from time import time, sleep

#setting up unleash connnection
def setupUnleash():
    client = UnleashClient(
        url="http://localhost:4242/api/",
        app_name="my-python-app",
        custom_headers={'Authorization': '*:default.f741b301a8a09519e8311b62c0423d7cdc3c9483d172e2f2e4f1ef11'})

    client.initialize_client()
    return client

#checking every second the status of the python flag
def unleashFT(client):
    while True:
        sleep(1 - time() % 1)  # run every 1 second... you can change that
        print("python flag - stnadard startegy -" +  str(client.is_enabled("python_flag")))
        print("experiment flag - traffic base strategy -" + str(client.is_enabled("experiment_flag")))

def get_user(client):
    if client.is_enabled('new_user_flow'):
        print(new_user('Rafa Nadal', '35', 'rafa@nadal.com', 'Male', '21' ))
    else:
        print(user('Rafa Nadal', '35', 'rafa@nadal.com', 'Male'))

def user(name, age, email, gender):
    return 'Name:' + name + ', Age:' + age  + ', Email:' + email + ', Gender:' + gender

def new_user(name, age, email, gender, gs_titles):
    return 'Name:' + name + ', Age:' + age  + ', Email:' + email + ', Gender:' + gender + ', Grand Slams Titles:' + gs_titles



def run():
    unleashClient = setupUnleash()
    get_user(unleashClient);
    unleashFT(unleashClient)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()





