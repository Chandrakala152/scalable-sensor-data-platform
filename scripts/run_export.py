from src.exporter import export_json_to_csv
from src.logger import setup_logger

def main():
    setup_logger()
    export_json_to_csv()

if __name__ == "__main__":  
    main()