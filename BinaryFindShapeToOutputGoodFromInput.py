
from random import randint

input_list = [(1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0), (0, 0, 1, 0), (1, 0, 1, 0),
              (0, 1, 1, 0), (1, 1, 1, 0), (0, 0, 0, 1), (1, 0, 0, 1)]

output_list = [(0, 1, 1, 0, 0, 0, 0), (1, 1, 0, 1, 1, 0, 1), (1, 1, 1, 1, 0, 0, 1), (0, 1, 1, 0, 0, 1, 1), (1, 0, 1, 1, 0, 1, 1),
               (0, 0, 1, 1, 1, 1, 1), (1, 1, 1, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 0, 1, 1)]

and_gate_logic = {(0, 0): 0,
                  (1, 0): 0,
                  (0, 1): 0,
                  (1, 1): 1
}

not_gate_logic = {
    0: 1,
    1: 0
}

in_test = [(0, 0), (1, 0), (0, 1), (1, 1)]

out_test = [0, 1, 1, 0]


class Gate:
    def __init__(self, logic, end=False):
        self.logic = logic
        self.current_output = None
        self.output_defined = False
        self.in_gate = []
        self.end = end

    def Is_output_defined(self):
        return self.output_defined

    def Get_output(self):
        if self.output_defined:
            return self.current_output
        else:
            return None

    def Set_output(self, input_values):
        self.current_output = self.logic[input_values]
        self.output_defined = True

    def Set_output_undefined(self):
        self.output_defined = False

    def Set_in_gate(self, in_gate_list):
        self.in_gate = in_gate_list


def Start(in_list, out_list):
    gates_list = []

    if type(in_list[0]) is tuple:
        nb_input_gate = len(in_list[0])
    else:
        nb_input_gate = 1

    if type(out_list[0]) is tuple:
        max_end_gate = len(out_list[0])
    else:
        max_end_gate = 1

    for input_case in in_list:
        first_gates = []
        total_end_gate = 0

        def Create_new_gate(gate_list):
            if randint(0, 1) == 1 and total_end_gate < max_end_gate:
                gate_end = True
            else:
                gate_end = False

            gate_type = randint(0, 1)
            if gate_type == 0:  # and gate
                gate_in_a = gate_list[randint(0, len(gate_list) - 1)]
                gate_in_b = gate_in_a
                while gate_in_b == gate_in_a:
                    gate_in_b = gate_list[randint(0, len(gate_list) - 1)]

                new_gate = Gate(and_gate_logic, gate_end)
                new_gate.Set_in_gate([gate_in_a, gate_in_b])

            else:  # not gate
                gate_in = gate_list[randint(0, len(gate_list) - 1)]

                new_gate = Gate(not_gate_logic, gate_end)
                new_gate.Set_in_gate(gate_in)

        for value in input_case:
            new_gate = Gate(None, False)
            new_gate.Set_output(value)
            first_gates.append(new_gate)

        # continuer avec système de récupération des valeurs en output