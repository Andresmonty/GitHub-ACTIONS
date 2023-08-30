import os
def main():
    lenguaje_favorito = os.getenv("LANGUAGE")
    print(f"¡Hello world from {lenguaje_favorito} desde los GitHubs!")
if __name__ == "__main__":
    main()