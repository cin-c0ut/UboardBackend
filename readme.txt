Booting and useful commands: 




Showing all models: 
python manage.py shell -c "from django.apps import apps; print('\n'.join([model.__name__ for model in apps.get_models()]))"
