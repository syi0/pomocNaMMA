{
	"Bubble sort": {
		"prefix": "bubble_sort",
		"body": [
			"def bubble_sort():",
			"    elements = [7, 3, 1, 2, 5]",
			"    size = len(elements)",
			" ",
			"    print('Before sorting:', elements)",
			" ",
			"    for i in range(size):",
			"        for j in range(0, size-i-1):",
			"            if elements[j] > elements[j+1]:",
			"                elements[j], elements[j+1] = elements[j+1], elements[j]",
			"                print(elements)",
			" ",
			"    print('After sorting:', elements)"
		],
		"description": "Bubble sort"
	},
	"Convert binary to decimal": {
		"prefix": "to_decimal",
		"body": [
			"def to_decimal(dana):",
			"    pom = 0",
			"    for i in range(len(dana)):",
			"        check = int(dana[-i-1])",
			"        pom += check * 2 ** i",
			"    return pom",
		],
		"description": "Konwertuje liczbę binarną na system dziesiętny"
	},
	"Convert decimal to binary": {
		"prefix": "to_binary",
		"body": [
			"def to_binary(liczba):",
			"    if liczba == 0:",
			"        return '0'",
			"    pom = ''",
			"    while liczba > 0:",
			"        pom = str(liczba % 2) + pom",
			"        liczba //= 2",
			"    return pom",
		],
		"description": "Konwertuje liczbę dziesiętną na system binarny"
	}
}
