# import csv
# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tehnostrelka.settings')
# django.setup()

from menu.models import Film
#
#
# def import_data_from_csv(csv_file_path):
#     with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             Film.objects.create(
#                 title=row['Name'],
#                 description=row['About'],
#                 generes=row['Genres'],
#                 keywords=row['Keywords'],
#                 image_url=row['ImageLink']
#             )
#
#
# if __name__ == "__main__":
#     csv_file_path = "films_info.csv"
#     import_data_from_csv(csv_file_path)
#
# for product in Film.objects.all():
#     if product.image_url.startswith('//'):
#         product.image_url = 'https:' + product.image_url
#         product.save()