from core.director import AethraDirector
from core.planner import AethraPlanner
from core.memory import AethraMemory
from core.time_engine import TimeRecoveryEngine


director = AethraDirector()
planner = AethraPlanner()
memory = AethraMemory()
time_engine = TimeRecoveryEngine()


def analyze_user_goal(goal):

    memory.save(
        "last_goal",
        goal
    )

    analysis = director.analyze_goal(
        goal
    )

    plan = planner.create_plan(
        goal
    )

    impact = time_engine.calculate_saved_time(
        300,
        45
    )

    return {
        "analysis": analysis,
        "plan": plan,
        "impact": impact
    }
