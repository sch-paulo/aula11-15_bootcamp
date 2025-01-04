from interface.classes.csv_class import CsvProcessor

arquivo_csv = './data/exemplo.csv'
filtro = ['estado', 'preço']
limite = ['SP', 11.04]

csv_processor = CsvProcessor(arquivo_csv)
csv_processor.carregar_csv()
print(csv_processor.filtrar_por(filtro, limite))