def all_caps(input_string):
    """ВСЕ ЗАГЛАВНЫЕ"""
    return input_string.upper()
def capitalize_words(input_string):
    """ПЕРВАЯ ЗАГЛАВНАЯ БУКВА"""
    return input_string.title()

input_str = input("Строка с разным регистром букв")
result = all_caps(input_str)
print(result)

input_string = input("Строки для теста")
result = capitalize_words(input_string)
print(result)

