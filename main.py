from typing import List

Genome = List[int]
Population = List[Genome]

def generate_genome(length: int) -> Genome:
    return choices([0, 1], k=length)

def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]

def fitness(genome: Genome, things: [Thing], weight_limit: int):
    if len(genome) != len(things):
        raise ValueError("Genome and things must be of the same length.")

    weight = 0
    length = 0

    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.value
            value += thing.value

            if weight > weight_limit:
                return 0
