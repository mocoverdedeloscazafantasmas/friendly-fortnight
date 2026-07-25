class AethraDirector:

    def __init__(self):
        self.name = "Aethra Director"

    def analyze_goal(self, goal):

        return {
            "goal": goal,
            "status": "analizando",
            "message": "He entendido tu objetivo.",
            "next_steps": [
                "Recoger información",
                "Analizar procesos",
                "Crear un plan de mejora"
            ]
        }


if __name__ == "__main__":

    director = AethraDirector()

    result = director.analyze_goal(
        "Quiero ahorrar tiempo gestionando mi empresa"
    )

    print(result)
