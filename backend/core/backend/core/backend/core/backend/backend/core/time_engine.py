class TimeRecoveryEngine:

    def __init__(self):
        self.name = "Aethra Time Recovery Engine"


    def calculate_saved_time(
        self,
        previous_minutes,
        current_minutes
    ):

        saved_time = previous_minutes - current_minutes

        if previous_minutes > 0:
            improvement = (
                saved_time / previous_minutes
            ) * 100
        else:
            improvement = 0


        return {
            "previous_time_minutes": previous_minutes,
            "current_time_minutes": current_minutes,
            "time_recovered_minutes": saved_time,
            "improvement_percentage": round(
                improvement,
                2
            )
        }



if __name__ == "__main__":

    engine = TimeRecoveryEngine()

    result = engine.calculate_saved_time(
        300,
        45
    )

    print(result)
