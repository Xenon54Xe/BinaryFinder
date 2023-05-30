from random import randint


class Gate:
    def __init__(self, index, name, logic=None):
        self.name = name
        self.index = index
        self.logic = logic
        self.current_output = None
        self.output_defined = False
        self.in_gate = []
        self.in_gate_set = False

    def get_index(self):
        return self.index

    def get_name(self):
        return self.name

    def get_output(self):
        if self.output_defined:
            return self.current_output
        return None

    def set_output(self, output):
        self.current_output = output
        self.output_defined = True

    def set_output_undefined(self):
        self.output_defined = False

    def set_in_gate(self, in_gate_list):
        self.in_gate = in_gate_list
        self.in_gate_set = True

    def set_in_gate_unset(self):
        self.in_gate_set = False


class AND(Gate):
    def __init__(self, index, name="AND"):
        and_gate_logic = {(0, 0): 0,
                          (1, 0): 0,
                          (0, 1): 0,
                          (1, 1): 1}

        super().__init__(index, name, and_gate_logic)

    def set_output(self):
        if self.in_gate_set:
            if self.in_gate[0].output_defined and self.in_gate[1].output_defined:
                in_a = self.in_gate[0].get_output()
                in_b = self.in_gate[0].get_output()
                super().set_output(self.logic[(in_a, in_b)])
            else:
                for gate in self.in_gate:
                    gate.set_output()
        else:
            raise Exception(f"La gate {self.name} tente de générer ses output à partir des gates d'entrée, "
                            f"mais celles-ci n'existent pas...")


class NOT(Gate):
    def __init__(self, index, name="NOT"):
        not_gate_logic = {0: 1,
                          1: 0}

        super().__init__(index, name, not_gate_logic)

    def set_output(self):
        if self.in_gate_set:
            if self.in_gate[0].output_defined:
                in_a = self.in_gate[0].get_output()
                super().set_output(self.logic[in_a])
            else:
                for gate in self.in_gate:
                    gate.set_output()
        else:
            raise Exception(f"La gate {self.name} tente de générer ses output à partir de la gate d'entrée, "
                            f"mais celle-ci n'existe pas...")


class NAND(Gate):
    def __init__(self, index, name="NAND"):
        nand_gate_logic = {(0, 0): 1,
                           (1, 0): 1,
                           (0, 1): 1,
                           (1, 1): 0}

        super().__init__(index, name, nand_gate_logic)

    def set_output(self):
        if self.in_gate_set:
            if self.in_gate[0].output_defined and self.in_gate[1].output_defined:
                in_a = self.in_gate[0].get_output()
                in_b = self.in_gate[0].get_output()
                super().set_output(self.logic[(in_a, in_b)])
            else:
                for gate in self.in_gate:
                    gate.set_output()
        else:
            raise Exception(f"La gate {self.name} tente de générer ses output à partir des gates d'entrée, "
                            f"mais celles-ci n'existent pas...")


def Start(input_shape_list, output_shape_list):
    if len(input_shape_list) != len(output_shape_list):
        raise Exception("Il faut que la liste des input et la liste des output soient de la même taille")

    if type(input_shape_list[0]) is tuple:
        nb_input = len(input_shape_list[0])
        for i in range(len(input_shape_list)):
            if len(input_shape_list[i]) != nb_input:
                raise Exception("Il faut que tous les ensembles d'input soient de la même taille",
                                f"Erreur au niveau de l'ensemble {i}")
    else:
        nb_input = 1

    if type(output_shape_list[0]) is tuple:
        nb_output = len(output_shape_list[0])
        for i in range(len(output_shape_list)):
            if len(output_shape_list[i]) != nb_output:
                raise Exception("Il faut que tous les ensembles d'output soient de la même taille",
                                f"Erreur au niveau de l'ensemble {i}")
    else:
        nb_output = 1

    index = 0
    logic_gates = []
    for i in range(nb_input):
        in_gate = Gate(index, f"In{i}", None)
        index += 1
        logic_gates.append(in_gate)

    for i in range(nb_output):
        out_gate = Gate(index, f"Out{i}", None)
        index += 1
        logic_gates.append(out_gate)

    for i_input_shape in range(len(input_shape_list)):
        input_shape = input_shape_list[i_input_shape]
        output_shape = output_shape_list[i_input_shape]

        for i in range(nb_input):
            name_wanted = f"In{i}"
            for gate in logic_gates:
                if gate.get_name() == name_wanted:
                    gate.set_output(input_shape[i])


# a continuer
in_list = [(1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0), (0, 0, 1, 0), (1, 0, 1, 0),
           (0, 1, 1, 0), (1, 1, 1, 0), (0, 0, 0, 1), (1, 0, 0, 1)]

out_list = [(0, 1, 1, 0, 0, 0, 0), (1, 1, 0, 1, 1, 0, 1), (1, 1, 1, 1, 0, 0, 1), (0, 1, 1, 0, 0, 1, 1),
            (1, 0, 1, 1, 0, 1, 1),
            (0, 0, 1, 1, 1, 1, 1), (1, 1, 1, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 0, 1, 1)]

in_test = [(0, 0), (1, 0), (0, 1), (1, 1)]

out_test = [1, 1, 1, 0]

Start(in_test, out_test)
