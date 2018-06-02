# -*- coding: UTF-8 -*-
class Recette:
    def __init__(self, name, kcal, glucose=0, lipides=0, acides_gras_satures=0, proteines=0):
        self.name = name
        self.kcal = kcal
        self.glucose = glucose
        self.lipides = lipides
        self.acides_gras_satures = acides_gras_satures
        self.proteines = proteines


class Repas:
    def __init__(self, date, heure):
        self.date = date
        self.heure = heure
        self.kcal = 0
        self.glucose = 0
        self.lipides = 0
        self.acide_gras_satures = 0
        self.proteines = 0
