from abc import ABC, abstractmethod


class Constraint(ABC):
    def __init__(self, variables):
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment):
        pass


class CSP():
    def __init__(self, variables, domains):
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP.")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable, assignment):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment
        unassigned = [v for v in self.variables if v not in assignment]

        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None


class MapColoringConstraint(Constraint):
    def __init__(self, region1, region2):
        super().__init__([region1, region2])
        self.region1 = region1
        self.region2 = region2

    def satisfied(self, assignment):
        if self.region1 not in assignment or self.region2 not in assignment:
            return True
        return assignment[self.region1] != assignment[self.region2]


def main():
    variables = {'WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T'}
    variables = [i.strip() for i in variables]
    domains = {}
    domain = {'red', 'green', 'blue'}
    domain = [i.strip() for i in domain]
    for variable in variables:
        domains[variable] = domain

    csp = CSP(variables, domains)
    reg = {'SA', 'WA'}
    reg = [i.strip() for i in reg]
    csp.add_constraint(MapColoringConstraint(reg[0], reg[1]))

    reg = {'SA', 'NT'}
    reg = [i.strip() for i in reg]
    csp.add_constraint(MapColoringConstraint(reg[0], reg[1]))

    reg = {'SA', 'Q'}
    reg = [i.strip() for i in reg]
    csp.add_constraint(MapColoringConstraint(reg[0], reg[1]))

    reg = {'SA', 'NSW'}
    reg = [i.strip() for i in reg]
    csp.add_constraint(MapColoringConstraint(reg[0], reg[1]))

    reg = {'SA', 'V'}
    reg = [i.strip() for i in reg]
    csp.add_constraint(MapColoringConstraint(reg[0], reg[1]))

    reg = {'WA', 'NT'}
    reg = [i.strip() for i in reg]
    csp.add_constraint(MapColoringConstraint(reg[0], reg[1]))

    reg = {'NT', 'Q'}
    reg = [i.strip() for i in reg]
    csp.add_constraint(MapColoringConstraint(reg[0], reg[1]))

    reg = {'Q', 'NSW'}
    reg = [i.strip() for i in reg]
    csp.add_constraint(MapColoringConstraint(reg[0], reg[1]))

    reg = {'NSW', 'V'}
    reg = [i.strip() for i in reg]
    csp.add_constraint(MapColoringConstraint(reg[0], reg[1]))

    solution = csp.backtracking_search()
    print("Solution: ", solution)

if __name__ == "__main__":
    main()
