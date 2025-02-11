""" Instructions :

This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.

    1.Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
        A Gene is a single value 0 or 1, it can mutate (flip).
        A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
        A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.

    2.Implement these classes as you see fit.

    3.Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.

    4.Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s. Then stop and record the number of generations (iterations) it took.

Write your results in you personal biology research notebook and tell us your conclusion :). """
import random
class Gene:
    def __init__(self):
        self.value = random.randint(0,1)

    def gene_flip(self):
        self.value = 1- self.value
        return self.value
    

class Chromosome(Gene):
    def __init__(self):
        self.chromosome = [Gene() for _ in range(10)]

    def chromosome_flip(self):
        self.chromosome =  [random.randint(0,1) for _ in self.chromosome]

    
class DNA(Chromosome):
    def __init__(self):
        self.dna = [Chromosome() for _ in range(10)]
    
    def dna_flip(self):
        self.dna =  [random.randint(0,1) for _ in self.dna]

            
class Organism(DNA):
    def __init__(self, environment_parameter):       
        self.environment_parameter = environment_parameter

 # Not finished            
        
