import pyrebase

config = {
    "apiKey": "AIzaSyBKYKaXBpWNMgT8TlSWECmbzUSP85Eo6Wg",
    "authDomain": "live-scoreboard-fc0e5.firebaseapp.com",
    "databaseURL": "https://live-scoreboard-fc0e5-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "live-scoreboard-fc0e5",
    "storageBucket": "live-scoreboard-fc0e5.appspot.com",
    "messagingSenderId": "115739864306",
    "appId": "1:115739864306:web:09e828c04e34a53a87f46b",
    "measurementId": "G-H02FX3HRPK",
}

firebase = pyrebase.initialize_app(config)


class Match:
    def __init__(self):
        database = firebase.database()
        self.match = database.child('match').get()

    def get_value_by_key_name(self, key_name):
        for x in self.match:
            if x.key() == key_name:
                return x.val()

    @property
    def team_info(self):
        return self.get_value_by_key_name("team_info")

    @property
    def phase(self):
        return self.get_value_by_key_name("phase")

    @property
    def format(self):
        return self.get_value_by_key_name("format")

    @property
    def tournament_name(self):
        return self.get_value_by_key_name("tournament_name")

    @property
    def team_a_set_won(self):
        return self.get_value_by_key_name("team_a_set_won")

    @property
    def team_b_set_won(self):
        return self.get_value_by_key_name("team_b_set_won")

    @property
    def set_1(self):
        return self.get_value_by_key_name("set_1")

    @property
    def set_2(self):
        return self.get_value_by_key_name("set_2")

    @property
    def set_3(self):
        return self.get_value_by_key_name("set_3")


if __name__ == '__main__':
    match = Match()
    a=1



