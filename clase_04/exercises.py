def filtrar_pares(num_list):
    even_list = []

    for num in num_list:
        if num % 2 == 0:
            even_list += num
    return even_list