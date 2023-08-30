import os
def main():
    nombre = os.getenv("USERNAME")
    lenguaje_favorito = os.getenv("LANGUAGE")
    print(f"¡Hello {nombre}, using {lenguaje_favorito} desde los GitHubs!")
if __name__ == "__main__":
    main()