def binary_search(arr, target):
    # Definindo os índices inicial e final
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Calcula o índice do meio
        mid = (left + right) // 2
        
        # Verifica se o elemento do meio é o alvo
        if arr[mid] == target:
            return mid  # Retorna o índice onde o alvo foi encontrado
        elif arr[mid] < target:
            # Ignora a metade esquerda
            left = mid + 1
        else:
            # Ignora a metade direita
            right = mid - 1
    
    # Retorna -1 se o alvo não foi encontrado
    return -1

# Exemplo de uso
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Elemento encontrado no índice {result}")
else:
    print("Elemento não encontrado na lista")