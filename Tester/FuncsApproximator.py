import math


class FuncsApproximator:
    def lin_approximate(self, data):
        sum1, sum2, sum3, sum4 = 0, 0, 0, 0
        for number in data:
            sum1 += number
            sum2 += data[number]
            sum3 += number * data[number]
            sum4 += number * number
        numerator = (sum1 * sum2 - len(data) * sum3)
        denominator = (sum1 * sum1 - len(data) * sum4)
        a = numerator / denominator
        b = (sum2 - a * sum1) / len(data)
        return (a, b)

    def log_approximate(self, data):
        new_data = {}
        for number in data.points:
            new_data[round(math.log1p(number))] = data.points[number].y
        a, b = self.lin_approximate(new_data)
        return (a, b)

    def pow_approximate(self, data):
        new_data = {}
        for number in data.points:
            new_data[math.log1p(number) - 1] = math.log1p(
                data.points[number].y - 1)
        b, a = self.lin_approximate(new_data)
        return (math.e ** a, b)
