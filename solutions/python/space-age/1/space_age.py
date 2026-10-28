class SpaceAge:
    orbital_period_earth_seconds = 31_557_600
    def __init__(self, seconds):
        self.age_in_seconds = seconds

    def on_mercury(self):
        return round((self.age_in_seconds/(self.orbital_period_earth_seconds*0.2408467)),2)
        
    def on_venus(self):
        return round((self.age_in_seconds/(self.orbital_period_earth_seconds*0.61519726)),2)
        
    def on_earth(self):
        return round((self.age_in_seconds/(self.orbital_period_earth_seconds*1.0)),2)

    def on_mars(self):
        return round((self.age_in_seconds/(self.orbital_period_earth_seconds*1.8808158)),2)

    def on_jupiter(self):
        return round((self.age_in_seconds/(self.orbital_period_earth_seconds*11.862615)),2)

    def on_saturn(self):
        return round((self.age_in_seconds/(self.orbital_period_earth_seconds*29.447498)),2)

    def on_uranus(self):
        return round((self.age_in_seconds/(self.orbital_period_earth_seconds*84.016846)),2)

    def on_neptune(self):
        return round((self.age_in_seconds/(self.orbital_period_earth_seconds*164.79132)),2)
