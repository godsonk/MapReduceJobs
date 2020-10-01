from mrjob.job import MRJob
from mrjob.step import MRStep

class NombreDeFilmsParTypes(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_titlesTypes,
                   reducer=self.reducer_count_titlesTypes)
        ]

    def mapper_get_titlesTypes(self, _, line):
        (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, en$
        yield titleType, 1

    def reducer_count_titlesTypes(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    NombreDeFilmsParTypes.run()

