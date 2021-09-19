from logging import getLogger
from operator import lt, gt
from typing import Sequence

logger = getLogger(__name__)


class DataUtils:

    @staticmethod
    def get_max_element_in_list_of_dict(iterable: Sequence[dict], dict_field: str) -> int:
        """Returns dict from list of dict where dict_field having max digital value"""
        logger.info('Getting max value from all dicts in list "%s" by field "%s"', iterable, dict_field)
        return max(iterable, key=lambda x: x[dict_field])[dict_field]

    @staticmethod
    def get_min_element_in_list_of_dict(iterable: Sequence[dict], dict_field: str) -> int:
        """Returns dict from list of dict where dict_field having min digital value"""
        logger.info('Getting min value from all dicts in list "%s" by field "%s"')
        return min(iterable, key=lambda x: x[dict_field])[dict_field]

    @staticmethod
    def elements_in_json_list_sorted_by_field(
            json_data: Sequence[dict], dict_field: str, descending: bool = False, elements_count_to_check: int = 0
    ) -> bool:
        """
        Returns True if collection 'json_data' sorted by value in field with description that is passed to 'dict_field'
        param. If param 'descending' is True, method will check descending of collection.
        elements_count_to_check = 0 - it means check all items. If this param greater than 0, method will check only
        first 'elements_count_to_check' elements.
        """
        func = DataUtils.get_max_element_in_list_of_dict if descending else DataUtils.get_min_element_in_list_of_dict
        start_value = func(json_data, dict_field)
        compare = lt if descending else gt
        if elements_count_to_check:
            collection = json_data[:elements_count_to_check]
        else:
            collection = json_data
        for item in collection[1:]:
            if compare(item[dict_field], start_value):
                start_value = item[dict_field]
            else:
                return False
        return True

    @staticmethod
    def get_node_by_field_value(data: Sequence[dict], field_name: str, field_value) -> dict:
        """Returns dict from sequence where field_name argument value equal to field_value argument"""
        node = list(filter(lambda x: x[field_name] == field_value, data))[0]
        return node

    @staticmethod
    def is_equal(data_1: dict, data_2: dict, fields_to_compare: Sequence[str]):
        """Returns True if dict1 equals to dict2 in specified fields from fields_to_compare argument"""
        for item in fields_to_compare:
            if data_1[item] != data_2[item]:
                return False, f'Field "{item}" did not matched: ' \
                              f'{repr(data_1[item])} != {repr(data_2[item])}'
        return True
