def all_caps(input_string):
    """Заглавные букны"""
    return input_string.upper()


input_str = input("Строка с разным регистром букв")
result = all_caps(input_str)
print(result)
