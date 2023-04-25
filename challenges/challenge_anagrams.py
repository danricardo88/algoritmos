def is_anagram(first_string: str, second_string: str) -> tuple:

    # Ver strings estão vazias
    if not first_string and not second_string:
        return ("", "", True)
    """Retorna uma tupla contendo duas strings ordenadas e
    um booleano"""
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        raise TypeError("As entradas devem ser strings.")

    first_list = list(first_string.lower())
    second_list = list(second_string.lower())
    _sort_list(first_list)
    _sort_list(second_list)
    first_sorted = "".join(first_list)
    second_sorted = "".join(second_list)
    return (first_sorted, second_sorted, first_sorted == second_sorted)


def _sort_list(input_list: list, start: int = 0, end: int = None) -> None:
    """Ordena a lista em ordem crescente, usando o algoritmo mergesort."""
    if end is None:
        end = len(input_list)
    if (end - start) > 1:
        middle_index = (start + end) // 2
        _sort_list(input_list, start, middle_index)
        _sort_list(input_list, middle_index, end)
        _merge_lists(input_list, start, middle_index, end)


def _merge_lists(
        input_list: list, start: int, middle_index: int, end: int) -> None:
    """Combina duas listas ordenadas em uma única lista ordenada."""
    i = start
    j = middle_index
    aux = []

    while i < middle_index and j < end:
        if input_list[i] < input_list[j]:
            aux.append(input_list[i])
            i += 1
        else:
            aux.append(input_list[j])
            j += 1

    while i < middle_index:
        aux.append(input_list[i])
        i += 1

    while j < end:
        aux.append(input_list[j])
        j += 1

    input_list[start:end] = aux
