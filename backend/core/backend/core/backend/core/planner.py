class AethraPlanner:

    def __init__(self):
        self.name = "Aethra Planner"


    def create_plan(self, goal):

        plan = {
            "objective": goal,
            "steps": [
                "Analizar situación actual",
                "Detectar tareas que consumen tiempo",
                "Crear propuestas de mejora",
                "Medir tiempo recuperado"
            ]
        }

        return plan



if __name__ == "__main__":

    planner = AethraPlanner()

    result = planner.create_plan(
        "Ahorrar tiempo en la gestión de una empresa"
    )

    print(result)
