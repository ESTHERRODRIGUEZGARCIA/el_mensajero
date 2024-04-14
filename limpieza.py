import re

def clean_file(input_file, output_file):
    # Leer el contenido del archivo original
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Utilizar una expresión regular para eliminar los dígitos
    cleaned_content = re.sub(r'\d+', '', content)
    
    # Escribir el contenido limpio en un nuevo archivo
    with open(output_file, 'w') as file:
        file.write(cleaned_content)

if __name__ == "__main__":
    # Asumiendo que el archivo original se llama 'warmpuplevel0.txt'
    input_file = 'warmpuplevel0.txt'
    output_file = 'brainfuck_limpio.txt'
    clean_file(input_file, output_file)
    print("Archivo limpiado y guardado como 'brainfuck_limpio.txt'")
