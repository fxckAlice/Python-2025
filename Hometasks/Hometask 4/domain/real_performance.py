from .perfomance import Performance

class RealPerformance(Performance):
    def average(self) -> float:
        if not self._scores:
            return 0.0
        return float(sum(self._scores) / len(self._scores))
