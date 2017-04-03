from example_have_cake import have_cake

from my_planning_graph import PlanningGraph

if __name__ == '__main__':
    p = have_cake()
    graph = PlanningGraph(p, p.initial)