from core.director import AethraDirector
from core.memory import AethraMemory
from core.planner import AethraPlanner


class AethraCore:

    def __init__(self):
        self.director = AethraDirector()
        self.memory = AethraMemory()
        self.planner = AethraPlanner()


    def process_goal(self, goal):

        # Guardamos el objetivo
        self.memory.save(
            "last_goal",
            goal
        )

        # Analizamos
        analysis = self.director.analyze_goal(
            goal
        )

        # Creamos plan
        plan = self.planner.create_plan(
            goal
        )

        return {
            "analysis": analysis,
            "plan": plan,
            "memory": self.memory.show_memory()
        }



if __name__ == "__main__":

    aethra = AethraCore()

    result = aethra.process_goal(
        "Quiero ahorrar tiempo gestionando mi empresa de transporte"
    )

    print(result)
