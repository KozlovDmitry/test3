from ..my_decorators.my_decorators import speed_test
import xmltodict


class Flatten:
    def __init__(self):
        self.result_dict = None
        self.max_depth = 0

    @speed_test
    def flatten_recursive(self, d):
        self.max_depth = 0
        result_dict = {}

        def get_key(input_tuple):
            if len(input_tuple) == 2:
                start_key, value = input_tuple
                currnet_depth = 0
            elif len(input_tuple) == 3:
                start_key, value, currnet_depth = input_tuple

            if self.max_depth < currnet_depth:
                self.max_depth = currnet_depth

            if isinstance(value, dict) or isinstance(value, list) or isinstance(value, xmltodict.OrderedDict):
                iterator_obj = self.get_iter_obj(value)
                list(map(
                    lambda key_val_cort: get_key((f"{start_key}.{key_val_cort[0]}", key_val_cort[1], currnet_depth+1)),
                    iterator_obj
                ))
            else:
                result_dict[start_key] = value

        list(map(get_key, d.items()))

        self.result_dict = result_dict
        return self.result_dict

    @speed_test
    def flatten_used_queue(self, d):
        result_dict = dict()
        queue = list()

        def get_key(current_key, next_key):
            if current_key:
                return f"{current_key}.{next_key}"
            return str(next_key)

        def main_checker(item):
            key_generator = ''
            current_depth = 0
            queue.append((item, key_generator, current_depth))

            while len(queue) > 0:
                current_layer = queue[-1]
                key, value = current_layer[0]
                current_key = current_layer[1]
                current_depth = current_layer[2]

                if self.max_depth < current_depth:
                    self.max_depth = current_depth

                if isinstance(value, dict) or isinstance(value, list) or isinstance(value, xmltodict.OrderedDict):

                    queue.pop()
                    key_generator = get_key(current_key, key)
                    iterator_obj = self.get_iter_obj(value)

                    list(map(
                        lambda val: queue.append((val, key_generator, current_depth + 1)),
                        iterator_obj
                    ))
                else:
                    key_generator = get_key(current_key, key)
                    result_dict[key_generator] = value
                    queue.pop()

        list(map(main_checker, d.items()))

        return result_dict

    def get_iter_obj(self, value):
        if isinstance(value, dict) or isinstance(value, xmltodict.OrderedDict):
            return value.items()
        if isinstance(value, list):
            return enumerate(value)
        else:
            raise Exception('Available data structure - dict, list')

    def get_depth_without_atr(self):
        return self.max_depth - 1